from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from sys import argv, exc_info
from time import sleep


def get_pc_username():
    if len(argv) != 2:
        print("\ttype your username of PC in second parameter")
        print("example: python chat_gpt_empty_chat_remover.py [username]")
        exit(999)
    return argv[1]


def set_up_chrome(pc_username):
    chrome_options = Options()
    chrome_options.add_argument(
        f"--user-data-dir=C:\\Users\\{pc_username}\\AppData\\Local\\Google\\Chrome\\User Data"
    )
    return webdriver.Chrome(options=chrome_options)


def wait_for_element(driver, find_by, name):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-projection-id="3"]')))
        print(f'Name "{name}" found by method By.{find_by}')
        sleep(1.5)
    except TimeoutException:
        print(f'Name "{name}" not found by method By.{find_by}')


if __name__ == "__main__":
    pc_username = get_pc_username()
    driver = set_up_chrome(pc_username)
    driver.get("https://chat.openai.com/")

    wait_for_element(driver, 'TAG_NAME', 'ol')
    chats_list = driver.find_elements(By.TAG_NAME, 'ol')
    chats = chats_list[0].find_elements(By.TAG_NAME, 'a')
    for chat in chats:
        if chat.text == 'New chat':
            print(40*'-')
        else:
            print(chat.text)
    input()
