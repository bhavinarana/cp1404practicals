from programming_language import ProgrammingLanguage

def main():
    """Create programming language objects and display dynamically typed languages."""
    # Create ProgrammingLanguage instances
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    
    # Test the __str__ method by printing each object
    print(python)
    print(ruby)
    print(visual_basic)
    
    # List of languages
    languages = [python, ruby, visual_basic]
    
    # Print names of all languages with dynamic typing
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()
