import subprocess

def test_repo(name):
    url = f"https://github.com/IambigGS/{name}.git"
    res = subprocess.run(f"git ls-remote {url} HEAD", capture_output=True, text=True, shell=True)
    print(f"Repo {name}: code={res.returncode}, out={res.stdout.strip()}, err={res.stderr.strip()[:100]}")

test_repo("MonsterStud")
test_repo("Monster-Stud")
test_repo("monster-stud")
test_repo("monsterstud")
