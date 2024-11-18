from __future__ import annotations

from utils.config import generate_args
from yutto import user_single_video

if __name__ == "__main__":
    args = generate_args()
    user_single_video(
        url="https://www.bilibili.com/video/BV1vZ4y1M7mQ/",
        args=args,
    )
