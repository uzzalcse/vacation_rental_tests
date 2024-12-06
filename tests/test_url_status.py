# test_url_status.py

from selenium.webdriver.common.by import By
from base_test import BaseTest
from excel_writer import ExcelWriter
from url_utils import URLUtils

class URLStatusTest(BaseTest):
    def __init__(self):
        super().__init__()
        self.excel_writer = ExcelWriter()
        
    def test_url_status(self, url):
        try:
            self.setup()
            self.driver.get(url)
            
            # Get all links
            links = self.driver.find_elements(By.TAG_NAME, 'a')
            broken_links = []
            
            for link in links:
                href = link.get_attribute('href')
                if href and not href.startswith('javascript'):
                    status_code = URLUtils.check_url_status(href)
                    if status_code == 404:
                        broken_links.append(href)
            
            status = 'PASS' if not broken_links else 'FAIL'
            comments = 'All URLs are valid' if not broken_links else f'Broken links found: {", ".join(broken_links)}'
            
            self.excel_writer.add_result(
                page_url=url,
                testcase='URL Status Check',
                status=status,
                comments=comments
            )
            
        except Exception as e:
            self.excel_writer.add_result(
                page_url=url,
                testcase='URL Status Check',
                status='ERROR',
                comments=str(e)
            )
        finally:
            self.teardown()
            
    def save_results(self):
        self.excel_writer.save_results(sheet_name='URL Status Tests')