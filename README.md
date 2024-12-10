# Vacation Rental Home Page Automation Testing

## Description

This project automates the testing of a vacation rental details page (https://www.alojamiento.io/) to validate key elements and functionalities. The script checks several SEO-related test cases such as:

- H1 tag existence
- HTML tag sequence validation (H1-H6)
- Image alt attribute validation
- URL status code validation (404 check)
- Currency filter functionality
- Scraping of script data and storing it in an Excel file



# Project Structure 

📁 vacation_rental_tests/  
├── 📁 reports/  
│   └──── 📄 test_results.xlsx  
│
├── 📁 tests/  
│   ├── 📄 __init__.py  
│   ├── 📄 test_currency.py  
│   ├── 📄 test_h1_tag.py  
│   ├── 📄 test_image_al.py  
│   ├── 📄 test_script_data.py  
│   ├── 📄 test_tags_sequence.py  
│   ├── 📄 test_urls.py  
│
├── 📁 tests_runners/  
│   └── 📄 run_tests.py  
│
├── 📁 utils/  
│   ├── 📄 __init__.py  
│   ├── 📄 excel_writer.py  
│
├── 📄 __init__.py  
├── 📄 main.py  
├── 📄 chrome_driver_config.py  
├── 📄 README.md  
├── 📄 requirements.txt  
└── 📄 .gitignore  


## Requirements

- Python 3.x
- Selenium WebDriver
- Google Chrome (minimum version: 131.0.6778.108)
- Pandas
- openpyxl

### Libraries

- **Selenium**: For web automation.
- **Pandas**: For recording test results into a CSV file.
- **WebDriver**: Google Chrome

### Installation

#### Clone the project repository

```
git clone https://github.com/uzzalcse/vacation_rental_tests.git

```

#### Go to the project directory 

```
cd vacation_rental_tests

```

#### Creating virtual environment 

```
python3 -m venv venv

```
#### If the previous (for creating virtual environment) command does not work 

```
python -m venv venv

```

#### Go to the virtual environment
##### In Windows
```
venv\Scripts\activate

```

###### In Mac/Linux

```
source venv/bin/activate

```


#### Now install  dependencies in virtual environment

```
pip install -r requirements.txt

```

#### Now write the following command to run the project 

```
python main.py

```

#### To see results check `reports/test_results.xlsx` file. 

Change the sheets on excel file ( `test_results.xlsx` ) to see results for each tests. For better performance go to `main.py` and run only required tests. Make comment and uncomment others.  
This way you can change `main.py` and see the specific tests.
```
if __name__ == "__main__":
    page_url = "https://www.alojamiento.io/"

    run_h1_test(page_url)
    #run_heading_sequence_test(page_url)
    #run_image_alt_test(page_url)
    #run_url_test(page_url)   
    run_scrape_data(page_url)
    #run_test_currency_filtering(page_url)
```

The results of each test are recorded in the excel file with the following format:

| page_url  | testcase | passed/fail | comments |
|-----------|----------|-------------|----------|

## Test Cases

### 1. **H1 Tag Existence**
- **Description:** Verifies that the page contains an `<h1>` tag. If missing, the test fails.
- **Test Details:** Ensures that the most important heading tag exists for SEO and accessibility.

### 2. **HTML Tag Sequence**
- **Description:** Ensures the HTML tag sequence from `<h1>` to `<h6>` is followed correctly.
- **Test Details:** If any tag is missing or out of sequence, the test fails. This ensures proper use of heading tags for SEO.

### 3. **Image Alt Attribute**
- **Description:** Checks if all images on the page contain the `alt` attribute.
- **Test Details:** If any image is missing an `alt` attribute, the test fails. This is important for accessibility and SEO.

### 4. **URL Status Code Check**
- **Description:** Verifies that all URLs on the page return a valid status code (anything other than 404).
- **Test Details:** If a 404 error is found, the test fails. This ensures that all external and internal links on the page are working correctly.

### 5. **Currency Filtering**
- **Description:** Tests if the currency filter on the page works correctly.
- **Test Details:** Ensures that the currency on property tiles changes when the user selects a new currency, confirming that the currency filter functionality is operational.

### 6. **Script Data Scraping**
- **Description:** Scrapes the script data from the page.
- **Test Details:** Extracts data such as SiteURL, CampaignID, SiteName, Browser, CountryCode, and IP, and records it into an Excel file for reporting.