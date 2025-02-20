from __future__ import annotations

import gradio as gr
from _typing import AudioQuality, VideoQuality
from api import entry_bangumi, entry_collection, entry_favorlist, entry_user_video, entry_user_video_list

video_quality_choice = list(VideoQuality.__args__) # type: ignore
audio_quality_choice = list(AudioQuality.__args__) # type: ignore

# 主界面布局
with gr.Blocks() as demo:
    with gr.Tab("用户视频"):
        with gr.Tab("单个视频"):
            # 添加说明文本区域
            gr.Markdown(
                """
            ## 对正在播放用户投稿视频下载（单视频，或者多视频的p1）
            示例链接🔗:
            - [https://www.bilibili.com/video/BV1vZ4y1M7mQ](https://www.bilibili.com/video/BV1vZ4y1M7mQ)

            用法：
            - 输入框URL:必填，输入想要下载的的视频链接
            - 资源选择: 可以单独选择或者组合选择。只选择画面则下载视频没有声音。
            - 清晰度:如果不存在指定的清晰度或者该清晰度不具有访问权限，那么会降低清晰度进行下载，更高清晰度需要大会员。大会员需要填写`configs/args.yaml`中的SESS_DATA并且用户自身具有大会员权限。
            点击按钮触发下载。
            - 音频质量: 同清晰度。不用多说了哈。

            点击下载开始下载哈～欢迎自由尝试并且反馈 bug.
            """
            )
            # url
            url = gr.Textbox(label="URL (视频网址，详细见参考链接)")

            # 资源选择 , checkbox, video, audio, danmaku
            require_video = gr.Checkbox(label="画面", value=True)
            reuiqre_audio = gr.Checkbox(label="音频", value=True)
            reuiqre_danmaku = gr.Checkbox(label="弹幕", value=False)

            # 下载质量
            video_quality = gr.Dropdown(
                choices=video_quality_choice, # type: ignore
                value=video_quality_choice[4], # type: ignore
                label="Quality",
                info="选择你想要的清晰度(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "1080p 高清"
            )
            audio_quality = gr.Dropdown(
                choices=audio_quality_choice, # type: ignore
                value=audio_quality_choice[2], # type: ignore
                label="Audio Quality",
                info="选择你想要的音频质量(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "320kbps 高品质"
            )

            download_button = gr.Button("开始下载")

            output = gr.Textbox(label="结果", interactive=False)

            download_button.click(entry_user_video, inputs=[url,
                                                            require_video,
                                                            reuiqre_audio,
                                                            reuiqre_danmaku,
                                                            video_quality,
                                                            audio_quality], outputs=output)

        with gr.Tab("视频列表（多个视频）"):
            # 添加说明文本区域
            gr.Markdown(
                """
            ## 对正在播放用户投稿视频下载：(支持多p,不指定默认全下)
            示例链接🔗:
            - [https://www.bilibili.com/video/BV1vZ4y1M7mQ](https://www.bilibili.com/video/BV1vZ4y1M7mQ)

            用法：
            - 输入框URL:必填，输入正在播放的视频链接
            - 选集:选填，选择要下载的p,支持写法`1,2,3`或`1~3`,全部下载`1~-1`,可以自己探索一下。不填写默认下载全部。
            - 资源选择： 参见用户视频-单个视频的说明。
            - 清晰度： 参见用户视频-单个视频的说明。
            - 音频质量： 参见用户视频-单个视频的说明。

            点击按钮触发下载。
            """
            )

            # 输入框
            url = gr.Textbox(label="URL (视频网址，详细见参考链接)")

            # 选集
            select_p = gr.Textbox(
                label="选集 (输入比如这样的,1,2,3 or 1~3 or 1~-1,注意英文逗号分隔)",
                value="1~-1",
            )

            # 资源选择
            require_video = gr.Checkbox(label="画面", value=True)
            reuiqre_audio = gr.Checkbox(label="音频", value=True)
            reuiqre_danmaku = gr.Checkbox(label="弹幕", value=False)

            # 下拉菜单选择质量
            video_quality = gr.Dropdown(
                choices=video_quality_choice, # type: ignore
                value=video_quality_choice[4], # type: ignore
                label="Quality",
                info="选择你想要的清晰度(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "1080p 高清"
            )
            audio_quality = gr.Dropdown(
                choices=audio_quality_choice, # type: ignore
                value=audio_quality_choice[2], # type: ignore
                label="Audio Quality",
                info="选择你想要的音频质量(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "320kbps 高品质"
            )

            # 创建一个按钮来触发下载
            download_button = gr.Button("开始下载")

            # 输出框来显示处理结果（如成功或错误信息）
            output = gr.Textbox(label="结果", interactive=False)

            # 将按钮与数据处理函数连接
            download_button.click(
                entry_user_video_list,
                inputs=[url, select_p, require_video, reuiqre_audio, reuiqre_danmaku, video_quality, audio_quality],
                outputs=output,
            )

    with gr.Tab("收藏夹"):
        gr.Markdown(
        """
        ## 对用户整个收藏夹下载：(不支持默认收藏夹，不建议尝试)
        示例链接🔗:
        - [https://space.bilibili.com/100969474/favlist?fid=1306978874&ftype=create](https://space.bilibili.com/100969474/favlist?fid=1306978874&ftype=create)

        用法：
        - 输入框URL:指定收藏夹地址，参考示例，不支持默认收藏夹。
        - 资源选择： 参见用户视频-单个视频的说明。
        - 清晰度： 参见用户视频-单个视频的说明。
        - 音频质量： 参见用户视频-单个视频的说明。

        点击按钮触发下载。
        """
        )
        # 输入框
        url = gr.Textbox(label="URL (视频网址,详细见参考链接)")

        # 资源选项
        require_video = gr.Checkbox(label="画面", value=True)
        reuiqre_audio = gr.Checkbox(label="音频", value=True)
        reuiqre_danmaku = gr.Checkbox(label="弹幕", value=False)

        # 质量
        video_quality = gr.Dropdown(
            choices=video_quality_choice, # type: ignore
            value=video_quality_choice[4], # type: ignore
            label="Quality",
            info="选择你想要的清晰度(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "1080p 高清"
        )
        audio_quality = gr.Dropdown(
            choices=audio_quality_choice, # type: ignore
            value=audio_quality_choice[2], # type: ignore
            label="Audio Quality",
            info="选择你想要的音频质量(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "320kbps 高品质"
        )

        # 创建一个按钮来触发下载
        download_button = gr.Button("开始下载")

        # 输出框来显示处理结果（如成功或错误信息）
        output = gr.Textbox(label="结果", interactive=False)

        # 将按钮与数据处理函数连接
        download_button.click(entry_favorlist, inputs=[url,reuiqre_audio,require_video,reuiqre_danmaku,video_quality,audio_quality], outputs=output)
    with gr.Tab("合集"):
        gr.Markdown(
            """
        ## 对用户发布合集下载：（不支持选集，只能全下）
        示例链接🔗:
        - [https://space.bilibili.com/100969474/channel/seriesdetail?sid=1947439](https://space.bilibili.com/100969474/channel/seriesdetail?sid=1947439)

        用法：
        - 输入框URL:指定合集地址，参考示例
        - 资源选择： 参见用户视频-单个视频的说明。
        - 清晰度： 参见用户视频-单个视频的说明。
        - 音频质量： 参见用户视频-单个视频的说明。

        点击按钮触发下载。
            """
        )
        # 输入框
        url = gr.Textbox(label="URL (视频网址,详细见参考链接)")

        # 资源选项
        require_video = gr.Checkbox(label="画面", value=True)
        require_audio = gr.Checkbox(label="音频", value=True)
        require_danmaku = gr.Checkbox(label="弹幕", value=False)

        # 质量
        video_quality = gr.Dropdown(
            choices=video_quality_choice, # type: ignore
            value=video_quality_choice[4], # type: ignore
            label="Quality",
            info="选择你想要的清晰度(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "1080p 高清"
        )
        audio_quality = gr.Dropdown(
            choices=audio_quality_choice, # type: ignore
            value=audio_quality_choice[2], # type: ignore
            label="Audio Quality",
            info="选择你想要的音频质量(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "320kbps 高品质"
        )

        # 将按钮与数据处理函数连接
        download_button.click(entry_collection, inputs=[url, require_video, require_audio, require_danmaku, video_quality, audio_quality], outputs=output)

        # 输出框来显示处理结果（如成功或错误信息）
        output = gr.Textbox(label="结果", interactive=False)
    with gr.Tab("番剧"):
        gr.Markdown(
            """
        ## 对番剧进行下载：（支持选集，不输入指定选集默认全下）
        示例链接🔗:
        - 播放中：[https://www.bilibili.com/bangumi/play/ss45957](https://www.bilibili.com/bangumi/play/ss45957)
        - 首页：[https://www.bilibili.com/bangumi/media/md21087073](https://www.bilibili.com/bangumi/media/md21087073)

        用法：
        - 输入框URL:指定番剧首页地址，参考示例
        - 选择集数： `1,2,3` 或者 `1~3` 或者 `1~-1`全下，不输入默认全下。
        - 资源选择: 可以单独选择或者组合选择。只选择画面则下载视频没有声音。
        - 清晰度:如果不存在指定的清晰度或者该清晰度不具有访问权限，那么会降低清晰度进行下载，更高清晰度需要大会员。大会员需要填写`configs/args.yaml`中的SESS_DATA并且用户自身具有大会员权限。
        点击按钮触发下载。
        - 音频质量: 同清晰度。不用多说了哈。

        点击按钮触发下载。
        """
        )
        # 输入框
        url = gr.Textbox(label="URL (视频网址,详细见参考链接)")

        # 选集
        select_p = gr.Textbox(
                label="选集 (输入比如这样的,1,2,3 or 1~3 or 1~-1,注意英文逗号分隔)",
                value="1~-1",
            )

        # 资源
        require_video = gr.Checkbox(label="画面", value=True)
        require_audio = gr.Checkbox(label="音频", value=True)
        require_danmaku = gr.Checkbox(label="弹幕", value=False)

        # 质量
        video_quality = gr.Dropdown(
            choices=video_quality_choice, # type: ignore
            value=video_quality_choice[4], # type: ignore
            label="Quality",
            info="选择你想要的清晰度(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "1080p 高清"
        )
        audio_quality = gr.Dropdown(
            choices=audio_quality_choice, # type: ignore
            value=audio_quality_choice[2], # type: ignore
            label="Audio Quality",
            info="选择你想要的音频质量(视频具有该资源并且你有访问权限,否则自动降级)",  # 默认选择 "320kbps 高品质"
        )

        # 创建一个按钮来触发下载
        download_button = gr.Button("开始下载")

        # 输出框来显示处理结果（如成功或错误信息）
        output = gr.Textbox(label="结果", interactive=False)

        # 将按钮与数据处理函数连接
        download_button.click(entry_bangumi, inputs=[url, select_p, require_video, require_audio, require_danmaku, video_quality, audio_quality], outputs=output)

    with gr.Tab("常见问题"):
        gr.Markdown(
            """
        ## 常见问题和反馈（见最后）:
        ### 1.为什么不能下其他清晰度的视频？
        如果你已经下载了某个视频，并且想要下载它其他的清晰度，应该需要你手动删除先前的下载记录（把`./download`下方的相关的视频或者文件夹整个删掉即可。）
        ### 2.为什么无法下载高清晰度视频？和番剧？
        你需要先获取SESS_DATA并且填入`./configs/args.yaml`.<br>
        如果你是大会员，你还有应该保证设置`args.yaml`中的`vip_strict`和`login_strict`同时为true,否则容易被当作普通用户。<br>
        如果你是普通用户，你应该保证`login_strict`为true,`vip_strict`为false.否则会因为大会员校验失败而无法下载视频。<br>
        如果填写了`SESS_DATA`那么总是应该保证`login_strict`为true,它会校验你的`SESS_DATA`是否有效。<br>
        ### 3.yutto is not accessible
        ![](https://image.baidu.com/search/down?url=http://i0.hdslb.com/bfs/new_dyn/886152ec5fbbe3baf74e836960215c5360547448.png)
        参见视频:[yutto is not accessible 解决方法 | yutto-uiya v1.0.1](https://www.bilibili.com/video/BV1c1zqYLEAE/)<br>

        ## 我应该在哪里反映我碰到的相关问题？
        你应该首先查阅该页面，然后查看终端的信息看自己是否能够解决。如果依然不能解决，那么请到:<br>
        [一目生的个人空间](https://space.bilibili.com/556737824?spm_id_from=333.788.0.0)<br>
        你可以私信我或者在我相关视频底下留言。<br>

        """
        )
    with gr.Tab("关于 yutto-uiya"):
        gr.Markdown(
            """
        ## 它的核心是`yutto`:
        作者原仓库:[yutto](https://github.com/yutto-dev/yutto)<br>
        我只是写了这个 gradio-WebUI:[yutto-uiya](https://github.com/MrXnneHang/yutto-uiya/)<br>

        如果有更多关于界面和操作上的优化，以及功能的需求欢迎补充，因为`yutto`的功能实际上还有好多有待发掘。<br>
        我会考虑尝试进行拓展。<br>

        最后，祝各位使用愉快!<br>

        ![](https://image.baidu.com/search/down?url=https://img3.doubanio.com/view/photo/m/public/p2915590863.webp)
        """
        )



if __name__ == "__main__":
    # 启动 gradio
    demo.launch()
