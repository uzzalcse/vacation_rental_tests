import requests
import os
import pandas as pd
from openpyxl import load_workbook


def test_url_status(hrefs):

    results = []
    
    for href in hrefs:
        try:
            # Send request to URL
            response = requests.get(href)
            # Check if response code is 404
            if response.status_code == 404:
                results.append({
                    'page_url': href,
                    'testcase': 'URL Status Code Test',
                    ' passed/fail': 'Fail',
                    'comments': '404 Error'
                })
            else:
                results.append({
                    'page_url': href,
                    'testcase': 'URL Status Code Test',
                    ' passed/fail': 'Pass',
                    'comments': 'URL is valid'
                })
        except requests.exceptions.RequestException as e:
            # Handle invalid/exception URLs
            results.append({
                'page_url': href,
                'testcase': 'URL Status Code Test',
                ' passed/fail': 'Fail',
                'comments': f'Error: {e}'
            })
    
    return results


