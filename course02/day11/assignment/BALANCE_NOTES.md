# Balance patch

## Evidence

From `day10/assignment/fights.csv` (64 logged rounds):


| Stat                            | Value         |
| ------------------------------- | ------------- |
| Fight commands                  | 53 / 64 (83%) |
| Defend commands                 | 2 / 64 (3%)   |
| Counter-attacks (`hit+counter`) | 9 fights      |
| Player deaths (HP → 0)          | 1 round       |


**A — Stat that worried me:** Defend was used only **2 times in 64 rounds**. Fight dominated every fight.

Dragon counter damage is `atk + d6` (see `combat.py`). With `atk: 8`, a big hit can cost **9–14 HP** and sometimes adds poison — so Defend feels too weak to try.

## Hypothesis

**B — If we lower Dragon** `atk` **from 8 → 6, players will use Defend more often** (especially after poison or a counter) instead of only spamming Fight.

## Change

**Before → after stats plan**


| Boss   | Field | Before | After | Why                                    |
| ------ | ----- | ------ | ----- | -------------------------------------- |
| Dragon | `hp`  | 50     | 50    | Keep fight length similar              |
| Dragon | `atk` | 8      | 6     | Softer counters (6+d6 instead of 8+d6) |


Updated in `assignment/bosses.json`:

```json
{"name": "Dragon", "hp": 50, "atk": 6}
```



## Retest result

Play **5 Dragon fights** after the patch. Log to `fights.csv` and check:

- [x] Did Defend show up more than 3% of commands?
- [x] Did counter-attacks feel less punishing?
- [x] Did fights still feel challenging?