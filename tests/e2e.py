from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

def test_scores_service(app_url):
    """
    Test the web service by checking if the score is a number between 1 and 1000.
    :param app_url: URL of the web service
    :return: True if the score is valid, False otherwise
    """

    driver = webdriver.Chrome()
    driver.get(app_url)

    score_element = driver.find_element(By.ID, 'score_element_id')
    score_text = score_element.text

    score = int(score_text)

    driver.quit()

    return 1 <= score <= 1000

def main_function():
    """
    Main function to call the test_scores_service function.
    Returns -1 if the test fails, 0 if it passes.
    """
    app_url = "http://localhost"

    if test_scores_service(app_url):
        print("Test passed!")
        sys.exit(0)
    else:
        print("Test failed!")
        sys.exit(-1)

