"""
pythonAssessment.py
Text analysis tool for news articles.
Author: [Your Name]
Date: 2026-06-08

This script performs various text analysis tasks on a given news article:
- Count specific word occurrences
- Identify the most common word
- Display top 5 most common words (EXTRA FEATURE 1)
- Unique word count (EXTRA FEATURE 2)
- Reading time estimate (EXTRA FEATURE 3)
- Calculate average word length
- Count paragraphs
- Count sentences

Developed as part of NLP text analysis coursework.
"""

import re
import math


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
    if not text or not word:
        return 0
    
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
    if not text:
        return None
    
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    
    if not words:
        return None
    
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
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
    if not text:
        return []
    
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    
    if not words:
        return []
    
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_words[:5]
# =======================================================


# ==================== EXTRA FEATURE 2 ====================
def count_unique_words(text):
    """
    EXTRA FEATURE: Counts the number of unique (distinct) words in the text.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        int: The number of unique words. Returns 0 if text is empty.
    """
    if not text:
        return 0
    
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    
    if not words:
        return 0
    
    unique_words = set(words)
    
    return len(unique_words)
# =======================================================


# ==================== EXTRA FEATURE 3 ====================
def estimate_reading_time(text, wpm=200):
    """
    EXTRA FEATURE: Estimates reading time based on word count.
    Average adult reading speed: 200-250 WPM.
    
    Args:
        text (str): The string to analyze.
        wpm (int): Words per minute reading speed. Default is 200.
    
    Returns:
        str: Formatted reading time (e.g., "2 minutes 30 seconds").
             Returns "0 seconds" if text is empty.
    """
    # Edge case: empty string
    if not text:
        return "0 seconds"
    
    # Count total words
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    total_words = len(words)
    
    # Edge case: no words found
    if total_words == 0:
        return "0 seconds"
    
    # Calculate time in minutes
    minutes = total_words / wpm
    
    # Convert to minutes and seconds for display
    full_minutes = int(minutes)
    seconds = int((minutes - full_minutes) * 60)
    
    # Format output string
    if full_minutes == 0:
        return f"{seconds} seconds"
    elif seconds == 0:
        return f"{full_minutes} minute{'s' if full_minutes != 1 else ''}"
    else:
        return f"{full_minutes} minute{'s' if full_minutes != 1 else ''} {seconds} seconds"
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
    if not text:
        return 0
    
    words = re.findall(r"\b[a-zA-Z']+\b", text)
    
    if not words:
        return 0
    
    total_length = 0
    for word in words:
        total_length += len(word)
    
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
    if not text:
        return 1
    
    paragraphs = re.split(r'\n\s*\n', text.strip())
    
    valid_paragraphs = []
    for p in paragraphs:
        if p.strip():
            valid_paragraphs.append(p)
    
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
    if not text:
        return 1
    
    sentences = re.findall(r'[.!?]', text)
    
    if not sentences:
        return 1
    
    return len(sentences)


def display_full_analysis(text):
    """
    Displays complete analysis of the news article.
    Includes EXTRA FEATURES.
    
    Args:
        text (str): The article text to analyze.
    """
    print("\n" + "=" * 50)
    print("FULL ARTICLE ANALYSIS")
    print("=" * 50)
    
    # Most common word (rubric requirement)
    most_common = identify_most_common_word(text)
    print(f"\n[1] Most Common Word: '{most_common}'")
    
    # EXTRA FEATURE 1: Top 5 most common words
    print("\n[EXTRA 1] Top 5 Most Common Words:")
    top_5 = get_top_5_words(text)
    if top_5:
        for rank, (word, count) in enumerate(top_5, 1):
            print(f"    {rank}. '{word}' - {count} times")
    else:
        print("    No words found.")
    
    # EXTRA FEATURE 2: Unique word count
    unique_count = count_unique_words(text)
    total_words = len(re.findall(r"\b[a-zA-Z']+\b", text.lower()))
    print(f"\n[EXTRA 2] Vocabulary Richness:")
    print(f"    Unique words: {unique_count}")
    print(f"    Total words: {total_words}")
    print(f"    Vocabulary diversity: {(unique_count/total_words)*100:.1f}%")
    
    # EXTRA FEATURE 3: Reading time estimate
    reading_time = estimate_reading_time(text)
    print(f"\n[EXTRA 3] Reading Time Estimate:")
    print(f"    Estimated reading time: {reading_time}")
    print(f"    (Based on 200 words per minute average)")
    
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
    try:
        with open("news_article.txt", "r", encoding="utf-8") as file:
            article_text = file.read()
    except FileNotFoundError:
        print("Error: news_article.txt not found!")
        print("Please ensure the news article file is in the same directory.")
        return
    
    print("=" * 50)
    print("NEWS ARTICLE ANALYZER")
    print("=" * 50)
    print("Welcome! This tool analyzes news articles using NLP techniques.")
    
    keep_running = True
    while keep_running:
        print("\n" + "-" * 50)
        print("MENU OPTIONS:")
        print("  1. Search for a specific word")
        print("  2. View full article analysis")
        print("  3. Exit")
        print("-" * 50)
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            search_word = input("\nEnter the word you want to count: ").strip()
            
            if search_word:
                word_count = count_specific_word(article_text, search_word)
                print(f"\nThe word '{search_word}' appears {word_count} times.")
            else:
                print("\nNo word entered. Please try again.")
                
        elif choice == "2":
            display_full_analysis(article_text)
            
        elif choice == "3":
            print("\nThank you for using News Article Analyzer. Goodbye!")
            keep_running = False
            
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()