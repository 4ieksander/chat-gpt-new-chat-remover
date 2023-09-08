from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from sys import argv
from time import sleep

def get_pc_username_and_empty_chat():
    if len(argv) != 3:
        print("\ttype your username of PC in second parameter and name_of_empty_chat in third")
        print("example: python chat_gpt_empty_chat_remover.py [username] [name_of_empty_chat]")
        exit(999)
    username_and_chat = (argv[1], argv[2])
    return username_and_chat


def set_up_chrome(pc_username):
    chrome_options = Options()
    chrome_options.add_argument(
        f"--user-data-dir=C:\\Users\\{pc_username}\\AppData\\Local\\Google\\Chrome\\User Data"
    )
    return webdriver.Chrome(options=chrome_options)


def wait_for_element(driver, find_by, name):
    find_by_map = {
        'css_selector': By.CSS_SELECTOR,
        'tag_name': By.TAG_NAME,
        'xpath': By.XPATH
    }
    
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_element_located((find_by_map.get(find_by), name)))
        print(f'Name "{name}" found by method By.{find_by}')
        sleep(0.2)
    except TimeoutException:
        driver.click()
        print(f'Name "{name}" not found by method By.{find_by}')
        sleep(3)


def prepare_chats(chats, name_of_empty_chat, delete_empty_chat = False):
    for chat in chats:
        if chat.text == name_of_empty_chat:
            print(40*'x')
            if delete_empty_chat:
                delete_chat(chat)
        else:
            print(chat.text)


def delete_chat(chat):
    sleep(0.1)
    chat.click()
    wait_for_element(chat, 'tag_name', 'button')
    sleep(0.1)
    buttons = chat.find_elements(By.TAG_NAME, 'button')
    try:
        buttons[1].click() # icone bin
    except IndexError:
        return
    wait_for_element(chat, 'xpath', '//div[text()="Delete"]')
    try:
        chat.find_element(By.XPATH, '//div[text()="Delete"]').click()
    except:
        sleep(2)
        chat.find_element(By.XPATH, '//div[text()="Delete"]').click()
    sleep(3)


if __name__ == "__main__":
    pc_username, name_of_empty_chat = get_pc_username_and_empty_chat()
    driver = set_up_chrome(pc_username)
    driver.get("https://chat.openai.com/")

    wait_for_element(driver, 'css_selector', 'div[data-projection-id="3"]')
    chats_list = driver.find_element(By.TAG_NAME, 'ol')
    chats = chats_list.find_elements(By.TAG_NAME, 'a')
    prepare_chats(chats, name_of_empty_chat)
    print(80*'-')
    input(f"""If you don't see above a list with chats from today and a lot of 'x' in places where was a {name_of_empty_chat},
        please press Ctrl + C and review the code / html elements in your webrowser, 
            if everything is good scroll down all chats on the webrowses for load.
      If everything is ready and all chats was load please press ENTER and just wait""")
    
    chats_lists = driver.find_elements(By.TAG_NAME, 'ol')
    for i in range (0, len(chats_lists)-1):
        try:
            chats = chats_lists[i].find_elements(By.TAG_NAME, 'a')
            prepare_chats(chats, name_of_empty_chat, delete_empty_chat = True)
            print('error occured in main module')
        except:
            sleep(10)
            chats = chats_lists[i].find_elements(By.TAG_NAME, 'a')
            prepare_chats(chats, name_of_empty_chat, delete_empty_chat = True)
    input()
