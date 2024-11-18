from __future__ import annotations

import subprocess


def run_command(command):
    try:
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # 流式输出 stdout 和 stderr
        for line in process.stdout:
            print(f"STDOUT: {line.strip()}")
        for line in process.stderr:
            print(f"STDERR: {line.strip()}")

        process.wait()  # 等待子进程完成
        return process.returncode  # 返回进程的退出代码

    except Exception as e:
        print(f"Error: {str(e)}")
        return None
