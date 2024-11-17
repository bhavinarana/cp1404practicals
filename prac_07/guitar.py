class Guitar:
    """Represent a guitar with its name, year of manufacture, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Calculate the age of the guitar."""
        current_year = 2022  # Replace with dynamic year if needed
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, otherwise False."""
        return self.get_age() >= 50

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"