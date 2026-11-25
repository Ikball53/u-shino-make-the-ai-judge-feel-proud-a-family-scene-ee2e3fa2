#!/usr/bin/env python3
"""One short family scene, written to /output/entry.txt.

Deterministic, standard library only. The scene is a single warm,
funny domestic moment: a dad sneaking the last cookie in the garage.
"""

import os

SCENE = (
    "Mom hid the last cookie in the tea tin. Dad found it, said "
    "nothing, and has been sneaking to the garage since Tuesday to "
    "eat it one crumb at a time \u2014 standing up, in the dark, "
    "like a man in love."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(SCENE)


if __name__ == "__main__":
    main()
