import subprocess

def run_cmd(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return res.stdout.strip()

print("Git credential helper:", run_cmd("git config --global credential.helper"))
