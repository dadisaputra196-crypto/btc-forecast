import os

root = os.path.dirname(os.path.abspath(__file__))
joke = "Pair programming with an AI: I explain the bug, it explains Python\'s history, then we both apologize to the rubber duck."

data = joke.encode("utf-8")

# Validate joke length: must be 1..280 characters
n_chars = len(joke)
if not (1 <= n_chars <= 280):
    raise ValueError(f"joke length {n_chars} outside 1..280 characters")

try:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
except PermissionError:
    pass

with open(os.path.join(root, "entry.txt"), "wb") as f:
    f.write(data)

print(f"entry written ({len(data)} bytes)")
