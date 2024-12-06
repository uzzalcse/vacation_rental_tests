# data_scraper.py

from selenium.webdriver.common.by import By
import json
import logging

class DataScraper:
    @staticmethod
    def get_script_data(driver):
        try:
            scripts = driver.find_elements(By.TAG_NAME, 'script')
            data = {}
            
            for script in scripts:
                if 'window.__INITIAL_DATA__' in script.get_attribute('innerHTML'):
                    script_content = script.get_attribute('innerHTML')
                    json_str = script_content.split('window.__INITIAL_DATA__ = ')[1].split('};')[0] + '}'
                    data = json.loads(json_str)
                    break
                    
            return {
                'SiteURL': driver.current_url,
                'CampaignID': data.get('campaignId', ''),
                'SiteName': data.get('siteName', ''),
                'Browser': driver.capabilities['browserName'],
                'CountryCode': data.get('countryCode', ''),
                'IP': data.get('clientIP', '')
            }
        except Exception as e:
            logging.error(f"Error scraping script data: {str(e)}")
            return {}