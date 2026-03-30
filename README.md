# 🛒 DataPulse — Flipkart E-Commerce Data Analytics
### CodeAlpha Data Science Internship | All Tasks Completed

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Scraping-green?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-orange?style=flat-square)
![Selenium](https://img.shields.io/badge/Selenium-Browser%20Automation-red?style=flat-square)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-9cf?style=flat-square)
![VADER](https://img.shields.io/badge/VADER-Sentiment%20NLP-purple?style=flat-square)
![TextBlob](https://img.shields.io/badge/TextBlob-NLP-blueviolet?style=flat-square)
![Status](https://img.shields.io/badge/Status-All%20Tasks%20Completed-brightgreen?style=flat-square)

---

## 📌 Project Overview

This project is part of the **CodeAlpha Data Science Internship**. It covers a complete end-to-end data science pipeline — from raw web scraping of Flipkart's laptop listings, through data cleaning and EDA, to advanced data visualization and NLP-based sentiment analysis.

> **Target Website:** [Flipkart.com](https://www.flipkart.com) — India's leading e-commerce platform
> **Category Scraped:** Laptops
> **Total Records Collected:** 700+ unique laptop listings

---

## 📁 Project Structure

```
CodeAlpha_DataPulse/
│
├── scraper.py                            # Task 1A — Web scraping (Selenium + BS4)
├── clean_data.py                         # Task 1B — Data cleaning & preprocessing
├── Task2_EDA_Flipkart_Laptops.ipynb      # Task 2  — Exploratory Data Analysis
├── Task3_Task4_Flipkart_Laptops.ipynb    # Task 3 & 4 — Visualization + Sentiment Analysis
│
├── data/
│   ├── flipkart_laptops.csv              # Raw scraped data (messy)
│   └── flipkart_laptops_cleaned.csv      # Final cleaned dataset
│
├── images/
│   ├── viz1_executive_dashboard.png
│   ├── viz2_brand_battle.png
│   ├── viz3_bubble_chart.png
│   ├── viz4_correlation_heatmap.png
│   ├── viz5_price_boxplot.png
│   ├── viz6_best_value.png
│   ├── viz7_sentiment_distribution.png
│   ├── viz8_vader_by_brand.png
│   ├── viz9_sentiment_vs_rating.png
│   ├── viz10_vader_vs_textblob_scatter.png
│   ├── viz11_wordcloud_positive.png
│   └── viz12_subjectivity_vs_polarity.png
│
└── README.md                             # Project documentation
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python 3.8+` | Core programming language |
| `Selenium` | Browser automation to bypass JS rendering |
| `BeautifulSoup4` | HTML parsing and data extraction |
| `Pandas` | Data manipulation and cleaning |
| `NumPy` | Numerical operations |
| `Regex (re)` | Pattern matching for text cleaning |
| `Matplotlib` | Core plotting library |
| `Seaborn` | Statistical data visualization |
| `WordCloud` | Word cloud generation |
| `VADER Sentiment` | Rule-based NLP sentiment scoring |
| `TextBlob` | ML-based polarity & subjectivity analysis |
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

```bash
# Step 1 — Install dependencies
pip install selenium webdriver-manager beautifulsoup4 pandas

# Step 2 — Run the scraper
python scraper.py
```

**Expected Output:**
```
✅ Page 1 scraped — 24 products collected so far
✅ Page 2 scraped — 48 products collected so far
...
🎉 Done! 700+ products saved to flipkart_laptops.csv
```

---

## 🧹 Task 1B — Data Cleaning

### Problems Found in Raw Data

| Issue | Example (Raw) | Fix Applied |
|-------|--------------|-------------|
| Broken price encoding | `â,'44,990` | Extracted digits only → `44990` |
| Ratings and reviews merged | `125 RatingsÂ &Â 11 Reviews` | Split into two numeric columns |
| No brand/company column | — | Extracted brand name from product title |
| Discount stored as text | `10% off` | Extracted number only → `10` |
| Duplicate product listings | Multiple identical rows | Removed via `drop_duplicates()` |
| Prices stored as strings | `"₹44,990"` | Converted to float |

### How to Run the Cleaning Script

```bash
python clean_data.py
```

### Sample — Before vs After Cleaning

**Before:**

| Product Name | Selling Price | Discount | Rating Count |
|---|---|---|---|
| Acer TravelLite AMD Ryzen 5... | â,'44,990 | 10% off | 125 RatingsÂ &Â 11 Reviews |
| HP Victus Intel Core i5... | â,'72,990 | 10% off | 733 RatingsÂ &Â 50 Reviews |

**After:**

| Brand | Product Name | Selling Price (INR) | Original Price (INR) | Discount (%) | Rating | Number of Ratings | Number of Reviews |
|---|---|---|---|---|---|---|---|
| Acer | Acer TravelLite AMD Ryzen 5... | 44990 | 50000 | 10 | 3.8 | 125 | 11 |
| HP | HP Victus Intel Core i5... | 72990 | 81201 | 10 | 4.3 | 733 | 50 |
| ASUS | ASUS Vivobook Go 15... | 38990 | 50990 | 23 | 4.3 | 1532 | 77 |

### Cleaning Steps Summary

```
1. Extract Brand Name   → from Product Name using keyword matching
2. Fix Price Encoding   → strip non-numeric chars, convert to float
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
| Total Products | 700+ |
| Brands Covered | HP, Lenovo, ASUS, Acer, Dell, Samsung, MSI, Apple and more |
| Price Range | ₹14,990 — ₹2,00,000+ |
| Average Rating | ~4.1 / 5 |
| Columns | 8 |

---

## 🔍 Task 2 — Exploratory Data Analysis (EDA)

Performed a thorough EDA on the cleaned dataset to uncover patterns and insights before visualization.

### Key EDA Steps

- **Descriptive Statistics** — mean, median, std, quartiles across all numeric columns
- **Missing Value Analysis** — identified and handled nulls in Rating, Price, and Review columns
- **Brand-wise Distribution** — product count and market share per brand
- **Price Distribution** — histogram + KDE plot of selling prices; identified skew towards mid-range
- **Discount Analysis** — distribution of discounts; brands offering the highest average discounts
- **Rating Distribution** — most products cluster between 3.8 and 4.5 stars
- **Correlation Analysis** — explored relationships between price, discount, rating, and review count
- **Price Segmentation** — categorized products into Budget / Mid-Range / Premium / Ultra Premium

### Key EDA Insights

- **HP and Lenovo** dominate the listing count with the most diverse portfolios
- **Higher priced laptops do not always guarantee higher ratings** — a weak positive correlation was observed
- **Discount % has no strong correlation with ratings**, suggesting discounts are marketing-driven
- **Number of Ratings and Number of Reviews are highly correlated** (as expected)
- **Budget segment (<₹30K)** has limited options but includes some highly rated value picks

---

## 🎨 Task 3 — Data Visualization

Six compelling visualizations were created to tell the complete story of the Flipkart laptop market.

### Visualization 1 — Executive Dashboard (Multi-Panel Overview)
A multi-panel overview with KPI cards showing total products, brand count, average price, average rating, average discount, and total reviews — plus five sub-charts covering brand distribution, price segment share, discount histogram, rating distribution, and top brands by review volume.

### Visualization 2 — Brand Battle: Price, Discount & Rating Heatmap
Three side-by-side horizontal bar charts comparing every brand across average selling price, average discount %, and average rating. Color-mapped for quick comparison.

### Visualization 3 — Price vs Discount Bubble Chart
Scatter plot where each bubble represents one laptop. X-axis = selling price, Y-axis = discount %, and bubble size = number of ratings (popularity). Color-coded by brand.

### Visualization 4 — Correlation Heatmap
Lower-triangle correlation matrix across all numeric features. Reveals strong positive correlation between number of ratings and reviews, and weak correlation between price and rating.

### Visualization 5 — Price Box Plot by Brand (Top 7)
Box + strip plot showing price spread (IQR, median, outliers) for the top 7 brands by listing count. Reveals Apple as a clear ultra-premium outlier while ASUS and Acer compete in the budget-mid range.

### Visualization 6 — Top 10 Best-Value Laptops
Ranked horizontal bar chart using a **Value Score = (Rating / Selling Price) × 100,000**, filtered to laptops with 50+ ratings. Identifies the best quality-per-rupee laptops on the platform.

---

## 🧠 Task 4 — Sentiment Analysis

Since the dataset contains **product names** rather than raw review text, a two-layer NLP strategy was applied:

| Layer | Tool | What It Analyzes |
|-------|------|-----------------|
| **VADER** | Rule-based lexicon (domain-tuned) | Product name tokens and spec keywords |
| **TextBlob** | ML-based polarity scoring | Product name polarity & subjectivity |
| **Rating-Backed** | Ground-truth validation | Actual customer rating converted to sentiment label |

### Step 4.1 — Text Preprocessing

Product names were cleaned before NLP scoring:
- Removed parentheses content (model suffixes)
- Stripped storage specs (e.g. `16GB`, `512GB SSD`)
- Removed all non-alphabetic characters
- Lowercased and normalized whitespace

### Step 4.2 — VADER Sentiment Scoring

VADER's lexicon was extended with **laptop-domain-specific words**:

| Positive Words (boosted) | Negative Words (penalized) |
|---|---|
| `slim`, `ultra`, `pro`, `elite`, `premium`, `gaming`, `lightweight`, `oled`, `powerful` | `lag`, `budget`, `basic`, `lite`, `entry`, `slow`, `chromebook` |

Each product received four VADER scores: `Positive`, `Negative`, `Neutral`, `Compound`. Compound ≥ 0.05 → Positive, ≤ −0.05 → Negative, else → Neutral.

### Step 4.3 — TextBlob Polarity & Subjectivity

TextBlob provided:
- **Polarity** score (−1 to +1): product name tone
- **Subjectivity** score (0 to 1): how descriptive vs factual the name is

### Step 4.4 — Rating-Backed Ground Truth

Customer ratings were mapped to sentiment labels for validation:
- Rating ≥ 4.0 → Positive
- Rating 3.5–3.99 → Neutral
- Rating < 3.5 → Negative

### Step 4.5 — Sentiment Visualizations (6 charts)

| # | Chart | Description |
|---|-------|-------------|
| 7 | Sentiment Distribution | Side-by-side bar charts comparing VADER vs TextBlob vs Rating-based sentiment |
| 8 | VADER by Brand | Average VADER compound score per brand — reveals brand name perception |
| 9 | Sentiment vs Avg Rating | Validates NLP labels against actual customer ratings |
| 10 | VADER vs TextBlob Scatter | Agreement scatter plot; points colored by actual rating sentiment |
| 11 | Word Cloud (Positive) | Word cloud of product names with positive VADER sentiment |
| 12 | Subjectivity vs Polarity | TextBlob scatter by price segment — Ultra Premium names are more subjective |

### Key Sentiment Findings

- **VADER** assigned a majority of laptops **Positive** sentiment, driven by spec-rich branding (Ultra, Pro, Elite)
- **TextBlob** was more conservative, with most products labeled **Neutral** due to factual/technical naming
- **Rating-backed validation** confirmed NLP accuracy: Positive-labeled products consistently had higher average customer ratings
- **VADER and TextBlob agree** on polarity direction for ~70% of products
- **Ultra Premium laptops** had the highest TextBlob subjectivity scores — premium brand names are more emotionally descriptive

---

## 🚀 How to Run the Full Project

```bash
# 1. Clone the repository
git clone https://github.com/Khprateek/CodeAlpha_DataPulse.git
cd CodeAlpha_DataPulse

# 2. Install all dependencies
pip install selenium webdriver-manager beautifulsoup4 pandas numpy \
            matplotlib seaborn wordcloud vaderSentiment textblob

# 3. Download TextBlob corpora
python -m textblob.download_corpora

# 4. Run scraper
python scraper.py

# 5. Run data cleaning
python clean_data.py

# 6. Open Jupyter notebooks for EDA, Visualization & Sentiment Analysis
jupyter notebook
```

---

## 👤 Author

**CodeAlpha Data Science Intern**
🔗 GitHub: [Khprateek](https://github.com/Khprateek)
🔗 LinkedIn: [Prateek Kharwar](https://www.linkedin.com/in/prateek-kharwar-a7764b270/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built as part of the CodeAlpha Data Science Internship Program*