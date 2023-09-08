from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sys import argv


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


if __name__ == "__main__":
    pc_username = get_pc_username()
    driver = set_up_chrome(pc_username)
    driver.get("https://chat.openai.com/")
    input()
