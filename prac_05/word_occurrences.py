"""
word_occurrences.py
A program to count the occurrences of words in a string and display them in a sorted and aligned format.

Estimated Time: 30 minutes
"""

# Function to count word occurrences in the input text
def count_word_occurrences(text):
    # Split the text into words
    words = text.split()
    # Create a dictionary to store word counts
    word_counts = {}

    # Count occurrences of each word
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# Get input text from the user
text = input("Text: ")

# Count the occurrences of words
word_counts = count_word_occurrences(text)

# Find the longest word to determine alignment width
max_word_length = max(len(word) for word in word_counts)

# Sort the word counts dictionary by word
for word in sorted(word_counts):
    # Use f-string formatting to align the output
    print(f"{word:{max_word_length}} : {word_counts[word]}")