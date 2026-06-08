"""
pythonAssessment.py
Text analysis tool for news articles.
Author: [Your Name]
Date: 2026-06-08
"""

def main():
    # Read the news article file
    with open("news_article.txt", "r", encoding="utf-8") as file:
        article_text = file.read()
    
    # Display confirmation that file was read
    print("News article loaded successfully!")
    print(f"Total characters: {len(article_text)}")
    print("-" * 50)

# Run the main function
if __name__ == "__main__":
    main()