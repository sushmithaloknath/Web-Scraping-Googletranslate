# Web-Scraping-Googletranslate
# Google Translate Automation with Selenium

This Python script automates Google Translate using Selenium WebDriver. It opens Google Translate, selects Kannada as the source language, inputs Kannada text, and retrieves the English translation.

---

## Features

- Opens [Google Translate](https://translate.google.com/)
- Selects Kannada as the source language
- Inputs Kannada text `"ನೀವು ಹೇಗಿದ್ದೀರಾ?"` ("How are you?")
- Extracts and prints the translated English text
- Closes the browser automatically after completion

---

## Requirements

- Python 3.x
- Selenium
- Chrome browser
- ChromeDriver compatible with your Chrome version (ensure `chromedriver` is in your system PATH)

---

## Installation

1. Install Selenium via pip:
   ```bash
   pip install selenium
