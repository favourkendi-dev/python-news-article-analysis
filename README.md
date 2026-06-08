# News Article Analyzer

&gt; A Python-based Natural Language Processing (NLP) tool for comprehensive text analysis of news articles. Built as a portfolio-grade project for academic assessment

---

## Overview

This project analyzes news article text to extract valuable linguistic insights using Python. It was developed as a summative lab assignment for a Natural Language Processing course, demonstrating core text analysis techniques including word frequency analysis, sentence/paragraph segmentation, readability metrics, and sentiment detection.

**Key Highlights:**
-  Passes all 8 CodeGrade autograder criteria (100/100)
-  10 bonus features beyond rubric requirements
-  Clean, documented, production-ready Python code
-  Version controlled with Git

---

##  Features

### Rubric Requirements (Core)
| Feature | Function | Status |
|---------|----------|--------|
| Specific Word Count | `count_specific_word(text, word)` | 
| Most Common Word | `identify_most_common_word(text)` | 
| Average Word Length | `calculate_average_word_length(text)` | 
| Paragraph Count | `count_paragraphs(text)` | 
| Sentence Count | `count_sentences(text)` | 
| While Loop | Interactive menu system |
| For Loop | Word frequency iteration | 
| If/Else | Menu logic & edge cases | 

### Bonus Features (Extra)
| # | Feature | Function |

| 1 | Top 5 Most Common Words | `get_top_5_words(text)` |
| 2 | Unique Word Count | `count_unique_words(text)` |
| 3 | Reading Time Estimate | `estimate_reading_time(text, wpm)` |
| 4 | Longest & Shortest Words | `find_extreme_words(text)` |
| 5 | Export to File | `export_analysis_to_file(text)` |
| 6 | Keyword Density % | `calculate_keyword_density(text, word)` |
| 7 | Sentence Average Length | `calculate_sentence_average_length(text)` |
| 8 | Character Count | `count_characters(text)` |
| 9 | Character Frequency | `get_top_characters(text)` |
| 10 | Sentiment Analysis | `analyze_sentiment(text)` |

---

##  Tech Stack

- **Language:** Python 3.8+
- **Standard Library:** `re` (regex), `datetime`
- **No external dependencies** — runs with pure Python

---

##  Getting Started

### Prerequisites
- Python 3.8 or higher installed
- A news article text file (`news_article.txt`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/favourkendi-dev/python-news-article-analysis.git
   cd python-news-article-analysis