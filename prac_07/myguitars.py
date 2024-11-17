class Guitar:
    """Represent a guitar with a name, year, and cost."""

    def __init__(self, name, year, cost):
        """Initialize a Guitar with a name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}), worth ${self.cost:.2f}"

    def __lt__(self, other):
        """Less-than comparison to sort Guitars by year."""
        return self.year < other.year


def main():
    """Main program to read, display, and sort guitars."""
    guitars = read_guitars()
    print("Unsorted Guitars:")
    display_guitars(guitars)

    # Sort guitars by year (using __lt__)
    guitars.sort()
    print("\nGuitars Sorted by Year:")
    display_guitars(guitars)


def read_guitars():
    """Read guitar data and return a list of Guitar objects."""
    guitars = [
        Guitar("Gibson L-5 CES", 1922, 16035.40),
        Guitar("Fender Stratocaster", 1954, 1234.56),
        Guitar("Yamaha FG700S", 2006, 489.99),
        Guitar("Martin D-28", 1931, 7000.00),
        Guitar("Gibson Les Paul", 1952, 1500.00)
    ]
    return guitars


def display_guitars(guitars):
    """Display each guitar in the list."""
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
