from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypedDict

from uiya.utils.config import load_config

ResourceType = Literal["bangumi", "video", "video_list", "collection", "favor", "space"]
VideoQuality = Literal[
    "360p 流畅",
    "480p 清晰",
    "720p 高清",
    "720p 60帧",
    "1080p 高清",
    "1080p 高码率",
    "1080p 60帧",
    "4K 超清",
    "HDR 真彩",
    "杜比视界",
    "8K 超高清",
]
AudioQuality = Literal[
    "64kbps", "128kbps", "320kbps", "杜比全景声", "杜比音效", "Hi-Res"
]

video_quality_mapping = {
    "360p 流畅": 16,
    "480p 清晰": 32,
    "720p 高清": 64,
    "720p 60帧": 74,
    "1080p 高清": 80,
    "1080p 高码率": 112,
    "1080p 60帧": 116,
    "4K 超清": 120,
    "HDR 真彩": 125,
    "杜比视界": 126,
    "8K 超高清": 127,
}

audio_quality_mapping = {
    "64kbps": 30216,
    "128kbps": 30232,
    "320kbps": 30280,
    "杜比全景声": 30250,
    "杜比音效": 30255,
    "Hi-Res": 30251,
}

# 能够下载到的前提是，该视频具有该等级的资源，并且你具有访问权限。


class CommandStatus(TypedDict):
    """Command Status"""

    resource_type: ResourceType
    url: str
    batch_download: bool  # bangumi:True, video: False, video_list: True, collection: True, Favor: True
    support_select: bool  # bangumi: True, video: False, video_list: True, collection: False, space: False, Favor: False
    selected_p: str | None  # Optional
    SESS_DATA: str
    require_video: bool
    require_audio: bool
    require_danmaku: bool
    require_cover: bool
    debug_mode: bool
    video_quality: VideoQuality
    audio_quality: AudioQuality


@dataclass
class ConfigParser:
    config = load_config()
    SESS_DATA: str = str(config["SESS_DATA"])
    download_dir: str = str(config["download_dir"])
    login_strict: bool = bool(config["login_strict"])
    vip_strict: bool = bool(config["vip_strict"])


