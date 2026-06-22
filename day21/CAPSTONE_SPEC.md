# Nora capstone spec

## MVP
- type **fight** to kill the dragon, roll the dice to choose how many **chance** you have to fight.
- type **handle** to begin a new turn, type **quit** to quit the game
- If player type other words like **pig**, run the game as usual


## Tasks
1. **Day 19** — `main.py`: welcome message + input loop until `quit`.
2. **Day 19** — `fight` command: two `roll_d6()` calls, compare, print result.
3. **Day 20** — Catch bad input; print "Type fight or quit." instead of crashing.
4. **Day 20** — Add `wins` and `losses` variables; update after each fight.
5. **Day 21** — Run 3 tests with different inputs, fix bugs
## Nice-to-have
- Count wins and losses and show the score after each fight.
- Type `potion` once per game to get +1 on your next roll.

## Example
- MVP: fight is MVP because without rolling dice and fighting, there is no game — only an empty loop.

- Nice-to-have: potion is extra fun but not required; the game is still playable without it.