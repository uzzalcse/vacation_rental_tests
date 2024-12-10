
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome_driver_config import get_chrome_driver
from tests.test_urls import test_url_status
from utils.excel_writer import save_results_to_excel
from tests.test_image_alt import image_alt_attribute_test  # Assuming this is in image_alt_test.py
from tests.test_h1_tag import test_h1
from tests.test_tags_sequence import test_heading_sequence
from tests.test_script_data import scrape_script_data
from tests.test_currency import test_currency_filtering


def get_driver_path():

    # Check the operating system
    if os.name == 'posix':  # Linux or macOS
        return './chromedriver'  # Assuming chromedriver is in the project root for Linux
    elif os.name == 'nt':  # Windows
        return './chromedriver.exe'  # Assuming chromedriver.exe is in the project root for Windows
    else:
        raise Exception("Unsupported OS. This script supports only Windows and Linux.")

def run_h1_test(page_url, driver_path=None, headless=False):
    print("h1 test started...")
    if not driver_path:
        driver_path = get_driver_path()
    
    driver = get_chrome_driver(driver_path, headless)
    
    try:
        # Open the URL
        driver.get(page_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        
        # Pass the URL to the image alt attribute test function
        results = test_h1([page_url], driver)
        
        # Save results to Excel
        save_results_to_excel(results, sheet_name="H1 tag test")
    finally:
        # Close Selenium driver
        print("h1 test ended.")
        driver.quit()

def run_heading_sequence_test(url, driver_path=None, headless=False):
    print("heading sequence test started...")
    if not driver_path:
        driver_path = get_driver_path()
    
    driver = get_chrome_driver(driver_path, headless)
    
    try:
        # Run the heading sequence test
        results = test_heading_sequence(url, driver)
        
        # Save results to Excel
        save_results_to_excel(results, sheet_name="Heading tag sequence test")
    finally:
        # Close the Selenium driver
        print("heading sequence test ended.")
        driver.quit()

def run_image_alt_test(page_url, driver_path=None, headless=False):
    print("image alt test started...")
    if not driver_path:
        driver_path = get_driver_path()
    
    # Initialize Selenium driver
    driver = get_chrome_driver(driver_path, headless)
    
    try:
        # Open the URL
        driver.get(page_url)
        time.sleep(2)  # Allow time for page elements to load
        
        # Pass the URL to the image alt attribute test function
        results = image_alt_attribute_test([page_url], driver)
        
        # Save results to Excel
        save_results_to_excel(results, sheet_name="Image alt attribute test")
    finally:
        # Close Selenium driver
        print("image alt test ended.")
        driver.quit()

def run_url_test(page_url, driver_path=None, headless=False):
    print("url test started...")
    if not driver_path:
        driver_path = get_driver_path()
    
    # Initialize Selenium driver
    driver = get_chrome_driver(driver_path, headless)
    
    try:
        # Open the URL
        driver.get(page_url)
        time.sleep(2)  # Allow time for page elements to load
        
        # Extract all href links
        links = driver.find_elements(By.TAG_NAME, 'a')
        hrefs = [link.get_attribute('href') for link in links if link.get_attribute('href')]
        
        # Test URL statuses
        results = test_url_status(hrefs)
        
        # Save results to Excel
        save_results_to_excel(results, sheet_name="URL status test")
    finally:
        # Close Selenium driver
        print("url test ended.")
        driver.quit()

def run_scrape_data(url, driver_path=None, headless=False):
    print("scrape data test started...")
    if not driver_path:
        driver_path = get_driver_path()
    
    driver = get_chrome_driver(driver_path, headless)
    
    try:
        # Run the script data scraping test
        results = scrape_script_data(url, driver)
        
        # Save results to Excel
        save_results_to_excel(results, sheet_name="Scrape script data test")
    finally:
        # Close the Selenium driver
        print("scrape data test ended.")
        driver.quit()


def run_test_currency_filtering(url, driver_path=None, headless=False):
    print("currency filtering test started...")
    if not driver_path:
        driver_path = get_driver_path()
    
    driver = get_chrome_driver(driver_path, headless)
    
    try:
        # Run the script data scraping test
        results = test_currency_filtering(url, driver)
                
        # Save results to Excel
        save_results_to_excel(results, sheet_name="Currency filtering test")
    finally:
        # Close the Selenium driver
        print("currency filtering test ended.")
        driver.quit()
