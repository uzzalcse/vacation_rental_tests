import pandas as pd
from selenium.webdriver.common.by import By


def scrape_and_record_to_excel(driver, url, browser, country_code, ip):
    driver.get(url)
    script_data = driver.find_element(By.TAG_NAME, "script").get_attribute("innerHTML")
    
    data = {
        'SiteURL': [url],
        'CampaignID': ["12345"],  # Example value, scrape actual CampaignID
        'SiteName': ["Alojamiento"],
        'Browser': [browser],
        'CountryCode': [country_code],
        'IP': [ip]
    }
    
    df = pd.DataFrame(data)
    return df
