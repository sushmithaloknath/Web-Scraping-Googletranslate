from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Google Translate
driver.get("https://translate.google.com/")
time.sleep(3)

# Select the source language (Kannada)
source_lang_button = driver.find_element(By.XPATH, "//button[@aria-label='More source languages']")
source_lang_button.click()
time.sleep(2)

kannada_option = driver.find_element(By.XPATH, "//div[text()='Kannada']")
kannada_option.click()
time.sleep(2)

# Enter Kannada text
source_input = driver.find_element(By.XPATH, "//textarea[@aria-label='Source text']")
source_input.send_keys("ನೀವು ಹೇಗಿದ್ದೀರಾ?")  # "How are you?" in Kannada

time.sleep(3)  # Wait for translation

# Get the translated output
translated_text = driver.find_element(By.XPATH, "//span[@class='HwtZe']")
print("✅ Translated Text:", translated_text.text)

# Close browser
time.sleep(5)
driver.quit()
