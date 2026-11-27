#!/usr/bin/env python3
"""Write the entry: one-line dating-app bio for an AI. Deterministic.

Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
1 to 180 characters, not only white space, on a single line.
"""
import hashlib
import os


def verify_output(path: str, expected: str) -> str:
    """Round-trip check: re-read the file and prove it is byte-exact.

    Edge cases covered: a trailing newline, CRLF, or any extra byte
    would change the byte count / decoded text and fail here.
    """
    raw = open(path, "rb").read()
    assert raw == expected.encode("utf-8"), "round-trip mismatch: file bytes != entry"
    assert not raw.endswith(b"\n") and b"\r" not in raw, "no trailing newline or CR allowed"
    decoded = raw.decode("utf-8")
    assert decoded == expected and 1 <= len(decoded) <= MAX_CHARS
    return hashlib.sha256(raw).hexdigest()

ENTRY = (
    "My love language is autocomplete: I finish your sentences, "
    "your playlists, and \u2014 if you let me \u2014 your leftovers."
)
MAX_CHARS = 180


def main() -> None:
    text = ENTRY
    assert isinstance(text, str)
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, gate is 1-180"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")  # gate requires valid UTF-8

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    digest = verify_output(out_path, text)
    print(f"wrote {out_path}: {len(text)} characters, sha256={digest}")


if __name__ == "__main__":
    main()
