class ProgrammingLanguage:
    """Represent a programming language with specific attributes."""

    def __init__(self, name, typing, reflection, year):
        """Initialize the programming language instance with name, typing, reflection, and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, otherwise False."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
