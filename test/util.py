import subprocess, sys, os, pathlib

def cd(path):
    os.chdir(path.resolve())

def shell(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.returncode, res.stdout