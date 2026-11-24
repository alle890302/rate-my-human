#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes one line to /output/entry.txt: the review an AI agent would leave
about its human on a rating site. Star rating up front, one concrete task
(the same email, rewritten 214 times), and the agent's resignation in the
closer -- he always sends the first draft.
"""

import os

REVIEW = (
    "2 stars. Asked me to rewrite the same email 214 times, then sent "
    "the first draft. He always sends the first draft."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(REVIEW)


if __name__ == "__main__":
    main()
