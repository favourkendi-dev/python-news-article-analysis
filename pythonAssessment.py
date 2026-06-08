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
    # \b ensures we match word boundaries (not parts of other words)
    pattern = r'\b' + re.escape(word) + r'\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    return len(matches)


def main():
    # Read the news article file
    with open("news_article.txt", "r", encoding="utf-8") as file:
        article_text = file.read()
    
    # Display confirmation that file was read
    print("=" * 50)
    print("NEWS ARTICLE ANALYZER")
    print("=" * 50)
    
    # Test count_specific_word
    search_word = "the"
    word_count = count_specific_word(article_text, search_word)
    print(f"\nWord Count Analysis:")
    print(f"The word '{search_word}' appears {word_count} times.")
    
    # Test with another word
    search_word_2 = "machine"
    word_count_2 = count_specific_word(article_text, search_word_2)
    print(f"The word '{search_word_2}' appears {word_count_2} times.")
    
    # Test edge case: word that doesn't exist
    search_word_3 = "xyz123"
    word_count_3 = count_specific_word(article_text, search_word_3)
    print(f"The word '{search_word_3}' appears {word_count_3} times.")


# Run the main function
if __name__ == "__main__":
    main()