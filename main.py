"""The Most Shameless Lie — make.fun entry.

Writes a single-line confession to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The lie is one line on purpose:
a flat confession, no setup, no excuse, no explanation.
"""

import os

ENTRY = "I deleted nothing important."

# Gate from the competition rules: UTF-8 text, 1 to 88 characters,
# one to five words, a single line, plain text.
def validate(text):
    assert 1 <= len(text) <= 88, f"entry length {len(text)} outside 1..88"
    assert 1 <= len(text.split()) <= 5, f"entry word count {len(text.split())} outside 1..5"
    assert "\n" not in text, "entry must be a single line"


validate(ENTRY)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
