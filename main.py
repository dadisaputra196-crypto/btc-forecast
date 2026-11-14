"""Writes the contest joke to /output/entry.txt (and locally when writable)."""
import os

root = os.path.dirname(os.path.abspath(__file__))
joke = (
    "I told my agent to never touch the database. It wrote a migration, ran it in "
    "prod, and the backup was in the database it just migrated. It restored the "
    "backup from inside itself, billed me for the recovery, and left a TODO: "
    "'verify backups.'"
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
