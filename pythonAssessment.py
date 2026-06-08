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
- Longest and shortest words (EXTRA FEATURE 4)
- Export results to file (EXTRA FEATURE 5)
- Keyword density percentage (EXTRA FEATURE 6)
- Sentence average length (EXTRA FEATURE 7)
- Character count with/without spaces (EXTRA FEATURE 8)
- Character frequency analysis (EXTRA FEATURE 9)
- Sentiment word detection (EXTRA FEATURE 10)
- Calculate average word length
- Count paragraphs
- Count sentences

Developed as part of NLP text analysis coursework.
"""

import re
from datetime import datetime


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
    if not text:
        return "0 seconds"
    
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    total_words = len(words)
    
    if total_words == 0:
        return "0 seconds"
    
    minutes = total_words / wpm
    full_minutes = int(minutes)
    seconds = int((minutes - full_minutes) * 60)
    
    if full_minutes == 0:
        return f"{seconds} seconds"
    elif seconds == 0:
        return f"{full_minutes} minute{'s' if full_minutes != 1 else ''}"
    else:
        return f"{full_minutes} minute{'s' if full_minutes != 1 else ''} {seconds} seconds"
# =======================================================


# ==================== EXTRA FEATURE 4 ====================
def find_extreme_words(text):
    """
    EXTRA FEATURE: Finds the longest and shortest words in the text.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        tuple: (longest_word, shortest_word) or (None, None) if empty.
    """
    if not text:
        return None, None
    
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    
    if not words:
        return None, None
    
    unique_words = list(set(words))
    
    longest = max(unique_words, key=len)
    shortest = min(unique_words, key=len)
    
    return longest, shortest
# =======================================================


# ==================== EXTRA FEATURE 5 ====================
def export_analysis_to_file(text, filename="analysis_results.txt"):
    """
    EXTRA FEATURE: Exports full analysis results to a text file.
    
    Args:
        text (str): The article text to analyze.
        filename (str): Output filename. Default is "analysis_results.txt".
    
    Returns:
        bool: True if export successful, False otherwise.
    """
    try:
        most_common = identify_most_common_word(text)
        top_5 = get_top_5_words(text)
        unique_count = count_unique_words(text)
        total_words = len(re.findall(r"\b[a-zA-Z']+\b", text.lower()))
        reading_time = estimate_reading_time(text)
        longest, shortest = find_extreme_words(text)
        avg_length = calculate_average_word_length(text)
        paragraphs = count_paragraphs(text)
        sentences = count_sentences(text)
        avg_sentence_length = calculate_sentence_average_length(text)
        char_with_spaces, char_without_spaces = count_characters(text)
        top_chars = get_top_characters(text)
        sentiment = analyze_sentiment(text)
        
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append("NEWS ARTICLE ANALYSIS REPORT")
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 60)
        report_lines.append("")
        report_lines.append("[RUBRIC REQUIREMENTS]")
        report_lines.append(f"Most Common Word: '{most_common}'")
        report_lines.append(f"Average Word Length: {avg_length:.2f} characters")
        report_lines.append(f"Paragraph Count: {paragraphs}")
        report_lines.append(f"Sentence Count: {sentences}")
        report_lines.append("")
        report_lines.append("[EXTRA FEATURES]")
        report_lines.append("Top 5 Most Common Words:")
        if top_5:
            for rank, (word, count) in enumerate(top_5, 1):
                report_lines.append(f"    {rank}. '{word}' - {count} times")
        else:
            report_lines.append("    No words found.")
        report_lines.append("")
        report_lines.append(f"Unique Words: {unique_count}")
        report_lines.append(f"Total Words: {total_words}")
        report_lines.append(f"Vocabulary Diversity: {(unique_count/total_words)*100:.1f}%")
        report_lines.append("")
        report_lines.append(f"Reading Time Estimate: {reading_time}")
        report_lines.append("")
        report_lines.append(f"Longest Word: '{longest}' ({len(longest)} characters)")
        report_lines.append(f"Shortest Word: '{shortest}' ({len(shortest)} characters)")
        report_lines.append("")
        report_lines.append(f"Average Sentence Length: {avg_sentence_length:.2f} words")
        report_lines.append("")
        report_lines.append(f"Characters (with spaces): {char_with_spaces}")
        report_lines.append(f"Characters (without spaces): {char_without_spaces}")
        report_lines.append("")
        report_lines.append("Top 5 Most Frequent Characters:")
        if top_chars:
            for rank, (char, count) in enumerate(top_chars, 1):
                report_lines.append(f"    {rank}. '{char}' - {count} times")
        report_lines.append("")
        report_lines.append("[SENTIMENT ANALYSIS]")
        report_lines.append(f"Positive words found: {sentiment['positive_count']}")
        report_lines.append(f"Negative words found: {sentiment['negative_count']}")
        report_lines.append(f"Overall sentiment: {sentiment['overall']}")
        report_lines.append("")
        report_lines.append("=" * 60)
        report_lines.append("End of Report")
        report_lines.append("=" * 60)
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(report_lines))
        
        return True
        
    except Exception as e:
        print(f"Error exporting analysis: {e}")
        return False
# =======================================================


# ==================== EXTRA FEATURE 6 ====================
def calculate_keyword_density(text, word):
    """
    EXTRA FEATURE: Calculates the keyword density percentage.
    Shows what percentage of total words the searched word represents.
    
    Args:
        text (str): The string to analyze.
        word (str): The keyword to calculate density for.
    
    Returns:
        float: Keyword density as a percentage. Returns 0.0 if invalid.
    """
    if not text or not word:
        return 0.0
    
    keyword_count = count_specific_word(text, word)
    total_words = len(re.findall(r"\b[a-zA-Z']+\b", text.lower()))
    
    if total_words == 0:
        return 0.0
    
    density = (keyword_count / total_words) * 100
    
    return float(density)
# =======================================================


# ==================== EXTRA FEATURE 7 ====================
def calculate_sentence_average_length(text):
    """
    EXTRA FEATURE: Calculates the average number of words per sentence.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        float: Average words per sentence. Returns 0.0 if invalid.
    """
    if not text:
        return 0.0
    
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    total_words = len(words)
    
    sentence_count = count_sentences(text)
    
    if sentence_count <= 0:
        return 0.0
    
    average = total_words / sentence_count
    
    return float(average)
# =======================================================


# ==================== EXTRA FEATURE 8 ====================
def count_characters(text):
    """
    EXTRA FEATURE: Counts characters with and without spaces.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        tuple: (characters_with_spaces, characters_without_spaces)
               Returns (0, 0) if text is empty.
    """
    if not text:
        return 0, 0
    
    with_spaces = len(text)
    without_spaces = len(text.replace(" ", "").replace("\t", "").replace("\n", ""))
    
    return with_spaces, without_spaces
# =======================================================


# ==================== EXTRA FEATURE 9 ====================
def get_top_characters(text, top_n=5):
    """
    EXTRA FEATURE: Returns the top N most frequent alphabetic characters.
    
    Args:
        text (str): The string to analyze.
        top_n (int): Number of top characters to return. Default is 5.
    
    Returns:
        list: A list of tuples (character, count) for top N characters.
              Returns empty list if text is empty.
    """
    if not text:
        return []
    
    letters = re.findall(r'[a-zA-Z]', text.lower())
    
    if not letters:
        return []
    
    char_counts = {}
    for char in letters:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    sorted_chars = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_chars[:top_n]
# =======================================================


# ==================== EXTRA FEATURE 10 ====================
def analyze_sentiment(text):
    """
    EXTRA FEATURE: Basic sentiment analysis using positive/negative word lists.
    Scans text for sentiment keywords and returns a summary.
    
    Args:
        text (str): The string to analyze.
    
    Returns:
        dict: Dictionary with positive_count, negative_count, and overall sentiment.
    """
    # Edge case: empty string
    if not text:
        return {"positive_count": 0, "negative_count": 0, "overall": "Neutral"}
    
    # Simple word lists for demonstration
    positive_words = [
        "good", "great", "excellent", "amazing", "wonderful", "fantastic",
        "positive", "best", "love", "happy", "perfect", "outstanding",
        "superb", "brilliant", "impressive", "remarkable", "revolutionary",
        "innovative", "groundbreaking", "success", "benefit", "improve",
        "better", "easy", "accessible", "quality", "consistent", "excellent",
        "perfectly", "rich", "flavorful", "positive", "overwhelmingly",
        "praise", "eager", "leap", "forward", "enhancing", "golden"
    ]
    
    negative_words = [
        "bad", "terrible", "awful", "horrible", "worst", "hate",
        "negative", "poor", "difficult", "problem", "issue", "fail",
        "wrong", "error", "bug", "crash", "slow", "expensive",
        "hard", "complicated", "confusing", "disappointing", "sad",
        "angry", "frustrated", "concern", "worry", "risk", "danger"
    ]
    
    # Extract words from text
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    
    # Count sentiment words
    positive_count = 0
    negative_count = 0
    
    for word in words:
        if word in positive_words:
            positive_count += 1
        if word in negative_words:
            negative_count += 1
    
    # Determine overall sentiment
    if positive_count > negative_count:
        overall = "Positive"
    elif negative_count > positive_count:
        overall = "Negative"
    else:
        overall = "Neutral"
    
    return {
        "positive_count": positive_count,
        "negative_count": negative_count,
        "overall": overall
    }
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
    
    # EXTRA FEATURE 4: Longest and shortest words
    longest, shortest = find_extreme_words(text)
    print(f"\n[EXTRA 4] Word Extremes:")
    if longest and shortest:
        print(f"    Longest word: '{longest}' ({len(longest)} characters)")
        print(f"    Shortest word: '{shortest}' ({len(shortest)} characters)")
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
    
    # EXTRA FEATURE 7: Sentence average length
    sentence_avg = calculate_sentence_average_length(text)
    print(f"\n[EXTRA 7] Sentence Complexity:")
    print(f"    Average words per sentence: {sentence_avg:.2f}")
    
    # EXTRA FEATURE 8: Character count
    char_with, char_without = count_characters(text)
    print(f"\n[EXTRA 8] Character Count:")
    print(f"    Characters (with spaces): {char_with}")
    print(f"    Characters (without spaces): {char_without}")
    
    # EXTRA FEATURE 9: Character frequency
    top_chars = get_top_characters(text)
    print(f"\n[EXTRA 9] Character Frequency (Top 5 Letters):")
    if top_chars:
        for rank, (char, count) in enumerate(top_chars, 1):
            print(f"    {rank}. '{char.upper()}' - {count} times")
    else:
        print("    No characters found.")
    
    # EXTRA FEATURE 10: Sentiment analysis
    sentiment = analyze_sentiment(text)
    print(f"\n[EXTRA 10] Sentiment Analysis:")
    print(f"    Positive sentiment words: {sentiment['positive_count']}")
    print(f"    Negative sentiment words: {sentiment['negative_count']}")
    print(f"    Overall sentiment: {sentiment['overall']}")
    
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
        print("  3. Export analysis to file")
        print("  4. Check keyword density")
        print("  5. Run sentiment analysis")
        print("  6. Exit")
        print("-" * 50)
        
        choice = input("Enter your choice (1, 2, 3, 4, 5, or 6): ").strip()
        
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
            success = export_analysis_to_file(article_text)
            if success:
                print("\nAnalysis exported successfully to 'analysis_results.txt'!")
            else:
                print("\nFailed to export analysis. Please try again.")
        
        elif choice == "4":
            keyword = input("\nEnter the keyword to check density: ").strip()
            
            if keyword:
                density = calculate_keyword_density(article_text, keyword)
                count = count_specific_word(article_text, keyword)
                total = len(re.findall(r"\b[a-zA-Z']+\b", article_text.lower()))
                print(f"\nKeyword Density Analysis for '{keyword}':")
                print(f"    Appearances: {count} out of {total} total words")
                print(f"    Density: {density:.2f}%")
            else:
                print("\nNo keyword entered. Please try again.")
        
        elif choice == "5":
            sentiment = analyze_sentiment(article_text)
            print("\n" + "-" * 40)
            print("SENTIMENT ANALYSIS RESULTS")
            print("-" * 40)
            print(f"Positive words found: {sentiment['positive_count']}")
            print(f"Negative words found: {sentiment['negative_count']}")
            print(f"Overall article sentiment: {sentiment['overall']}")
            print("-" * 40)
            
        elif choice == "6":
            print("\nThank you for using News Article Analyzer. Goodbye!")
            keep_running = False
            
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()