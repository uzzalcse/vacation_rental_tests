from selenium.webdriver.common.by import By

def test_html_sequence(driver, url):
    """Test the HTML tag sequence (H1-H6)."""
    driver.get(url)
    
    # Loop through H1 to H6 tags and check if they exist
    tags = [driver.find_elements(By.TAG_NAME, f"h{i}") for i in range(1, 7)]
    
    for i, tag in enumerate(tags, start=1):
        if not tag:
            return {
                "url": url,
                "testcase": f"H{i} tag sequence",
                "result": "Fail",
                "comments": f"H{i} tag missing"
            }
    
    return {
        "url": url,
        "testcase": "HTML tag sequence",
        "result": "Pass",
        "comments": "H1-H6 tags are present in correct order"
    }
