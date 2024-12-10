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
from tests_runners.run_tests import run_h1_test
from tests_runners.run_tests import run_heading_sequence_test
from tests_runners.run_tests import run_image_alt_test
from tests_runners.run_tests import run_url_test
from tests_runners.run_tests import run_scrape_data
from tests_runners.run_tests import run_test_currency_filtering

if __name__ == "__main__":
    page_url = "https://www.alojamiento.io/"

    run_h1_test(page_url)
    run_heading_sequence_test(page_url)
    run_image_alt_test(page_url)
    #run_url_test(page_url)   
    run_scrape_data(page_url)
    run_test_currency_filtering(page_url)
