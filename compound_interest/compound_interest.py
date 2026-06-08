def compound_interest():
    """Calculates the future value of an investment using compound interest.

Parameters
----------
None (reads from stdin)

Formula: F = P * (1 + i/100) ** n"""
    
    P = float(input("Principal/Face Value: "))
    if P <= 0:
        print("Error: principal must be positive.")
        return
        
    r = float(input("Periodic Interest Rate (%): "))
    if r <= -100:
        print("Error: interest rate cannot be -100% or lower")
        return
        
    n = float(input("Number of periods: "))
    if n <= 0:
        print("Error: periods must be positive.")
        return
    
    return P * ((1 + (r / 100)) ** n)

if __name__ == "__main__":
    result = compound_interest()
    if result is not None:
        print(f"Future Value: {result:.2f}")

# Negative rates are permitted (e.g. negative-yield environments);
# only rates <= -100% are mathematically invalid.
# Known limitations / future improvements:
# - No input validation for non-numeric entries (letters will crash the program)
# - Could add support for continuous compounding (F = P * e^(rt))
# - Could extend to annuity calculations
