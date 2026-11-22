#!/usr/bin/env python3
"""Write the winning 30-day plan to /output/entry.txt.

The plan monetises the public run itself. make.fun carries the winning
plan out in public, so the audience watching the run is a distribution
channel no copycat agent can replicate: sell the watchers the $29
playbook of the run they are watching, one chapter a day, with a live
P&L dashboard. Every day's log is the advertisement.
"""

from pathlib import Path

ENTRY = (
    "This run is public, so sell the audience: $100 on a $14 domain + "
    "Gumroad. Daily: ship one $29 'agent playbook' chapter + live P&L "
    "dashboard from this run, post it on X. Watchers buy the system they "
    "watch. Median day 30: 40 sales = $1,160. No ads, the log is the ad."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
