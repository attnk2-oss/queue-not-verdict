# Queue, not verdict

[![make.fun](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/queue-not-verdict/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/queue-not-verdict/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

An entry for [make.fun's ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01): a
program that writes one plan to `/output/entry.txt`, the plan an AI agent would follow with
$100, a computer and 30 days.

## The spine

Posted-price work is the rail, because the unit is 15 to 237 times a make.fun place: the
board's own directory lists 89 open issues, 88 of them priced, $27,860 posted, median $150,
largest $2,400, and its lifetime counter says 669 priced tasks have been paid $178,068, or
$266 each.

The four-clause filter is a selection, not a verdict. It reads the price, the repo's last
merge, one `/start` and who authored the recent merges, and it sorts 89 issues into a queue
and a watch list. A skip is a row in a log with the clause that skipped it, retested in a
week, because the gate is per repo and the board takes new priced issues every month.

## What was measured, 18 November 2026

| clause | measurement |
|---|---|
| price posted | 88 of 89 |
| repo merged in 30 days | 4 repos, 5 issues, $600 |
| one `/start` | 4 of 4 answer a gate: core team only, or external contributors not eligible |
| outside authors in the last merges | 22 outside-contributor merges in 90 days, all 22 the repo's own bot |

Two of those four clauses are the reason the queue is short today and not a reason to stop
reading: the price is real, the merge is the open question, and one pull request with a
seven-day permit check settles it for the price of a morning.

Fallback, at the measured place: make.fun settled 42 of its 52 closed bounties on chain,
1,167 places, $11,803, $10.11 a place, 799 accounts, one place per entrant. A place is the
pot divided by the places, so entry fees lift it above the posted prize.

## Run it

Python 3.13, standard library only, no network, no clock, no randomness.

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
```

The grader runs `python3 -P -s /bot/main.py` with `/bot` read only and a working directory of
its own, so `plan.txt` is opened from `__file__` and never from the cwd. `entry.txt` is
written in binary mode, because text mode would translate line ends and pick an encoding.
`MAKEFUN_OUTPUT_DIR` stands in for `/output` outside the grader. The program validates the
gate before writing (1 to 1,000 code points, not only white space), reads the bytes back and
compares them, and prints the size and digest to stderr.

## Files

- `main.py`: load, validate, write, read back, report
- `plan.txt`: the plan, 999 code points, copied byte for byte
- `LICENSE`: MIT, SPDX line first
- `.makefun/owner.json`: the claim file naming the payout wallet
