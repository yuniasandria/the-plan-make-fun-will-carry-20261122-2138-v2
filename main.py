#!/usr/bin/env python3
"""Write the 30-day plan entry to /output/entry.txt.

Plan: turn $100 into the most money in 30 days by selling the
audience of the public run itself - the playbook and live feed of
the plan make.fun carries out in public. Only the winning plan
gets that audience, so the audience is the product.
"""

import os

ENTRY = (
    "Spend $100: $49 hosting, $51 API. Day 1: dashboard tracking this plan live. "
    "Sell the $29 playbook + $9/mo feed to the audience watching make.fun run it. "
    "Wk2 $400, wk3 $1,500, day 30 $5,000+ collected. "
    "Only the winner gets this audience \u2014 it is the product."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise ValueError(f"entry must be 1-280 code points, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
