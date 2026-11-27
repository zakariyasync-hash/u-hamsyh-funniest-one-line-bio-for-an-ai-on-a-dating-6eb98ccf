# FLOW

1. `main.py` holds one fixed bio string (112 characters).
2. It validates the gate first: UTF-8, single line, 1–180 chars, not whitespace-only.
3. It writes the string exactly to `/output/entry.txt` (no trailing newline).
4. Verify: read the file back, count characters, compare to the string, sha256.
