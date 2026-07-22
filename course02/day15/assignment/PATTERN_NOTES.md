# Patterns I see

## Hypothesis

A: fight and heal wins most, because fight is the only command that can hit the dragon, heal is the only command that heal the player

## Actual data

- Total fights: 21 | Player wins: 10 | Boss wins: 11 (48% win rate)
- Command totals: fight 107, heal 61, defend 7 → **fight is used most**
- When player wins: avg fights=6.1, heals=5.7, defends=0.7, rounds=12.5
- When boss wins: avg fights=4.2, heals=0.4, defends=0.0, rounds=4.5

## Pattern (matched or broke?)

Hypothesis **matched**: winning fights need both **fight** and **heal**.

- Fight is still the most-used command (107), and it is the only way to damage the dragon.
- But wins also use many heals (avg 5.7), while losses barely heal (avg 0.4) and end fast (4.5 rounds).
- So fight hits the dragon; heal keeps you alive long enough to finish.

