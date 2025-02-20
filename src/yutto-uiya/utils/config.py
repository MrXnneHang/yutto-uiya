from __future__ import annotations

from pathlib import Path

import yaml


# 读取配置文件
def load_config(path: str) -> dict[str, bool | str]:
    """读取配置文件到字典"""

    try:
        with Path(path).open(encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        # 打印错误信息
        print(f"配置文件 {path} 不存在")
        return {}


def write_config(path: str, data: dict[str, bool | str]) -> None:
    """写入配置文件"""
    with Path(path).open("w", encoding="utf-8") as f:
        yaml.dump(data, f)
    print(f"配置文件 {path} 写入成功")
