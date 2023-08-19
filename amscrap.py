from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open("Amazon.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all divs with the specified class
divs = soup.find_all("div", class_="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t1 puis-include-content-margin puis puis-v3b48cl1js792724v4d69zlbwph s-latency-cf-section s-card-border")

# Create a new Excel workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add headers to the sheet
sheet.append(["Product Name", "Product Price", "Product Reviews"])

# Iterate through the divs and extract information
for div in divs:
    product_name_elem = div.find("span", class_="a-size-medium a-color-base a-text-normal")
    product_name = product_name_elem.get_text(strip=True) if product_name_elem else ""

    product_price_elem = div.find("span", class_="a-price-whole")
    product_price = product_price_elem.get_text(strip=True) if product_price_elem else ""

    product_reviews_elem = div.find("span", class_="a-size-base puis-normal-weight-text")
    product_reviews = product_reviews_elem.get_text(strip=True) if product_reviews_elem else ""

    # Append data to the sheet
    sheet.append([product_name, product_price, product_reviews])

# Save the workbook
workbook.save("Amazon_Products.xlsx")
print("Data has been written to Amazon_Products.xlsx")
