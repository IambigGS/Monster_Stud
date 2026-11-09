import os

workflows_dir = r"C:\bgs\all myAssets\0myApps-All\steve_arena\FUimAfly\.github\workflows"
if os.path.exists(workflows_dir):
    for wf in os.listdir(workflows_dir):
        print("Workflow:", wf)
        with open(os.path.join(workflows_dir, wf), 'r', encoding='utf-8') as f:
            print(f.read())
            print("="*40)
else:
    print("No .github/workflows directory found.")
