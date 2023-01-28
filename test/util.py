import subprocess, sys, os, pathlib

def cd(path):
    os.chdir(path.resolve())

def shell(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.returncode, res.stdout

def command_expect_output(cmd, expected_out, expected_retcode=0):
    code, out = shell(cmd)
    assert out == expected_out
    assert code == expected_retcode