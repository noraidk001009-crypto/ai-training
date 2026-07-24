# war with dragon — Game Analyst Capstone

Turn-based text RPG: fight a village-eating Dragon, log every battle to CSV, then analyze what actually wins.

## Run the game

Code lives in Day 16 (latest Capstone build):

```
cd ../day16
python main.py
```

Commands in-game: `fight` / `defend` / `heal` / `quit`  
Each finished fight appends a row to `fights.csv`.

## Run the analysis

From the same folder (`day16/`):

```
python summarize.py
python make_chart.py
```

- `summarize.py` — win rate, command totals, win vs loss averages  
- `make_chart.py` — bar chart saved as `capstone_chart.png`

## Chart

![Commands in capstone fights](./capstone_chart.png)

Across **21** fights: player wins **10**, boss wins **11** (win rate **48%**).  
Command totals: fight **107**, heal **61**, defend **7**.

## Key insight

Winning needs **fight + heal**: wins average **6.1** fights and **5.7** heals; losses average **4.2** fights and **0.4** heals and die fast (~4.5 rounds).

**Defend is almost unused** (only 7 uses). The few fights that used defend all won, but the sample is tiny. Recommendation: buff defend slightly (`raw // 2` → `raw // 3`) so players have a safer mid-fight option without replacing heal.

Full write-up: `../day16/assignment/REPORT.md`

## AI help (honest)

- **I wrote / decided:** game title & boss theme, analyst questions (Day 13), playtest fights logged to CSV, pattern notes, report findings and the defend-buff recommendation.
- **AI helped with:** debugging CSV column bugs, `summarize.py` / `make_chart.py` structure, and polishing report / README wording.
- **This README:** drafted with Cursor AI from the Day 17 template, using my Day 16 `REPORT.md` numbers — I checked that the insight and run steps match my real project.
