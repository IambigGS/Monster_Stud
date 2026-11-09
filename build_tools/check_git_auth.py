import subprocess

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        return res.returncode, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return -1, "", str(e)

print("--- Git user config ---")
code, out, err = run_cmd("git config --global --get-regexp user")
print(out if out else f"Code {code}, err: {err}")

print("\n--- GitHub CLI (gh) status ---")
code, out, err = run_cmd("gh auth status")
print("stdout:", out)
print("stderr:", err)
print("code:", code)
