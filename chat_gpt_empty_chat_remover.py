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
    except TimeoutException:
        print(f'Name "{name}" not found by method By.{find_by}')

def prepare_chats(chats):
    for chat in chats:
        if chat.text == 'New chat':
            print(40*'x')
        else:
            print(chat.text)

if __name__ == "__main__":
    pc_username = get_pc_username()
    driver = set_up_chrome(pc_username)
    driver.get("https://chat.openai.com/")

    wait_for_element(driver, 'TAG_NAME', 'li')
    chats_list = driver.find_element(By.TAG_NAME, 'ol')
    chats = chats_list.find_elements(By.TAG_NAME, 'a')
    prepare_chats(chats)
    print(80*'-')
    input(f"""If you don't see above a list with chats from today and a lot of 'x' in places where was a "New chat",
        please press Ctrl + C and review the code / html elements in your webrowser, 
            if everything is good scroll down all chats on the webrowses for load.
      If everything is ready and all chats was load please press ENTER and just wait""")
    chats_lists = driver.find_elements(By.TAG_NAME, 'ol')
    for i in range (0, len(chats_lists)-1):
        chats = chats_lists[i].find_elements(By.TAG_NAME, 'a')
        prepare_chats(chats)
    input()
