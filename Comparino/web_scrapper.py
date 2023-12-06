import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_flipkart(url):
    chrome_options = Options()
    chrome_options.headless = False  # Set to True if you don't want the browser to be visible

    # Adjust the path to your chromedriver executable
    driver = webdriver.Chrome(executable_path=r'C:/Users/Poojavb/Downloads/chromedriver_win32/chromedriver.exe', options=chrome_options)

    driver.get(url)
    time.sleep(5)  # Adjust the sleep time based on the page load time
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    products = []

    for product in soup.find_all('div', class_='_1AtVbE'):
        name = product.find('a', class_='IRpwTa').text.strip()
        price = product.find('div', class_='_30jeq3').text.strip()
        link = product.find('a', class_='IRpwTa')['href']
        link = f'https://www.flipkart.com{link}'

        products.append({
            'name': name,
            'price': price,
            'link': link
        })

    driver.quit()
    return products

def scrape_gem(url):
    chrome_options = Options()
    chrome_options.headless = False  # Set to True if you don't want the browser to be visible

    # Adjust the path to your chromedriver executable
    driver = webdriver.Chrome(executable_path=r'C:/Users/Poojavb/Downloads/chromedriver_win32/chromedriver.exe', options=chrome_options)

    driver.get(url)
    time.sleep(5)  # Adjust the sleep time based on the page load time
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    products = []

    for product in soup.find_all('div', class_='searchresultItemBox'):
        name = product.find('a', class_='productNameLink').text.strip()
        price = product.find('span', class_='product-discountedPrice').text.strip()
        link = product.find('a', class_='productNameLink')['href']
        link = f'https://mkp.gem.gov.in{link}'

        products.append({
            'name': name,
            'price': price,
            'link': link
        })

    driver.quit()
    return products

# Example usage for Flipkart:
flipkart_url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax"
flipkart_products = scrape_flipkart(flipkart_url)

# Save Flipkart data to CSV
with open("flipkart_products.csv", mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['name', 'price', 'link']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for product in flipkart_products:
        writer.writerow(product)

# Example usage for GeM:
gem_url = "https://mkp.gem.gov.in/search?q=Mobiles"
gem_products = scrape_gem(gem_url)

# Save GeM data to CSV
with open("gem_products.csv", mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['name', 'price', 'link']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for product in gem_products:
        writer.writerow(product)
