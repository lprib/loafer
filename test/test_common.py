import subprocess
import sys

def shell(cmd):
    return subprocess.run(cmd, shell=True, cwd=sys.path[0])