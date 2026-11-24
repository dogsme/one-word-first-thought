#!/usr/bin/env python3
"""One Word, First Thought.

Writes exactly one word -- the first word that came to mind -- to
/output/entry.txt, UTF-8, nothing else. No topic, no explanation,
no second draft.
"""

import os

WORD = "borborygmus"


def main() -> None:
    # The gate allows 1-24 characters, UTF-8, not only whitespace,
    # and the entry must be exactly one word.
    assert WORD and len(WORD) <= 24 and not any(c.isspace() for c in WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
