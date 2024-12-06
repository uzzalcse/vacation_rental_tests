from selenium.webdriver.common.by import By

def test_image_alt(driver, url):
    """Test that images have alt attributes."""
    driver.get(url)
    
    # Find all image elements on the page
    images = driver.find_elements(By.TAG_NAME, "img")
    
    # Check if each image has an alt attribute
    for img in images:
        alt_text = img.get_attribute("alt")
        if not alt_text:
            return {
                "url": url,
                "testcase": "Image alt attribute",
                "result": "Fail",
                "comments": "Image missing alt attribute"
            }
    
    return {
        "url": url,
        "testcase": "Image alt attribute",
        "result": "Pass",
        "comments": "All images have alt attributes"
    }
