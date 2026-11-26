"""Simple currency conversion for TravelBuddy trip budgets."""

# Fixed example rates relative to GBP (for demonstration only).
RATES_FROM_GBP = {
    "GBP": 1.0,
    "EUR": 1.17,
    "USD": 1.27,
}


def convert(amount, from_currency, to_currency):
    """Convert an amount between two supported currencies."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    try:
        in_gbp = amount / RATES_FROM_GBP[from_currency]
        return round(in_gbp * RATES_FROM_GBP[to_currency], 2)
    except KeyError as missing:
        raise ValueError(f"Unsupported currency: {missing.args[0]}") from None
