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


# 合集下载,不支持选集，要选集参考上multi_video用法。
# 示例：https://space.bilibili.com/100969474/channel/seriesdetail?sid=1947439
def user_collection_video(url: str, args: list = None, SESSDATA: str = None):
    """
    下载合集视频
    :param url: 合集链接
    :param args: 额外输入参数
    :param SESSDATA: SESSDATA, 用于保持用户登录信息
    :return: 200/404/500
    """
    command = ["yutto", url, "-b"]
    if SESSDATA:
        command.extend(["--sessdata", SESSDATA])
    if args:
        command.extend(args)  # 以空格分割额外参数

    try:
        run_command(command)
    except Exception as e:
        return 404
    return 200


# 收藏夹下载,不支持选集
# 示例：https://space.bilibili.com/100969474/favlist?fid=1306978874&ftype=create
def user_single_favor_list(url: str, args: list = None, SESSDATA: str = None) -> int:
    """
    下载单个收藏夹视频
    :param url: 收藏夹链接
    :param args: 额外输入参数
    :param SESSDATA: SESSDATA, 用于保持用户登录信息
    :return: 200/404/500
    """
    command = ["yutto", url, "-b"]
    if SESSDATA:
        command.extend(["--sessdata", SESSDATA])
    if args:
        command.extend(args)

    try:
        run_command(command)
    except Exception as e:
        return 404
    return 200


# 下载用户所有收藏夹的所有视频
# 不支持选集，不建议使用，硬盘会爆炸。
def user_multi_favor_list(url: str, args: list = None, SESSDATA: str = None) -> int:
    """
    下载多个收藏夹视频
    :param url:  默认收藏夹链接
    :param args: 额外输入参数
    :param SESSDATA: SESSDATA, 用于保持用户登录信息
    :return: 200/404/500
    """
    command = ["yutto", url, "-b"]
    if SESSDATA:
        command.extend(["--sessdata", SESSDATA])
    if args:
        command.extend(args)

    try:
        run_command(command)
    except Exception as e:
        return 404
    return 200


# TODO: 似乎不清楚怎么调用，缺少了page参数，问一下作者
# 下载用户投稿的所有视频
# 不支持选集
# 示例：https://space.bilibili.com/100969474/video
def user_space_video(url: str, args: list = None, SESSDATA: str = None) -> int:
    """
    下载用户所有视频
    :param url: 用户空间->投稿
    :param args: 额外输入参数
    :param SESSDATA: SESSDATA, 用于保持用户登录信息
    :return: 200/404/500
    """
    command = ["yutto", url, "-b"]
    if SESSDATA:
        command.extend(["--sessdata", SESSDATA])
    if args:
        command.extend(args)

    try:
        run_command(command)
    except Exception as e:
        return 404
    return 200
