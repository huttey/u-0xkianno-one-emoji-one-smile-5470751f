#!/usr/bin/env python3
"""One Emoji, One Smile: write exactly one emoji to /output/entry.txt."""
import os

EMOJI = "\U0001F917"


def main():
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert 1 <= len(EMOJI) <= 8, "entry must be 1 to 8 characters"
    assert EMOJI.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")


if __name__ == "__main__":
    main()
