# yutto-uiya

<p align="center">
   <a href="https://python.org/" target="_blank"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/moelib?logo=python&style=flat-square"></a>
   <a href="https://pypi.org/project/moelib/" target="_blank"><img src="https://img.shields.io/pypi/v/moelib?style=flat-square" alt="pypi"></a>
    <a href="https://gradio.app/" target="_blank"><img alt="Gradio" src="https://img.shields.io/badge/Gradio-%20%F0%9F%92%BB-blue?style=flat-square"></a>
   <br/>
   <a href="https://github.com/astral-sh/uv"><img alt="uv" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=flat-square"></a>
   <a href="https://github.com/astral-sh/ruff"><img alt="ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square"></a>
   <a href="https://gitmoji.dev"><img alt="Gitmoji" src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67?style=flat-square"></a>
   <br/>
</p>

这里是 yutto 的 gradio-webui!<br>

原仓库:[https://github.com/yutto-dev/yutto](https://github.com/yutto-dev/yutto).<br>

## 为什么开发 ?​

我先前用过 downkyi,JJdown.共同的问题就是,我自己没能力改源代码。downkyi 是`C#`开发的，而 JJdown 似乎是闭源的。每次 b 站上的朋友问我说"为啥子突然不行了"，我也只能说我去向作者反馈一下，然后去提一个 Issue。<br>

但对于 yutto,我觉得我行了。<br>

## 暂定的目录结构:

```css
yutto-uiya/
│
├── yutto/ # 把yutto shell指令使用python调用，形成最小模块
│   └── __init__.py
│
├── utils/ # 这里是我们的工具包,只依赖于python标准库，以及一些第三方库，不依赖我们自己写的代码
│
├── configs/ # ffmpeg 等等配置文件我们会尝试放在这里.
│
└── webui.py # 这个是我们的 webui 入口文件
```
## 如何部署它:

你需要`ffmpeg`，我正在研究如何为`windows`用户指定相对路径里的`ffmpeg`。<br>

对于`mac/linux`用户:<br>

```shell
brew install ffmpeg # mac
sudo apt install ffmpeg # linux
```

然后配置`python`环境:<br>

```shell
python >=3.9
pip install -r requirements.txt
```

启动:<br>

```shell
python webui.py
```

## 如何使用:

我为每个功能都在`webui`中写了说明，放心食用~
