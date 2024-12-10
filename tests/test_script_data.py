import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_script_data(url, driver):
    
    results = []  # Initialize result list

    try:
        # Open the target webpage
        driver.get(url)

        # Wait for the page to load
        time.sleep(3)

        # Get scriptData from JavaScript on the page
        script_data = driver.execute_script("return window.ScriptData;")

        # Extracting required fields from ScriptData
        if script_data:
            site_url = script_data['config']['SiteUrl']  # Site URL from config
            site_name = script_data['config']['SiteName']  # Site name from config
            campaign_id = script_data['pageData'].get('CampaignId', 'Not found')  # Campaign ID from pageData
            user_info = script_data.get('userInfo', {})
            browser = user_info.get('Browser', 'Not found')  # Browser from userInfo
            country_code = user_info.get('CountryCode', 'Not found')  # CountryCode from userInfo
            ip = user_info.get('IP', 'Not found')  # IP from userInfo

            # Store the results
            results.append({
                'SiteURL': site_url,
                'CampaignID': campaign_id,
                'SiteName': site_name,
                'Browser': browser,
                'CountryCode': country_code,
                'IP': ip,
            })

        else:
            print(f"No ScriptData found on {url}")

    except Exception as e:
        print(f"Error processing {url}: {e}")
    finally:
        driver.quit()

    return results