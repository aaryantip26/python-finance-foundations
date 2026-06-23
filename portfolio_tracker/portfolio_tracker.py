import csv

class PortfolioTracker:

    def __init__(self, filename):
        self.filename = filename
        self.holdings = []
        self.load_csv(filename)

    
    def load_csv(self, filename):
        with open(filename) as file:
            reader = csv.DictReader(file)
            
            expected = {"Name", "Symbol", "Quantity", "Price"}
            if set(reader.fieldnames) != expected:
                raise ValueError("""Invalid CSV Format.
                                 The fieldnames should be:
                                 {"Name", "Symbol", "Quantity", "Price"}""")

            for row in reader:
                try:
                    qty = int(row["Quantity"])
                    price = float(row["Price"])

                except ValueError:
                    print(f"Invalid numeric data in row {row}")

                else:
                    self.holdings.append({
                        "Name" : row["Name"],
                        "Symbol" : row["Symbol"],
                        "Quantity" : qty,
                        "Price" : price
                        })
    
    
    def total(self):    
        total = 0
        for row in self.holdings:
            total += row["Quantity"]*row["Price"]
        
        return total


    def weights(self):
        total = self.total()
        if total == 0:
            return self.holdings
        self.new_holdings = self.holdings.copy()
        for row in self.new_holdings:
            qty = row["Quantity"]
            price = row["Price"]

            weight = (qty*price) / total
            row["Weight"] = f"{weight:.2%}"
        
        return self.new_holdings

    
    def summary(self):
        rows = self.weights()
        with open(f"revised_{self.filename}", "w", newline = "") as file:
            fieldnames = ["Name","Symbol","Quantity","Price","Weight"]
            summary = csv.DictWriter(file,
                                     fieldnames = fieldnames)
            
        
            summary.writeheader()

            for row in rows:
                summary.writerow(row)
            
            summary.writerow({
                "Name": "TOTAL",
                "Price": f"${self.total():,.2f}"
                })


if __name__ == "__main__":
    try:
        tracker = PortfolioTracker(input("CSV: "))
        tracker.summary()
        print("Portfolio summary created")
    except FileNotFoundError:
        print("Oops! File not found.")
    except ValueError as e:
        print(e)


## Known limitations
# - Assumes well-formed numeric data for Quantity and Price (invalid rows are skipped with a warning, not auto-corrected)
