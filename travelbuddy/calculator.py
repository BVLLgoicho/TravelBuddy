"""Core trip calculations for TravelBuddy."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def total_trip_cost(*costs):
    """Return the total cost of a trip from any number of individual costs."""
    for cost in costs:
        if cost < 0:
            raise ValueError("Costs cannot be negative")
    return round(sum(costs), 2)


def split_cost(total, people):
    """Split a total cost evenly between a number of travellers."""
    if people <= 0:
        raise ValueError("There must be at least one traveller")
    return round(total / people, 2)
