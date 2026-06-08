"""
pythonAssessment.py
Text analysis tool for news articles.
Author: [Your Name]
Date: 2026-06-08

This script performs various text analysis tasks on a given news article:
- Count specific word occurrences
- Identify the most common word
- Display top 5 most common words (EXTRA FEATURE)
- Calculate average word length
- Count paragraphs
- Count sentences

Developed as part of NLP text analysis coursework.
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
    
    # Find the word with the highest count using max()
    most_common = max(word_counts, key=word_counts.get)
    
    return most_common


# ==================== EXTRA FEATURE 1 ====================
def get_top_5_words(text):
    """
    EXTRA FEATURE: Returns the top 5 most common words with their counts.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        list: A list of tuples (word, count) for top 5 words.
              Returns empty list if text is empty.
    """
    # Edge case: empty string
    if not text:
        return []
    
    # Regex: extract words, lowercase
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    
    # Edge case: no words found
    if not words:
        return []
    
    # Count frequencies
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Sort by count (highest first), then alphabetically
    # sorted() returns a list of tuples sorted by the key
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Return top 5 (or fewer if less than 5 unique words)
    return sorted_words[:5]
# =======================================================


def calculate_average_word_length(text):
    """
    Calculates the average length of words in the text.
    Excludes punctuation marks and special characters.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        float: The average word length. Returns 0 if text is empty.
    """
    # Edge case: empty string
    if not text:
        return 0
    
    # Regex: extract only words (letters and apostrophes), strip punctuation
    words = re.findall(r"\b[a-zA-Z']+\b", text)
    
    # Edge case: no words found
    if not words:
        return 0
    
    # Calculate total length of all words
    total_length = 0
    for word in words:
        total_length += len(word)
    
    # Calculate average
    average = total_length / len(words)
    
    return float(average)


def count_paragraphs(text):
    """
    Counts the number of paragraphs in the text.
    Paragraphs are defined as blocks of text separated by empty lines.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        int: The number of paragraphs. Returns 1 if text is empty.
    """
    # Edge case: empty string
    if not text:
        return 1
    
    # Split text by blank lines
    paragraphs = re.split(r'\n\s*\n', text.strip())
    
    # Filter out any empty strings from the list
    valid_paragraphs = []
    for p in paragraphs:
        if p.strip():
            valid_paragraphs.append(p)
    
    # Edge case: if no valid paragraphs found, return 1
    if not valid_paragraphs:
        return 1
    
    return len(valid_paragraphs)


def count_sentences(text):
    """
    Counts the number of sentences in the text.
    Sentences end with periods, exclamation marks, or question marks.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        int: The number of sentences. Returns 1 if text is empty.
    """
    # Edge case: empty string
    if not text:
        return 1
    
    # Regex: count sentence-ending punctuation marks
    sentences = re.findall(r'[.!?]', text)
    
    # Edge case: if no sentence endings found, return 1
    if not sentences:
        return 1
    
    return len(sentences)


def display_full_analysis(text):
    """
    Displays complete analysis of the news article.
    Includes EXTRA FEATURE: Top 5 most common words.
    
    Args:
        text (str): The article text to analyze.
    """
    print("\n" + "=" * 50)
    print("FULL ARTICLE ANALYSIS")
    print("=" * 50)
    
    # Most common word (rubric requirement)
    most_common = identify_most_common_word(text)
    print(f"\n[1] Most Common Word: '{most_common}'")
    
    # EXTRA FEATURE: Top 5 most common words
    print("\n[EXTRA] Top 5 Most Common Words:")
    top_5 = get_top_5_words(text)
    if top_5:
        for rank, (word, count) in enumerate(top_5, 1):
            print(f"    {rank}. '{word}' - {count} times")
    else:
        print("    No words found.")
    
    # Average word length
    avg_length = calculate_average_word_length(text)
    print(f"\n[2] Average Word Length: {avg_length:.2f} characters")
    
    # Paragraph count
    paragraphs = count_paragraphs(text)
    print(f"[3] Paragraph Count: {paragraphs}")
    
    # Sentence count
    sentences = count_sentences(text)
    print(f"[4] Sentence Count: {sentences}")
    
    print("\n" + "=" * 50)


def main():
    """
    Main function that drives the program.
    Includes WHILE LOOP and IF/ELSE for interactive menu.
    """
    # Read the news article file into a string variable
    try:
        with open("news_article.txt", "r", encoding="utf-8") as file:
            article_text = file.read()
    except FileNotFoundError:
        print("Error: news_article.txt not found!")
        print("Please ensure the news article file is in the same directory.")
        return
    
    # Display welcome message
    print("=" * 50)
    print("NEWS ARTICLE ANALYZER")
    print("=" * 50)
    print("Welcome! This tool analyzes news articles using NLP techniques.")
    
    # WHILE LOOP - allows user to perform multiple searches
    keep_running = True
    while keep_running:
        print("\n" + "-" * 50)
        print("MENU OPTIONS:")
        print("  1. Search for a specific word")
        print("  2. View full article analysis")
        print("  3. Exit")
        print("-" * 50)
        
        # Get user input
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        # IF/ELSE - handles user menu choice
        if choice == "1":
            # Word count feature
            search_word = input("\nEnter the word you want to count: ").strip()
            
            if search_word:
                word_count = count_specific_word(article_text, search_word)
                print(f"\nThe word '{search_word}' appears {word_count} times.")
            else:
                print("\nNo word entered. Please try again.")
                
        elif choice == "2":
            # Full analysis feature (now includes top 5 words)
            display_full_analysis(article_text)
            
        elif choice == "3":
            # Exit program
            print("\nThank you for using News Article Analyzer. Goodbye!")
            keep_running = False
            
        else:
            # Invalid input handling
            print("\nInvalid choice. Please enter 1, 2, or 3.")


# Entry point of the program
if __name__ == "__main__":
    main()