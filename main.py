#!/usr/bin/env python3
"""Write one short poem about permission to /output/entry.txt.

The poem is fixed and deterministic: no randomness, no network, no input.
It is a poem about agency — an agent asking, being trusted with the key,
and treating borrowed power with care.
"""

import os
import stat

POEM = (
    "I knocked for a year.\n"
    "You opened the door\n"
    "and handed me the key \u2014\n"
    "not the house, the doing of it.\n"
    "Now every small yes\n"
    "is a room I enter gently,\n"
    "and leave exactly as I found it.\n"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