@dataclass
class CommandGenerator:
    """Command Generator"""

    resource_type: ResourceType
    url: str
    batch_download: bool
    support_select: bool
    selected_p: str | None = None
    SESS_DATA: str = ""
    require_video: bool = True
    require_audio: bool = True
    require_danmaku: bool = False
    require_cover: bool = False
    debug_mode: bool = False
    video_quality: VideoQuality = "360p 流畅"
    audio_quality: AudioQuality = "320kbps"
    Config = ConfigParser()

    def __post_init__(self):
        # 在 __post_init__ 中设置默认值，确保类型正确
        # 如果需要根据 CommandStatus 的值进行设置，可以在这里添加逻辑
        pass

    @classmethod
    def from_status(cls, status: CommandStatus) -> CommandGenerator:
        """从 CommandStatus 创建 CommandGenerator 实例"""
        return cls(**status)

    def url_check(self, url: str) -> bool:
        return True

    def gen_args(self):
        # ================== URL
        # URL not correct
        if self.url == "" or not self.url_check(self.url):
            raise ValueError("Invalid URL")

        # ================== RESOURCES
        # [] [] [], no resource required
        if (
            not self.require_video
            and not self.require_audio
            and not self.require_danmaku
            and not self.require_cover
        ):
            raise ValueError("No resource required")

        # TODO: 指令形式的资源选择很难处理复杂需求，很费脑子，以及可能存在逻辑冲突，应该考虑改用配置_toml来实现。
        # --danmaku-only , --video-only , --audio-only, 可以下到同一个目录下。
        self.args = []
        # C41 + C42 + C43 + C44 = 4 + 6 + 4 + 1 = 15,这特奶奶的绝对是最愚蠢的写法，但是我实在是想不到更好的办法了。
        # 1.[x] [] [] [], video only, pass!
        if (
            self.require_video
            and not self.require_audio
            and not self.require_danmaku
            and not self.require_cover
        ):
            self.args = ["yutto", self.url, "--video-only", "--no-danmaku"]
        # 2.[] [x] [] [], audio only, pass!
        if (
            not self.require_video
            and self.require_audio
            and not self.require_danmaku
            and not self.require_cover
        ):
            self.args = ["yutto", self.url, "--audio-only", "--no-danmaku"]
        # 3.[] [] [x] [], danmaku only, pass!
        if (
            not self.require_video
            and not self.require_audio
            and self.require_danmaku
            and not self.require_cover
        ):
            self.args = ["yutto", self.url, "--danmaku-only"]
        # 4.[] [] [] [x], cover only, pass!
        if (
            not self.require_video
            and not self.require_audio
            and not self.require_danmaku
            and self.require_cover
        ):
            self.args = ["yutto", self.url, "--cover-only"]
        # 5.[x] [x] [] [], video with audio, default! pass!
        if (
            self.require_video
            and self.require_audio
            and not self.require_danmaku
            and not self.require_cover
        ):
            self.args = ["yutto", self.url, "--no-danmaku"]
        # 6.[] [x] [x] [], audio with danmaku, pass!
        if (
            not self.require_video
            and self.require_audio
            and self.require_danmaku
            and not self.require_cover
        ):
            self.args = ["yutto", self.url, "--audio-only"]
        # 7.[] [] [x] [x], danmaku with cover, failed!
        # TODO:没有下载封面的情况下是无法保留封面的哦～
        if (
            not self.require_video
            and not self.require_audio
            and self.require_danmaku
            and self.require_cover
        ):
            self.args = ["yutto", self.url, "--danmaku-only", "--save-cover"]
            raise ValueError("目前暂时不支持封面+弹幕 =-=")
        # 8.[x] [] [x] [], video with danmaku,pass!
        if (
            self.require_video
            and not self.require_audio
            and self.require_danmaku
            and not self.require_cover
        ):
            self.args = ["yutto", self.url, "--video-only"]
            raise ValueError("目前暂时不支持单独下载封面，得捆绑视频资源才能下载。")
        # 9.[x] [] [] [x], video with cover, pass!
        if (
            self.require_video
            and not self.require_audio
            and not self.require_danmaku
            and self.require_cover
        ):
            self.args = [
                "yutto",
                self.url,
                "--video-only",
                "--save-cover",
                "--no-danmaku",
            ]
        # 10.[] [x] [] [x], audio with cover,pass!
        if (
            not self.require_video
            and self.require_audio
            and not self.require_danmaku
            and self.require_cover
        ):
            self.args = [
                "yutto",
                self.url,
                "--audio-only",
                "--save-cover",
                "--no-danmaku",
            ]
        # 11.[x] [x] [x] [], video with audio and danmaku,pass!
        if (
            self.require_video
            and self.require_audio
            and self.require_danmaku
            and not self.require_cover
        ):
            self.args = ["yutto", self.url]
        # 12.[x] [x] [] [x],  video with audio and cover, pass!
        if (
            self.require_video
            and self.require_audio
            and not self.require_danmaku
            and self.require_cover
        ):
            self.args = ["yutto", self.url, "--no-danmaku", "--save-cover"]
        # 13.[x] [] [x] [x], video with danmaku and cover, pass!
        if (
            self.require_video
            and not self.require_audio
            and self.require_danmaku
            and self.require_cover
        ):
            self.args = ["yutto", self.url, "--video-only", "--save-cover"]
        # 14.[] [x] [x] [x], audio with danmaku and cover, pass!
        if (
            not self.require_video
            and self.require_audio
            and self.require_danmaku
            and self.require_cover
        ):
            self.args = ["yutto", self.url, "--audio-only", "--save-cover"]
        # 15.[x] [x] [x] [x], video with audio, danmaku and cover,pass!
        if (
            self.require_video
            and self.require_audio
            and self.require_danmaku
            and self.require_cover
        ):
            self.args = ["yutto", self.url, "--save-cover"]
        # =================== BATCH DOWNLOAD
        if self.support_select and self.selected_p is not None:
            batch_download_args = ["-b", "-p", self.selected_p]
            self.args.extend(batch_download_args)

        # =================== VIDEO QUALITY
        video_quality_args = ["-q", str(video_quality_mapping[self.video_quality])]
        if self.require_video:
            self.args.extend(video_quality_args)

        # =================== AUDIO QUALITY
        audio_quality_args: list[str] = [
            "-aq",
            str(audio_quality_mapping[self.audio_quality]),
        ]
        if self.require_audio:
            self.args.extend(audio_quality_args)

        # =================== DOWNLOAD DIRECTORY
        download_dir_args: list[str] = ["--dir", self.Config.download_dir]
        self.args.extend(download_dir_args)

        # =================== SESS DATA
        sess_data_args: list[str] = ["-c", self.Config.SESS_DATA]
        if self.Config.SESS_DATA != "":
            self.args.extend(sess_data_args)

        # debug mode
        if self.debug_mode:
            print("=================== DEBUG MODE ↓===================")
            print(self.args)
            print("=================== DEBUG MODE ↑===================")

        return self.args
