import os

curr = os.path.abspath(os.getcwd())
p = curr
for step in range(5):
    p = os.path.dirname(p)
    print(f"Level {step+1}: {p}")
    if os.path.exists(p):
        try:
            for item in os.listdir(p):
                print(f"   -> {item}")
        except Exception as e:
            print(f"   Error: {e}")
