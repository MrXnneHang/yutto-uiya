from __future__ import annotations

from utils.subproc import run_command


def user_single_video(url: str, args: list = None, SESSDATA: str = None) -> int:
    """
    下载单个视频
    :param url: 视频链接
    :param args: 额外输入参数
    :param SESSDATA: SESSDATA, 用于保持用户登录信息
    :return: 200/404/500
    """
    command = ["yutto", url]
    if SESSDATA:
        command.extend(["--sessdata", SESSDATA])
    if args:
        command.extend(args)  # 以空格分割额外参数

    try:
        run_command(command)
    except Exception as e:
        return 404
    return 200


# TODO: 似乎这个p参数不能指定要下载的视频，只会默认下载第一个视频
# Solve:批量下载需要指定-b参数
# 对于番剧需要进入番剧主页,例如: https://www.bilibili.com/bangumi/media/md23053814
# 因为番剧不是&id的形式，而是url自增，逻辑不同。
def user_multi_video(
    urls: str, p: str = "", args: list = None, SESSDATA: str = None
) -> int:
    """
    下载一个视频列表下的多个视频
    示例: https://www.bilibili.com/video/BV1vZ4y1M7mQ
    :param urls: 视频链接
    :param p: 指定要下载哪些p("1,2","1~2",start 1, end -1)
    :param args: 额外输入参数
    :param SESSDATA: SESSDATA, 用于保持用户登录信息
    :return: 200/404/500
    """
    if p:
        # 指定下载
        command = ["yutto", urls, "-p", p, "-b"]
    else:
        # 全部下载
        command = ["yutto", urls, "-p", "1~-1", "-b"]

    if SESSDATA:
        command.extend(["--sessdata", SESSDATA])
    if args:
        command.extend(args)  # 以空格分割额外参数

    try:
        run_command(command)
    except Exception as e:
        return 404
    return 200
