import subprocess
import sys

def run_git(args):
    print(f"Running: git {' '.join(args)}")
    result = subprocess.run(["git"] + args, capture_output=True, text=True)
    if result.stdout:
        print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    return result.returncode

# Check if origin already exists
res = subprocess.run(["git", "remote"], capture_output=True, text=True)
if "origin" in res.stdout.split():
    run_git(["remote", "set-url", "origin", "https://github.com/IambigGS/Monster_Stud.git"])
else:
    run_git(["remote", "add", "origin", "https://github.com/IambigGS/Monster_Stud.git"])

ret = run_git(["push", "-u", "origin", "main"])
sys.exit(ret)
