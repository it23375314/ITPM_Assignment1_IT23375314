# Sinhala Transliteration Testing Automation

## Student

IT23375314


## Project Description

This project automates testing of a Sinhala transliteration web application using Python and Playwright.

The automation script:

* Reads Singlish test inputs from an Excel file
* Sends inputs to the transliteration website
* Captures Sinhala output
* Compares expected vs actual results
* Automatically marks test cases as Pass or Fail


## Features

* Reads test cases from Excel
* Handles Singlish inputs (short, medium, long)
* Supports punctuation, emojis, and mixed English words
* Captures Sinhala transliteration output
* Compares expected vs actual results
* Updates Excel file automatically
* Generates Pass/Fail status for each test case


## Requirements

Make sure the following are installed:

* Python 3.x
* Google Chrome browser
* Internet connection


## Install Dependencies

Open Terminal (Mac) and run:

```bash
pip3 install playwright openpyxl
```

---

## Install Playwright Browsers

```bash
playwright install
```

> If this step fails, the script will automatically use your system Google Chrome.


## How to Run the Automation

Navigate to your project folder:

```bash
cd ITPM_Assignment1_IT23375314
```

Run the script:

```bash
python3 test_automation.py
```


## Input File

The automation uses the following Excel file:

```
Assignment 1 - Test cases.xlsx
```


## Output

After execution:

* **Actual output** column is updated
* **Status** column is updated (Pass / Fail)
* File is saved automatically after each test case


## Project Structure

```
ITPM_Assignment1_IT23375314/
--test_automation.py
--Assignment 1 - Test cases.xlsx
--README.md
```


## Notes

* Ensure stable internet connection
* Do not close the browser while automation is running
* Some test cases are expected to fail intentionally (edge cases)
* The script uses Google Chrome for automation


## Conclusion

This project successfully demonstrates automated testing of Sinhala transliteration using Playwright and Python, covering multiple Singlish input variations and validating system behavior through structured test cases.

