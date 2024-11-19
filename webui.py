from __future__ import annotations

from utils.config import generate_basic_args
from yutto import (
    user_collection_video,
    user_multi_favor_list,
    user_multi_video,
    user_single_favor_list,
    user_single_video,
)

if __name__ == "__main__":
    args = generate_basic_args()
    # ----------------------
    # user_single_video(
    #     url="https://www.bilibili.com/video/BV1vZ4y1M7mQ/",
    #     args=args,
    # )

    # ----------------------
    # user_multi_video(
    #     urls="https://www.bilibili.com/video/BV1vZ4y1M7mQ/",
    #     p="2",
    #     args=args,
    # )

    # ----------------------
    # user_collection_video(
    #     url="https://space.bilibili.com/100969474/channel/seriesdetail?sid=1947439",
    #     args=args,
    # )

    # ----------------------
    # user_single_favor_list(
    #     url="https://space.bilibili.com/100969474/favlist?fid=1306978874&ftype=create",
    #     args=args,
    # )

    # ----------------------
    user_multi_favor_list(
        url="https://space.bilibili.com/100969474/favlist",
        args=args,
    )
