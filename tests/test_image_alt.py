import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def image_alt_attribute_test(urls, driver):
    """
    Tests if images on a list of URLs have the 'alt' attribute.
    :param urls: List of URLs to test.
    :param driver: Selenium WebDriver instance.
    :return: List of test results.
    """
    results = []  # Initialize a list to store test results

    for page_url in urls:
        try:
            # Open the target webpage
            driver.get(page_url)

            # Allow the page to load
            driver.implicitly_wait(10)

            # Get all images on the page
            images = driver.find_elements("tag name", "img")

            if len(images) == 0:
                results.append({
                    "page_url": page_url,
                    "testcase": "Image alt attribute test",
                    "passed_fail": "fail",
                    "comments": "No images found"
                })
                continue

            # Loop through all images and test if they have valid alt attributes
            for image in images:
                # Extract the image's source URL and its alt attribute
                image_url = image.get_attribute("src")
                alt_value = image.get_attribute("alt")

                # Check if alt is missing or empty
                if alt_value is None or alt_value.strip() == "":
                    result = {
                        "page_url": image_url,  # Set image URL as the test URL
                        "testcase": "Image alt attribute test",
                        "passed_fail": "fail",
                        "comments": "Missing alt attribute",
                    }
                else:
                    result = {
                        "page_url": image_url,  # Set image URL as the test URL
                        "testcase": "Image alt attribute test",
                        "passed_fail": "pass",
                        "comments": "Alt attribute present",
                    }

                # Append the result to the results list
                results.append(result)

        except Exception as e:
            results.append({
                "page_url": page_url,
                "testcase": "Image alt attribute test",
                "passed_fail": "fail",
                "comments": f"Error: {e}",
            })

    # Return the results
    return results