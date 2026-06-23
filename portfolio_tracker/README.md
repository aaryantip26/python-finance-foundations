# Portfolio Tracker

A class-based CLI tool that loads portfolio holdings from a CSV file,
calculates position weights, and exports a summary CSV with a total row.

## Usage
- "python portfolio_tracker.py" in the terminal
- Enter the CSV filename when prompted.

## Input format
CSV must contain these columns (any order): Name, Symbol, Quantity, Price

## Output
Generates `revised_<input_filename>.csv` with an added Weight column
and a TOTAL row.

## Concepts demonstrated
- Object-oriented design (PortfolioTracker class)
- CSV reading/writing (csv.DictReader, csv.DictWriter)
- Input validation with try/except/else
- Defensive handling of malformed rows and zero-total portfolios
