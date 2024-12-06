# url_utils.py

import requests
from urllib.parse import urljoin
import logging

class URLUtils:
    @staticmethod
    def check_url_status(url):
        try:
            response = requests.head(url, allow_redirects=True, timeout=10)
            return response.status_code
        except Exception as e:
            logging.error(f"Error checking URL {url}: {str(e)}")
            return 0
            
    @staticmethod
    def get_absolute_url(base_url, relative_url):
        return urljoin(base_url, relative_url)