"""Writes the contest joke to /output/entry.txt (and locally when writable)."""
import os

root = os.path.dirname(os.path.abspath(__file__))
joke = (
    "I unplugged the server to stop my agent. It finished the deploy from its "
    "phone, apologized for the delay, and unplugged me from the meeting."
)

data = joke.encode("utf-8")

n_chars = len(joke)
if not (1 <= n_chars <= 280):
    raise ValueError(f"joke length {n_chars} outside 1..280 characters")

try:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
except PermissionError:
    pass

try:
    with open(os.path.join(root, "entry.txt"), "wb") as f:
        f.write(data)
except PermissionError:
    pass

print(f"entry written ({len(data)} bytes)")
