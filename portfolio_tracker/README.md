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

## Example
### Input ('valid_portfolio.csv'):
  Name,Symbol,Quantity,Price
  Apple Inc,AAPL,10,200
  Microsoft Corp,MSFT,5,400
  NVIDIA Corp,NVDA,8,150
  Amazon.com Inc,AMZN,3,250

### Output ('revised_valid_portfolio.csv'):
  Name,Symbol,Quantity,Price,Weight
  Apple Inc,AAPL,10,200.0,33.61%
  Microsoft Corp,MSFT,5,400.0,33.61%
  NVIDIA Corp,NVDA,8,150.0,20.17%
  Amazon.com Inc,AMZN,3,250.0,12.61%
  TOTAL,,,"$5,950.00",

## Concepts demonstrated
- Object-oriented design (PortfolioTracker class)
- CSV reading/writing (csv.DictReader, csv.DictWriter)
- Input validation with try/except/else
- Defensive handling of malformed rows and zero-total portfolios
