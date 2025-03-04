from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sys

def test_scores_service(app_url):
    """
    Test the web service by checking if the score is a number between 1 and 1000.
    :param app_url: URL of the web service
    :return: True if the score is valid, False otherwise
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

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
    if url is None:
        url = "http://localhost:8777"

    if test_scores_service(url):
        print("Test passed!")
        sys.exit(0)
    else:
        print("Test failed!")
        sys.exit(-1)

if __name__ == "__main__":
    service_url = None
    main_function(service_url)

