from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import sys

def test_scores_service(app_url):
    """
    Test the web service by checking if the score is a number between 1 and 1000.
    :param app_url: URL of the web service
    :return: True if the score is valid, False otherwise
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Use the Chromium binary
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    # Initialize the Chrome WebDriver with headless options
    driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)

    driver.get(app_url)

    score_element = driver.find_element(By.ID, 'score')
    score_text = score_element.text

    score = int(score_text)

    driver.quit()

    return 1 <= score <= 1000

def main_function(url):
    """
    Main function to call the test_scores_service function.
    :param url: URL of the web service
    :return: -1 if the test fails, 0 if it passes.
    """

    if test_scores_service(url):
        sys.exit(0)
    else:
        sys.exit(-1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        service_url = sys.argv[1]
    else:
        service_url = "http://localhost:8777"

    main_function(service_url)

