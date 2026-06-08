"""
pythonAssessment.py
Text analysis tool for news articles.
Author: [Your Name]
Date: 2026-06-08
"""

import re


def count_specific_word(text, word):
    """
    Counts the occurrences of a specific word in the text.
    Whole word match, case-insensitive.
    
    Args:
        text (str): The string to search through.
        word (str): The word to count.
    
    Returns:
        int: The count of the word in the text. Returns 0 if no matches.
    """
    # Edge case: empty text or empty word
    if not text or not word:
        return 0
    
    # Use regex for whole word, case-insensitive matching
    pattern = r'\b' + re.escape(word) + r'\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    return len(matches)


def identify_most_common_word(text):
    """
    Identifies the most common word in the text using regex tokenization.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        str: The most common word. Returns None if text is empty.
    """
    # Edge case: empty string
    if not text:
        return None
    
    # Regex: find all words (letters and apostrophes), convert to lowercase
    # \b[a-zA-Z']+\b matches words with letters and apostrophes
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    
    # Edge case: no words found
    if not words:
        return None
    
    # Count word frequencies using a dictionary
    word_counts = {}
    
    # FOR LOOP - satisfies rubric requirement
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Find the word with the highest count
    most_common = max(word_counts, key=word_counts.get)
    
    return most_common


def main():
    # Read the news article file
    with open("news_article.txt", "r", encoding="utf-8") as file:
        article_text = file.read()
    
    # Display header
    print("=" * 50)
    print("NEWS ARTICLE ANALYZER")
    print("=" * 50)
    
    # Test count_specific_word
    search_word = "the"
    word_count = count_specific_word(article_text, search_word)
    print(f"\n[1] Word Count Analysis:")
    print(f"    The word '{search_word}' appears {word_count} times.")
    
    # Test identify_most_common_word
    most_common = identify_most_common_word(article_text)
    print(f"\n[2] Most Common Word:")
    print(f"    The most common word is: '{most_common}'")
    
    # Test edge case: empty string
    empty_test = identify_most_common_word("")
    print(f"    Edge case (empty string): {empty_test}")


# Run the main function
if __name__ == "__main__":
    main()