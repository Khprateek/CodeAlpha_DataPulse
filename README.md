# 🛒 DataPulse — Flipkart E-Commerce Data Analytics
### CodeAlpha Data Science Internship | Task 1: Web Scraping & Data Cleaning

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Scraping-green?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-orange?style=flat-square)
![Selenium](https://img.shields.io/badge/Selenium-Browser%20Automation-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

## 📌 Project Overview

This project is part of the **CodeAlpha Data Science Internship**. It involves building an end-to-end data pipeline starting from raw web scraping of Flipkart's laptop listings to a clean, structured dataset ready for Exploratory Data Analysis (EDA), Visualization, and Sentiment Analysis.

> **Target Website:** [Flipkart.com](https://www.flipkart.com) — India's leading e-commerce platform  
> **Category Scraped:** Laptops  
> **Total Records Collected:** 300+ unique laptop listings

---

## 📁 Project Structure

```
CodeAlpha_DataPulse/
│
├── scraper.py                    # Web scraping script (Selenium + BeautifulSoup)
├── clean_data.py                 # Data cleaning and preprocessing script
│
├── data/
│   ├── flipkart_laptops.csv          # Raw scraped data (messy)
│   └── flipkart_laptops_cleaned.csv  # Final cleaned dataset
│
└── README.md                     # Project documentation
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python 3.8+` | Core programming language |
| `Selenium` | Browser automation to bypass JavaScript rendering |
| `BeautifulSoup4` | HTML parsing and data extraction |
| `Pandas` | Data manipulation and cleaning |
| `Regex (re)` | Pattern matching for text cleaning |
| `ChromeDriver` | Headless browser for Selenium |

---

## 🕷️ Task 1A — Web Scraping

### Why Selenium Instead of Requests?

Flipkart renders its product listings using **JavaScript**, which means a simple `requests.get()` returns an empty or incomplete HTML page. Selenium launches a real Chrome browser, waits for the page to fully load, and then passes the rendered HTML to BeautifulSoup for extraction.

### Data Collected Per Product

| Column | Description |
|--------|-------------|
| `Product Name` | Full product title as shown on Flipkart |
| `Selling Price` | Current discounted price |
| `Original Price` | MRP before discount |
| `Discount` | Percentage discount offered |
| `Rating` | Average customer rating (out of 5) |
| `Rating Count` | Total number of ratings and reviews |

### How to Run the Scraper

**Step 1 — Install dependencies**
```bash
pip install selenium webdriver-manager beautifulsoup4 pandas
```

**Step 2 — Run the scraper**
```bash
python scraper.py
```

**Step 3 — Output**
```
✅ Page 1 scraped — 24 products collected so far
✅ Page 2 scraped — 48 products collected so far
...
🎉 Done! 310 products saved to flipkart_laptops.csv
```

---

## 🧹 Task 1B — Data Cleaning

### Problems Found in Raw Data

After scraping, the raw CSV contained several issues that needed to be fixed before any analysis could be performed:

| Issue | Example (Raw) | Fix Applied |
|-------|--------------|-------------|
| Broken price encoding | `â,'44,990` | Extracted digits only → `44990` |
| Ratings and reviews merged in one column | `125 RatingsÂ &Â 11 Reviews` | Split into two separate numeric columns |
| No brand/company column | — | Extracted brand name from product title |
| Discount stored as text | `10% off` | Extracted number only → `10` |
| Duplicate product listings | Multiple identical rows | Removed using `drop_duplicates()` |
| Prices stored as strings | `"₹44,990"` | Converted to float for calculations |

### How to Run the Cleaning Script

```bash
python clean_data.py
```

### Sample — Before Cleaning

| Product Name | Selling Price | Discount | Rating Count |
|---|---|---|---|
| Acer TravelLite AMD Ryzen 5... | â,'44,990 | 10% off | 125 RatingsÂ &Â 11 Reviews |
| HP Victus Intel Core i5... | â,'72,990 | 10% off | 733 RatingsÂ &Â 50 Reviews |

### Sample — After Cleaning

| Brand | Product Name | Selling Price (INR) | Original Price (INR) | Discount (%) | Rating | Number of Ratings | Number of Reviews |
|---|---|---|---|---|---|---|---|
| Acer | Acer TravelLite AMD Ryzen 5... | 44990 | 50000 | 10 | 3.8 | 125 | 11 |
| HP | HP Victus Intel Core i5... | 72990 | 81201 | 10 | 4.3 | 733 | 50 |
| ASUS | ASUS Vivobook Go 15... | 38990 | 50990 | 23 | 4.3 | 1532 | 77 |

### Cleaning Steps (Summary)

```
1. Extract Brand Name   → from Product Name using keyword matching
2. Fix Price Encoding   → strip all non-numeric characters, convert to float
3. Split Rating Column  → separate "Number of Ratings" and "Number of Reviews"
4. Clean Discount       → extract integer from "10% off" → 10
5. Remove Duplicates    → based on Product Name
6. Drop Null Rows       → remove rows with missing Product Name
7. Reorder Columns      → logical order for analysis
8. Export Clean CSV     → flipkart_laptops_cleaned.csv
```

---

## 📊 Dataset Summary (After Cleaning)

| Metric | Value |
|--------|-------|
| Total Products | 300+ |
| Brands Covered | HP, Lenovo, ASUS, Acer, Dell, Samsung, MSI, Apple and more |
| Price Range | ₹14,990 — ₹2,00,000+ |
| Average Rating | ~4.1 / 5 |
| Columns | 8 |

---
## 👤 Author

**CodeAlpha Data Science Intern**  
🔗 GitHub: [Your GitHub Profile](https://github.com/Khprateek)  
🔗 LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/prateek-kharwar-a7764b270/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built as part of the CodeAlpha Data Science Internship Program*