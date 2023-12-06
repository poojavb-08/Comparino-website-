import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a new instance of the Chrome web browser
driver = webdriver.Chrome()

# Navigate to Amazon.in
driver.get("https://www.amazon.in/")

# Create a CSV file to write the data
csv_file = open('amazon_products.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Category', 'Title', 'Price', 'Link'])

# Find and print product category links
category_links = driver.find_elements(By.CSS_SELECTOR, ".fsdLink")
for link in category_links:
    category_name = link.text.strip()
    category_url = link.get_attribute("href")

    # Visit the category page
    driver.get(category_url)

    # Wait for the products to load (you may need to adjust the timeout)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s-result-item")))

    # Find and print product details
    product_titles = driver.find_elements(By.CSS_SELECTOR, ".s-title-instructions a")
    product_prices = driver.find_elements(By.CSS_SELECTOR, ".a-price .a-offscreen")
    product_links = driver.find_elements(By.CSS_SELECTOR, ".s-title-instructions a")

    for title, price, link in zip(product_titles, product_prices, product_links):
        csv_writer.writerow([category_name, title.text, price.text, link.get_attribute("href")])

# Close the CSV file
csv_file.close()

# Close the browser
driver.quit()
