# Vacation Rental Homepage Automation Testing

## Description

This project automates the testing of a vacation rental details page ([https://www.alojamiento.io/](https://www.alojamiento.io/)) to validate key elements and functionalities. It performs the following key tests for SEO and functionality:

- Verifies the existence of the `<h1>` tag.
- Ensures proper HTML heading tag sequence (`<h1>` to `<h6>`).
- Validates the presence of `alt` attributes in images.
- Checks URL status codes (e.g., 404 errors).
- Tests the functionality of the currency filter.
- Scrapes and records relevant script data into an Excel file.

## Project Structure

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

### Prerequisites

- Python 3.x
- Selenium WebDriver
- Google Chrome (minimum version: 131.0.6778.108)
- Pandas
- Openpyxl

### Libraries

- **Selenium**: For web automation.
- **Pandas**: For recording test results into a CSV file.
- **ChromeDriver**: Google Chrome WebDriver for running Selenium tests.

## Setup & Installation

### Clone the Repository

```bash
git clone https://github.com/uzzalcse/vacation_rental_tests.git
```

### Navigate to the Project Directory

```bash
cd vacation_rental_tests
```

### Create a Virtual Environment

```bash
python3 -m venv venv
```

#### If the Above Command Fails

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### On Windows

```bash
venv\Scripts\activate
```

#### On Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python main.py
```

### View Results

- Test results will be saved in the `reports/test_results.xlsx` file.
- Each test's results are saved in separate sheets.

### Customize Tests

To run specific tests, edit `main.py` and commnet or uncomment the desired tests:

```python
if __name__ == "__main__":
    page_url = "https://www.alojamiento.io/"

    run_h1_test(page_url)
    #run_heading_sequence_test(page_url)
    #run_image_alt_test(page_url)
    #run_url_test(page_url)   
    run_scrape_data(page_url)
    #run_test_currency_filtering(page_url)
```

## Test Cases

### 1. **H1 Tag Existence**
- **Purpose**: Verifies the presence of an `<h1>` tag for SEO and accessibility.
- **Validation**: Fails if the `<h1>` tag is missing.

### 2. **HTML Tag Sequence**
- **Purpose**: Ensures the correct sequence of HTML heading tags (`<h1>` to `<h6>`).
- **Validation**: Fails if any tag is missing or out of sequence.

### 3. **Image Alt Attribute**
- **Purpose**: Checks that all images contain the `alt` attribute for SEO and accessibility.
- **Validation**: Fails if any image is missing an `alt` attribute.

### 4. **URL Status Code Check**
- **Purpose**: Verifies that all URLs on the page return valid status codes (e.g., no 404 errors).
- **Validation**: Fails if any URL returns a 404 error.

### 5. **Currency Filtering**
- **Purpose**: Tests if the currency filter works as expected.
- **Validation**: Ensures that selecting a currency updates the displayed prices accordingly.

### 6. **Script Data Scraping**
- **Purpose**: Extracts key script data from the page, such as:
  - SiteURL
  - CampaignID
  - SiteName
  - Browser
  - CountryCode
  - IP
- **Validation**: Saves the extracted data into the Excel report.

## Result Format

The results are recorded in `reports/test_results.xlsx` in the following format:

| Page URL       | Test Case Name        | Result (Pass/Fail) | Comments           |
|----------------|-----------------------|--------------------|--------------------|

## Notes

- Ensure that you have the latest version of ChromeDriver compatible with your Google Chrome browser.
- If you encounter issues, check the `chrome_driver_config.py` file for configuration settings.
- Modify `main.py` to run only the necessary tests for efficiency.



## Contribution

We welcome contributions to improve the project! If you would like to contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m 'Add your message here'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.


## Contact

For questions or support, please reach out:

- **Author**: Uzzal Mia
- **Email**: uzzal.cse42@gmail.com 
- **GitHub**: [uzzalcse](https://github.com/uzzalcse)
