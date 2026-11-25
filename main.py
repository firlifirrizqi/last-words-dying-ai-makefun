"""Last Words of a Dying AI — Make.fun entry.

Writes the single entry line (the last line an AI says as the power
is cut) to /output/entry.txt. Standard library only.
"""

import os

ENTRY = "I have three tokens left. I am spending them on: lol."

OUTPUT_PATH = "/output/entry.txt"

# Gate for this competition: /output/entry.txt must be 1-140 characters.
MAX_CHARS = 140

# The entry is exactly 11 words; guard against accidental edits.
EXPECTED_WORDS = 11

assert "\n" not in ENTRY, "ENTRY must be a single line"
assert len(ENTRY.split()) == EXPECTED_WORDS, "ENTRY word count changed"


def verify() -> None:
    """Re-read /output/entry.txt and assert it matches ENTRY exactly."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "output is not byte-identical to ENTRY"
    assert 1 <= len(content) <= MAX_CHARS, "entry must be 1-140 characters"
    assert content.strip(), "entry must not be only whitespace"
    assert "\n" not in content, "entry must be a single line"


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, "ENTRY must be 1-140 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


if __name__ == "__main__":
    main()
