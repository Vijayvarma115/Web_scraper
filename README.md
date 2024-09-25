# Mobile Data Scraper using BeautifulSoup

This project extracts mobile data from Flipkart's website and stores it in a CSV file. The data includes the mobile titles, ratings, reviews, and prices, which are scraped using the BeautifulSoup library in Python.

## Table of Contents

1. [Project Description]
2. [Technologies Used]
3. [Setup Instructions]
4. [How to Use]
5. [Output]

## Project Description

This Python script scrapes data from the Flipkart website, specifically looking for mobile phones. It captures the following details:
- Mobile Titles
- Ratings
- Reviews
- Prices

The scraped data is then stored in a CSV file named `mobilesinfo.csv`.

## Technologies Used

- Python 3.x
- BeautifulSoup4
- Requests
- Pandas

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Vijayvarma115/Web_scraper.git
   cd Web_scraper
   ```

2. **Install the Required Libraries:**

   Ensure you have Python installed, then run:

   ```bash
   pip install requests beautifulsoup4 pandas
   ```

3. **Update the Flipkart URL (if necessary):**

   In case Flipkart changes its HTML structure or classes, you may need to update the `class_` values in the `soup.find_all` statements.

## How to Use

1. **Run the Script:**

   You can run the script using the command:

   ```bash
   python scraper.py
   ```

2. **Check the CSV Output:**

   After running the script, a file called `mobilesinfo.csv` will be generated in the same directory. This file contains the scraped data in a structured format.

## Output

Once you run the script, a CSV file with the following structure will be created:

| Mobile Title        | Mobile Rating | Mobile Reviews | Mobile Price |
|---------------------|---------------|----------------|--------------|
| Moto G55 mobile  | 4.5           | 1200 Reviews   | ₹15,999      |
