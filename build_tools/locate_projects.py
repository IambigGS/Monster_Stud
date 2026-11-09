import os

# Let's inspect the parent directories of the current working directory
current_dir = os.path.abspath(os.getcwd())
print("Current dir:", current_dir)

parent_1 = os.path.dirname(current_dir)
print("\nParent 1:", parent_1)
if os.path.exists(parent_1):
    try:
        entries = os.listdir(parent_1)
        for e in entries:
            print("  [P1 entry]:", e)
    except Exception as ex:
        print("  Error listing P1:", ex)

parent_2 = os.path.dirname(parent_1)
print("\nParent 2:", parent_2)
if os.path.exists(parent_2):
    try:
        entries = os.listdir(parent_2)
        for e in entries:
            print("  [P2 entry]:", e)
    except Exception as ex:
        print("  Error listing P2:", ex)
