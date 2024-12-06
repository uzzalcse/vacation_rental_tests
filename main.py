import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.excel_writer import write_to_excel
from tests.test_h1_tags import test_h1_tag
from tests.test_html_sequence import test_html_sequence
from tests.test_image_alt import test_image_alt
from tests.test_currency import test_currency_filtering
from tests.test_script_data import scrape_script_data
from selenium.webdriver.common.by import By

MAIN_URL = "https://www.alojamiento.io/"
RESULTS_FILE = "test_results.xlsx"

def fetch_child_urls(driver, url):
    """Fetch all child links from the main page."""
    driver.get(url)
    anchors = driver.find_elements(By.TAG_NAME, "a")
    child_urls = set(anchor.get_attribute("href") for anchor in anchors if anchor.get_attribute("href"))
    return [url for url in child_urls if url.startswith(MAIN_URL)]

def run_tests_on_page(url, driver, country_code, ip):
    """
    Run all tests for a given page and return results.
    """
    results = []
    results.append({
        "test_case": "H1 Tag Existence",
        "status": test_h1_tag(driver, url),
        "comments": "Test for H1 tag"
    })
    
    results.append({
        "test_case": "HTML Sequence Test",
        "status": test_html_sequence(driver, url),
        "comments": "Test for HTML tag sequence"
    })
    
    results.append({
        "test_case": "Image Alt Test",
        "status": test_image_alt(driver, url),
        "comments": "Test for image alt attributes"
    })
    
    results.append({
        "test_case": "Currency Filtering Test",
        "status": test_currency_filtering(driver, url),
        "comments": "Test for currency filtering on property tiles"
    })
    
    results.append({
        "test_case": "Scrape Script Data",
        "status": scrape_script_data(driver, url, country_code, ip),
        "comments": "Scrape site data and record it"
    })
    
    return results


def main():
    # Configure WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Fetch child URLs dynamically
    child_urls = fetch_child_urls(driver, MAIN_URL)
    country_code = "US"
    ip = "127.0.0.1"  # Replace with dynamic IP fetching logic

    # Dictionary to store results by URL
    results_by_url = {}

    for url in child_urls:
        print(f"Testing: {url}")
        results_by_url[url] = run_tests_on_page(url, driver, country_code, ip)

    # Write results to Excel file
    write_to_excel(RESULTS_FILE, results_by_url)
    driver.quit()
    print(f"Results saved to {RESULTS_FILE}")

if __name__ == "__main__":
    main()
