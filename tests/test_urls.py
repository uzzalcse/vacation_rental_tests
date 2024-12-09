import requests
import os
import pandas as pd
from openpyxl import load_workbook


def test_url_status(hrefs):
    """
    Tests the HTTP status of a list of URLs.
    :param hrefs: List of URLs to test.
    :return: List of test results.
    """
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
                    'passed_fail': 'fail',
                    'comments': '404 Error'
                })
            else:
                results.append({
                    'page_url': href,
                    'testcase': 'URL Status Code Test',
                    'passed_fail': 'pass',
                    'comments': 'URL is valid'
                })
        except requests.exceptions.RequestException as e:
            # Handle invalid/exception URLs
            results.append({
                'page_url': href,
                'testcase': 'URL Status Code Test',
                'passed_fail': 'fail',
                'comments': f'Error: {e}'
            })
    
    return results


