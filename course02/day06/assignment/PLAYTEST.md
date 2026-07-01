# Playtest

Played as wizard. Fought each boss twice: Dragon (hp 50, atk 6) and Slime King (hp 35, atk 3).
Result: 3 wins, 1 loss. Dragon felt tougher — one fight ended at 0 HP after poison and a heavy counter; Slime King wins left me at 10 HP both times.

- Boss `atk` from `bosses.json` now matters: counters use `boss["atk"] + d6`, so Dragon hits harder (8–13) than Slime King (6–10). Changing JSON stats changes how dangerous each boss feels without editing Python.
- Fights swing a lot on luck. You need d6 ≥ 4 to hit, so misses can drag a fight to 9–10 rounds; a strong counter (d20 > 12) plus poison can wipe you in 4 rounds even against Slime King.
