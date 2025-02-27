from __future__ import annotations


from typing import Literal, TypedDict

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
