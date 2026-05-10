# Stats-ketball

A desktop app for tracking and reviewing your basketball game statistics. Built with Python and Tkinter.

## Features

- **Enter Stats** — Log points, rebounds, and assists for each game, saved to a CSV file
- **Load Existing File** — Append new stats to a previously created CSV file
- **View Stats** — Load a CSV file and see your averaged points, rebounds, and assists across all logged games

## Requirements

- Python 3.x (Tkinter is included in the standard library)

## Usage

```bash
python main.py
```

From the landing screen you can:

1. **Enter Stats** — Fill in points, rebounds, and assists, then click **Save Stats**. By default stats are written to `stats.csv`. Use **Load Existing File** to append to a different file.
2. **View Stats** — Click **Load File**, select a CSV, and see your per-game averages.

## Data Format

Stats are stored as plain CSV files with the following columns:

```
Points,Rebounds,Assists
```

Each row represents one game.
