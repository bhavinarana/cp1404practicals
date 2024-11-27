import wikipedia


def main():
    print("Wikipedia Search")
    user_input = input("\nEnter page title or search phrase (or press Enter to quit): ")

    while user_input:  # Continue while the user enters something
        try:
            # Try to get the page with autosuggest enabled
            page = wikipedia.page(user_input, autosuggest=True)
            print_page_details(page)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{user_input}" does not match any pages. Try another id!')
        except Exception as e:
            print(f"An error occurred: {e}")

        # Prompt for the next input
        user_input = input("\nEnter page title or search phrase (or press Enter to quit): ")

    print("Thank you.")


def print_page_details(page):
    """
    Print the title, summary, and URL of the Wikipedia page.
    """
    print(f"\n{page.title}")
    print(page.summary[:500] + "...")  # Show only the first 500 characters of the summary
    print(page.url)


if __name__ == "__main__":
    main()

