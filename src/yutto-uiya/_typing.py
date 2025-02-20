from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, Optional, TypedDict

ResourceType = Literal["bangumi", "video", "video_list", "collection", "favor", "space"]
VideoQuality = Literal["360p 流畅", "480p 清晰", "720p 高清", "720p 60帧", "1080p 高清", "1080p 高码率", "1080p 60帧", "4K 超清", "HDR 真彩", "杜比视界", "8K 超高清"]
AudioQuality = Literal["64kbps", "128kbps", "320kbps", "杜比全景声", "杜比音效", "Hi-Res"]


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
    "8K 超高清": 127
}

audio_quality_mapping = {
    "64kbps": 30216,
    "128kbps": 30232,
    "320kbps": 30280,
    "杜比全景声": 30250,
    "杜比音效": 30255,
    "Hi-Res": 30251
}

# 能够下载到的前提是，该视频具有该等级的资源，并且你具有访问权限。



class CommandStatus(TypedDict):
    """Command Status"""
    resource_type: ResourceType
    url: str
    batch_download: bool # bangumi:True, video: False, video_list: True, collection: True, Favor: True
    support_select:bool # bangumi: True, video: False, video_list: True, collection: False, space: False, Favor: False
    selected_p: str | None # Optional
    SESS_DATA: str
    require_video: bool
    require_audio: bool
    require_danmaku: bool
    video_quality: VideoQuality
    audio_quality: AudioQuality

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
    video_quality: VideoQuality = "360p 流畅"
    audio_quality: AudioQuality = "320kbps"
    args: list[str] = field(default_factory=list)

    def __post_init__(self):
        # 在 __post_init__ 中设置默认值，确保类型正确
        # 如果需要根据 CommandStatus 的值进行设置，可以在这里添加逻辑
        pass

    @classmethod
    def from_status(cls, status: CommandStatus) -> CommandGenerator:
        """从 CommandStatus 创建 CommandGenerator 实例"""
        return cls(**status)

    def set_default_args(self):
        self.require_video = True
        self.require_audio = True
        self.require_danmaku = False

    def url_check(self, url: str) -> bool:
        return True

    def gen_args(self):
        # ================== URL
        # URL not correct
        if self.url == "" or not self.url_check(self.url):
            raise ValueError("Invalid URL")

        # ================== RESOURCES
        # [] [] [], no resource required
        if not self.require_video and not self.require_audio and not self.require_danmaku:
            raise ValueError("No resource required")

        self.args = []
        # [x] [] [], video only
        if self.require_video and not self.require_audio and not self.require_danmaku:
            self.args = ["yutto",self.url,"--video-only","--no-danmaku"]
        # [] [x] [], audio only
        if not self.require_video and self.require_audio and not self.require_danmaku:
            self.args = ["yutto",self.url,"--audio-only","--no-danmaku"]
        # [] [] [x], danmaku only
        if not self.require_video and not self.require_audio and self.require_danmaku:
            self.args = ["yutto", self.url,"--danmaku-only"]
        # [x] [x] [], video with audio, default!
        if self.require_video and self.require_audio and not self.require_danmaku:
            self.args = ["yutto", self.url,"--no-danmaku"]
        # [] [x] [x], audio with danmaku
        if not self.require_video and self.require_audio and self.require_danmaku:
            self.args = ["yutto",self.url,"--audio-only"]
        # [x] [x] [x], video,audio,danmaku
        if self.require_video and self.require_audio and self.require_danmaku:
            self.args = ["yutto",self.url]

        # =================== VIDEO QUALITY
        video_quality_args = ["-q",str(video_quality_mapping[self.video_quality])]
        if self.require_video:
            self.args.extend(video_quality_args)

        # =================== AUDIO QUALITY
        audio_quality_args: list[str] = ["-aq",str(audio_quality_mapping[self.audio_quality])]
        if self.require_audio:
            self.args.extend(audio_quality_args)

        return self.args
