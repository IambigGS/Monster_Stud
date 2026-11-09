import subprocess

def run_cmd(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

print("System credential helper:", run_cmd("git config --system credential.helper"))

# Test git connection to Steve's remote repo
code, out, err = run_cmd("git ls-remote https://github.com/IambigGS/FUimAfly.git HEAD")
print("ls-remote code:", code)
print("ls-remote stdout:", out)
print("ls-remote stderr:", err)
