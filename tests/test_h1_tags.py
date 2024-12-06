from selenium.webdriver.common.by import By

def test_h1_tag(driver, url):
    """Test the existence of H1 tags on the page."""
    driver.get(url)
    h1_tags = driver.find_elements(By.TAG_NAME, "h1")
    
    if not h1_tags:
        return {"url": url, "testcase": "H1 tag existence", "result": "Fail", "comments": "No H1 tag found"}
    
    return {"url": url, "testcase": "H1 tag existence", "result": "Pass", "comments": "H1 tag exists"}
