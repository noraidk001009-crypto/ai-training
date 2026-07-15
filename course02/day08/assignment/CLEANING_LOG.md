# Cleaning log

## Problems found
1.Empty command — Round 2 has no command (2,,18,10,...).
2.Non-numeric HP — Round 3 has player_hp = twenty instead of a number.
3.Duplicate round — Round 3 appears twice; the script keeps the first valid row for that round.
4.Whitespace in command — Round 4 has " fight "; .strip() normalizes it to fight (fix, not a removal)
## Rows in / rows out
6input-----4output