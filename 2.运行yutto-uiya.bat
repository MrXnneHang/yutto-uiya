@echo off
setlocal

:: 获取 ffmpeg.exe 的绝对路径
for /f "delims=" %%i in ('dir /s /b .\ffmpeg\bin\ffmpeg.exe 2^>nul') do set FFMPEG_PATH=%%i
echo %FFMPEG_PATH%

:: 检查是否找到了 ffmpeg.exe
if not defined FFMPEG_PATH (
    echo ffmpeg.exe not found in the expected location.
    goto :END
)

:: 提取目录路径（即不包含 ffmpeg.exe）
for %%i in ("%FFMPEG_PATH%") do set FFMPEG_DIR=%%~dpi



:: 设置 YUTTO_PATH 变量并添加到 PATH
for /f "delims=" %%i in ('dir /s /b .\env\Scripts\yutto.exe 2^>nul') do set YUTTO_PATH=%%i
for %%i in ("%YUTTO_PATH%") do set YUTTO_DIR=%%~dpi
echo %YUTTO_PATH%
set PATH=%YUTTO_DIR%;%PATH%
:: 将 ffmpeg 路径添加到当前会话的 PATH
set PATH=%FFMPEG_DIR%;%PATH%

:: 启动 Python 脚本
.\env\python.exe webui.py

pause

:END
