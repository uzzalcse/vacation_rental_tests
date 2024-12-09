from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_chrome_driver(driver_path="./chromedriver", headless=False):
    """
    Configures and returns a Chrome WebDriver instance.
    :param driver_path: Path to the ChromeDriver executable.
    :param headless: Run Chrome in headless mode (default: False).
    :return: Configured WebDriver instance.
    """
    # Ensure ChromeDriver path is executable
    service = Service(driver_path)
    
    # Set Chrome options
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
    
    return webdriver.Chrome(service=service, options=options)
