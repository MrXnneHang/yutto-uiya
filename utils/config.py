from __future__ import annotations

import os
from pathlib import Path

import yaml

# 读取配置文件


def load_config(path: str) -> dict:
    """读取配置文件到字典"""

    try:
        with Path(path).open(encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        # 打印错误信息
        print(f"配置文件 {path} 不存在")
        return {}


def write_config(path: str, data: dict) -> None:
    """写入配置文件"""
    with Path(path).open("w", encoding="utf-8") as f:
        yaml.dump(data, f)
    print(f"配置文件 {path} 写入成功")


def generate_basic_args() -> str:
    """根据args.yaml生成基础参数"""
    config = load_config("./configs/args.yaml")
    args = ["-d", config["download_dir"]]

    if config["SESSDATA"]:
        args.extend(["-c", config["SESSDATA"]])
        if config["vip_strict"]:
            args.extend(["--vip-strict"])
        if config["login_strict"]:
            args.extend(["--login-strict"])

    # TODO: 把--video-only,--audio-only,--no-danmaku做成webui中的勾选项目
    if config["no_danmaku"]:
        args.extend(["--no-danmaku"])

    return args
