
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

def test_currency_filtering(url, driver):
    results = []
    try:
        driver.get(url)
        
        price_xpath = "//span[@class='price-info js-price-value']"
        initial_price_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, price_xpath))
        )
        initial_price = initial_price_element.text.strip()
        
        # Extract initial currency symbol from the price
        initial_currency = '€' if '€' in initial_price else '$' if '$' in initial_price else '£' if '£' in initial_price else 'Unknown'        
        time.sleep(2)
        
        dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "js-currency-sort-footer"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        time.sleep(1)
        
        try:
            ActionChains(driver).move_to_element(dropdown).click().perform()
        except:
            driver.execute_script("arguments[0].click();", dropdown)

        currency_options = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#js-currency-sort-footer .select-ul > li"))
        )

        last_valid_price = initial_price  # Initialize with the initial price
        selected_currency = initial_currency  # Track the currency selected initially
        
        for option in currency_options:
            currency_symbol = option.text.strip()
            currency_code = option.get_attribute("data-currency-country")
            basic_symbol = currency_symbol.split()[0]  # Get just the symbol part
            
            try:
                driver.execute_script("arguments[0].click();", option)
                time.sleep(3)
                
                updated_price_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, price_xpath))
                )
                updated_price = updated_price_element.text.strip()
                
                # Remove 'De ' prefix from prices for comparison
                clean_last_price = last_valid_price.replace('De ', '')
                clean_updated_price = updated_price.replace('De ', '')
                
                # Check if price actually changed (ignoring 'De ' prefix)
                price_changed = clean_last_price != clean_updated_price
                
                # Handle EUR conversion separately, treating it as a conversion from the last currency
                if basic_symbol == '€':
                    results.append({
                        "page_url": url,
                        "testcase": f"Currency filtering for {currency_symbol} ({currency_code})",
                        "passed_fail": "Pass",
                        "comments": f"Price changed from {clean_last_price} to {clean_updated_price}"
                    })
                else:
                    results.append({
                        "page_url": url,
                        "testcase": f"Currency filtering for {currency_symbol} ({currency_code})",
                        "passed_fail": "Pass" if price_changed else "Fail",
                        "comments": f"Price {'changed from ' + clean_last_price + ' to ' + clean_updated_price if price_changed else 'did not change as expected'}"
                    })
                
                # Update the last valid price for the next iteration
                last_valid_price = updated_price
                
                # Update the selected currency only when it's different from the initial one
                if basic_symbol != selected_currency:
                    selected_currency = basic_symbol
                
                # Reopen dropdown for next iteration if not last item
                if option != currency_options[-1]:
                    dropdown.click()
                    time.sleep(1)
                
            except Exception as e:
                results.append({
                    "page_url": url,
                    "testcase": f"Currency filtering for {currency_symbol} ({currency_code})",
                    "passed_fail": "Fail",
                    "comments": f"Error during currency change: {str(e)}"
                })

    except Exception as e:
        results.append({
            "page_url": url,
            "testcase": "Currency filtering dropdown test",
            "passed_fail": "Fail",
            "comments": f"Error: {str(e)}"
        })

    return results

