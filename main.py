
import os
import time
try:
    import webdriver_manager
    import selenium
except:
    os.system("pip install selenium webdriver-manager")
import random, threading
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Attributes:
    def __init__(self) -> None:
        self.names = self.__getnames()
        self.loggedIn = 0

    def __read(self, file):
        with open(file, 'r') as f:
            return f.read().splitlines()

    def __getnames(self):
        self.accountlist = self.__read('./names.txt')
        return [account.split('\n')[0] for account in self.accountlist]

    @staticmethod
    def clear():
        os.system('cls')
        print(f"LessonUp.app autojoiner\nMade by NoelP and Sadcat\n-------------------\nUsers: {Attributes().loggedIn}")

    @staticmethod
    def setup():
        options = webdriver.EdgeOptions()
        options.add_argument("--log-level=3")
        options.add_argument('--headless')
        driver = webdriver.Edge(
            EdgeChromiumDriverManager().install(), options=options)
        return driver
    @staticmethod
    def joinuser(driver):
        driver.get(f"https://lessonup.app/?lang=en&code={code}")
        WebDriverWait(driver, 30).until(
            EC.url_contains("https://lessonup.app/player/"))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, 
            "/html/body/div[3]/div/div[3]/div/div[1]/form/input[1]"))).send_keys(f"{player}", Keys.RETURN)
        time.sleep(1)
        driver.quit()
        Attributes().loggedIn += 1
    @staticmethod
    def submit(code, player):
        options = webdriver.EdgeOptions()
        options.add_argument("--log-level=3")
        options.add_argument('--headless')
        driver = webdriver.Edge(
            EdgeChromiumDriverManager().install(), options=options)
        threading.Thread(target=Attributes().joinuser, args=(driver,)).start()

if __name__ == "__main__":
    Attributes.clear()
    code = input("Lessonup code: ")
    for player in Attributes().names:
        Attributes.submit(code,player)
        print(f"Joined with {player}")
        time.sleep(1)
        Attributes.clear()
    print("End of script.")
