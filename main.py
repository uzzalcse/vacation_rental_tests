from tests_runners.run_tests import run_h1_test
from tests_runners.run_tests import run_heading_sequence_test
from tests_runners.run_tests import run_image_alt_test
from tests_runners.run_tests import run_url_test
from tests_runners.run_tests import run_scrape_data
from tests_runners.run_tests import run_test_currency_filtering

if __name__ == "__main__":
    page_url = "https://www.alojamiento.io/"

    # run_h1_test(page_url)
    # run_heading_sequence_test(page_url)
    # run_image_alt_test(page_url)
    # run_url_test(page_url)   
    # run_scrape_data(page_url)
    run_test_currency_filtering(page_url)
