import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_h1(urls, driver):
    # Initialize result list
    results = []

    for page_url in urls:
        try:
            # Open the target webpage
            driver.get(page_url)

            # Wait implicitly for elements to load
            driver.implicitly_wait(10)

            # Attempt to find H1 tag
            try:
                h1_tag = driver.find_element(By.TAG_NAME, "h1")
                # Record test result if H1 tag is found
                results.append({
                    "page_url": page_url,
                    "testcase": "Check H1 tag presence",
                    " passed/fail": "Pass",
                    "comments": f"Found H1 tag with text: {h1_tag.text}"
                })
            except NoSuchElementException:
                # Record test result if H1 tag is not found
                results.append({
                    "page_url": page_url,
                    "testcase": "Check H1 tag presence",
                    " passed/fail": "Fail",
                    "comments": "H1 tag not found on the page"
                })

        except Exception as e:
            results.append({
                "page_url": page_url,
                "testcase": "Check H1 tag presence",
                "passed_fail": "Fail",
                "comments": f"Error: {e}",
            })

    # Return the results
    return results