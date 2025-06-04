# 🏏 Live Cricket Score Extractor using Selenium

A Python-based automation tool that leverages Selenium to extract real-time cricket match scores from a live sports website and stores the data in an Excel file. This script is designed for seamless data collection and reporting.

## 📘 Project Overview

This project automates the process of collecting live cricket match data using the **Selenium WebDriver**. It navigates to a live scores page, scrapes structured information about ongoing matches, and exports the results into an Excel spreadsheet (`livescore.xlsx`) using **Pandas**.

## ✅ Key Highlights

- Fully automated browser interaction using Selenium.
- Captures live match details: team names, scores, and match status.
- Data structured and exported in Excel format for further analysis/reporting.
- No manual effort required post execution.

## 🛠️ Technologies & Libraries

| Technology     | Description                        |
|----------------|------------------------------------|
| Python 3       | Core programming language          |
| Selenium       | Web automation and scraping        |
| WebDriverManager | Automatic ChromeDriver handling |
| Pandas         | Data manipulation & Excel export   |
| OpenPyXL       | Excel file handling via Pandas     |


## 🖥️ How to Run

### 1. Clone the Repository

git clone https://github.com/Saranya-Ravindran/WS-Task6.git
cd WS-Task6

2. Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available, install manually:
pip install selenium pandas openpyxl webdriver-manager

3. Execute the Script
python livescore_scraper.py

On execution, a browser window will open.

The script will fetch current live match data.

An Excel file (livescore.xlsx) will be saved in the project directory.

📂 Output Format
The generated Excel file contains the following columns:

Match Title	Match Status	Team 1	Score 1	Team 2	Score 2

Each row represents one ongoing or completed match.
