#Project 1

def compound_interest():
    """Given the accurate periodic interest rate, this simple calculator will
    return the Future Value of an interest-gaining investment/loan"""
    P = float(input("Principal/Face Value: "))
    i = float(input("Periodic Interest Rate (%): "))
    n = float(input("Number of periods: "))
    F = P * ((1 + (i / 100)) ** n)
    print(f"Future Value: {F:.2f}")

if __name__ == "__main__":
    compound_interest()
