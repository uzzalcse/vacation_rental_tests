import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_heading_sequence(url, driver):

    results = []  # Initialize a list to store test results

    try:
        # Open the test page
        driver.get(url)

        # Wait for page load
        driver.implicitly_wait(10)  # Wait for up to 10 seconds

        # Validate sequence H1 through H6
        for i in range(1, 7):  # Loop H1 to H6
            try:
                # Attempt to find each heading
                driver.find_element(By.TAG_NAME, f"h{i}")
               # print(f"Found H{i} tag.")
            except NoSuchElementException:
                # Report failure if a heading is missing
                #print(f"FAIL: Missing H{i} tag.")
                results.append({
                    "page_url": url,
                    "testcase": f"Check for H{i} presence in sequence",
                    "passed/fail": "Fail",
                    "comments": f"Missing H{i} tag"
                })
                # Stop checking further in sequence because it's broken
                break
        else:
            # If no failure was found in the entire sequence
            results.append({
                "page_url": url,
                "testcase": "Validate full H1-H6 tag sequence",
                "passed/fail": "Pass",
                "comments": "All tags found in proper sequence."
            })

    except Exception as e:
        # Log any unexpected exception during the test
        results.append({
            "page_url": url,
            "testcase": "Unexpected error during validation",
            "passed/fail": "Fail",
            "comments": f"Error: {e}"
        })

    # Return the results list
    return results