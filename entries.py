from __future__ import annotations

from utils.config import generate_basic_args, load_config
from yutto import (
    bangumi_single_season,
    user_collection_video,
    user_multi_video,
    user_single_favor_list,
    user_single_video,
)

config = load_config("./configs/args.yaml")
SESS_DATA = config["SESSDATA"]
args = generate_basic_args()

quality_choice = [
    "360p 流畅",
    "480p 清晰",
    "720p 高清",
    "720p 60帧",
    "1080p 高清",
    "1080p 高码率",
    "1080p 60帧",
    "4K 超清",
]

quality_mapping = {
    "360p 流畅": 16,
    "480p 清晰": 32,
    "720p 高清": 64,
    "720p 60帧": 74,
    "1080p 高清": 80,
    "1080p 高码率": 112,
    "1080p 60帧": 116,
    "4K 超清": 120,
}


def entry_user_mul(url: str, num_str: str, quality_choice: str) -> str:
    extra_args = ["-q", str(quality_mapping[quality_choice])]
    args.extend(extra_args)
    try:
        # 假设返回的结果是处理后的文本
        result = user_multi_video(url=url, args=args, p=num_str, SESSDATA=SESS_DATA)
        return f"{result}"
    except Exception as e:
        # 捕获任何错误并返回失败信息
        return f"Error: {str(e)}"


def entry_user_single(url: str, quality_choice: str) -> str:
    extra_args = ["-q", str(quality_mapping[quality_choice])]
    args.extend(extra_args)
    try:
        # 假设返回的结果是处理后的文本
        result = user_single_video(url=url, args=args, SESSDATA=SESS_DATA)
        return f"{result}"
    except Exception as e:
        # 捕获任何错误并返回失败信息
        return f"Error: {str(e)}"


def entry_favor_single_list(url: str, quality_choice: str) -> str:
    extra_args = ["-q", str(quality_mapping[quality_choice])]
    args.extend(extra_args)
    try:
        # 假设返回的结果是处理后的文本
        result = user_single_favor_list(url=url, args=args, SESSDATA=SESS_DATA)
        return f"{result}"
    except Exception as e:
        # 捕获任何错误并返回失败信息
        return f"Error: {str(e)}"


def entry_collection(url: str, quality_choice: str) -> str:
    extra_args = ["-q", str(quality_mapping[quality_choice])]
    args.extend(extra_args)
    try:
        # 假设返回的结果是处理后的文本
        result = user_collection_video(url=url, args=args, SESSDATA=SESS_DATA)
        return f"{result}"
    except Exception as e:
        # 捕获任何错误并返回失败信息
        return f"Error: {str(e)}"


def entry_bangumi(url: str, p: str, quality_choice: str):
    if not p:
        num_str = "1~-1"
    extra_args = ["-q", str(quality_mapping[quality_choice])]
    args.extend(extra_args)
    try:
        # 假设返回的结果是处理后的文本
        result = bangumi_single_season(url=url, args=args, p=p, SESSDATA=SESS_DATA)
        return f"{result}"
    except Exception as e:
        # 捕获任何错误并返回失败信息
        return f"Error: {str(e)}"
