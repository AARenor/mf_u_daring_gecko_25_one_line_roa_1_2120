"""Write one short roast line for a make.fun bounty entry.

Standard library only, no network. The text is written as UTF-8 bytes with
no trailing newline, into MAKEFUN_OUTPUT_DIR when set, else /output.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "My watch congratulated me on a twelve-hour stand goal I hit standing "
    "at the fridge."
)


def output_dir() -> Path:
    """Return the destination folder, honouring the environment."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"

    destination = output_dir()
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
