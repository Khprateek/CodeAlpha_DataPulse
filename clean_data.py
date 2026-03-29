import pandas as pd
import re

df = pd.read_csv("flipkart_laptops.csv")

print("Before cleaning:", df.shape)

# ============================================
# 1. EXTRACT BRAND NAME from Product Name
# ============================================
brands = ["ASUS", "HP", "Lenovo", "Dell", "DELL", "Acer", "Samsung", 
          "Apple", "MSI", "Microsoft", "Infinix", "Realme", "GIGABYTE"]

def extract_brand(name):
    for brand in brands:
        if brand.lower() in str(name).lower():
            return brand.upper() if brand == "Dell" else brand
    return "Other"

df["Brand"] = df["Product Name"].apply(extract_brand)

# ============================================
# 2. CLEAN PRICE COLUMNS (fix â,' → ₹)
# ============================================
def clean_price(value):
    if pd.isna(value) or value == "N/A":
        return None
    # Remove encoding garbage, ₹ symbol, commas
    value = str(value)
    value = re.sub(r'[^\d,.]', '', value)  # Keep only digits, commas, dots
    value = value.replace(",", "").strip()
    try:
        return float(value)
    except:
        return None

df["Selling Price (INR)"] = df["Selling Price"].apply(clean_price)
df["Original Price (INR)"] = df["Original Price"].apply(clean_price)

# ============================================
# 3. CLEAN DISCOUNT COLUMN
# ============================================
def clean_discount(value):
    if pd.isna(value) or value == "N/A":
        return None
    value = str(value)
    match = re.search(r'(\d+)', value)
    return int(match.group(1)) if match else None

df["Discount (%)"] = df["Discount"].apply(clean_discount)

# ============================================
# 4. CLEAN RATING COUNT
# ============================================
def extract_ratings(value):
    if pd.isna(value) or value == "N/A":
        return None
    match = re.search(r'(\d[\d,]*)\s*Ratings?', str(value))
    if match:
        return int(match.group(1).replace(",", ""))
    return None

def extract_reviews(value):
    if pd.isna(value) or value == "N/A":
        return None
    match = re.search(r'(\d+)\s*Reviews?', str(value))
    return int(match.group(1)) if match else None

df["Number of Ratings"] = df["Rating Count"].apply(extract_ratings)
df["Number of Reviews"] = df["Rating Count"].apply(extract_reviews)

# ============================================
# 5. CLEAN RATING COLUMN
# ============================================
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# ============================================
# 6. DROP OLD MESSY COLUMNS
# ============================================
df.drop(columns=["Selling Price", "Original Price", "Discount", "Rating Count"], inplace=True)

# ============================================
# 7. REMOVE DUPLICATES & MISSING
# ============================================
df.drop_duplicates(subset=["Product Name"], inplace=True)
df.dropna(subset=["Product Name"], inplace=True)

# ============================================
# 8. REORDER COLUMNS NEATLY
# ============================================
df = df[["Brand", "Product Name", "Selling Price (INR)", "Original Price (INR)", 
         "Discount (%)", "Rating", "Number of Ratings", "Number of Reviews"]]

# ============================================
# 9. SAVE CLEANED FILE
# ============================================
df.to_csv("data/flipkart_laptops_cleaned.csv", index=False)

print(f"✅ Cleaned! Shape: {df.shape}")
print("\n", df.head(5).to_string())
print("\nMissing values:\n", df.isnull().sum())
print("\nBrand Distribution:\n", df["Brand"].value_counts())