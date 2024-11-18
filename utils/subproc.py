from __future__ import annotations

import subprocess
import sys


def run_command(command):
    try:
        process = subprocess.run(
            command, text=True, stdout=sys.stdout, stderr=sys.stderr
        )
        return process.returncode
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, [], [str(e)]
