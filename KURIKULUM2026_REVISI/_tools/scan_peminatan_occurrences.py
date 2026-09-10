import glob
import re
import os

files = sorted(glob.glob("*.md"))
total = 0
for f in files:
    c = open(f, "r", encoding="utf-8", errors="ignore").read()
    matches = re.findall(r"ST[ABC]-0\d", c)
    if matches:
        print(f"{f:55}: {len(matches)} matches")
        total += len(matches)

print("-" * 65)
print(f"Total occurrences: {total} across {len(files)} files.")
