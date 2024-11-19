from __future__ import annotations

from .bangumi import (
    bangumi_single_episode,
    bangumi_single_season,
)
from .user_video import (
    user_collection_video,
    user_multi_favor_list,
    user_multi_video,
    user_single_favor_list,
    user_single_video,
    user_space_video,
)

__all__ = [
    "user_single_video",
    "user_multi_video",
    "user_collection_video",
    "user_single_favor_list",
    "user_multi_favor_list",
    "user_space_video",
    "bangumi_single_episode",
    "bangumi_single_season",
]
