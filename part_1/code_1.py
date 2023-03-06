from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Instagram_bot():

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.browser = webdriver.Chrome("..\\chromedriver\\chromedriver.exe")

    def browser_close(self):
        

        self.browser.close()
        self.browser.quit()

    def login(self):

        browser = self.browser
        browser.get('https://www.instagram.com/')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

    def like_photo_by_hashtag(self, hashtag):

        browser = self.browser
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(5)

        post_urls = []

        for i in range(1, 6):
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(random.randrange(3, 5))
            hrefs = browser.find_elements(By.TAG_NAME, 'a')

            post_urls = post_urls + [item.get_attribute('href') for item in hrefs if
                                     "/p/" in item.get_attribute('href')]
            print(len(post_urls))

        post_urls = set(post_urls)

        for url in post_urls:
            try:

                browser.get(url)
                time.sleep(5)

                browser.find_element(By.CSS_SELECTOR,
                                     '#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.ltpMr.Slqrh > span.fr66n > button').click()

                time.sleep(random.randrange(1, 10))

            except Exception as ex:
                print(ex)
                browser.close()

    def xpath_exists(self, url):

        browser = self.browser
        try:
            browser.find_element(By.XPATH, url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def put_exactly_like(self, userpost):

        browser = self.browser
        browser.get(userpost)
        time.sleep(4)

        wrong_userpage = '/html/body/div[1]/section/main/div/div/h2'
        if self.xpath_exists(wrong_userpage):
            print("Такого поста не существует")
            browser.close()
        else:
            like_buttom = '#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.ltpMr.Slqrh > span.fr66n > button'
            browser.find_element(By.CSS_SELECTOR, like_buttom).click()
            print("like^)))))))))")
            time.sleep(5)
            self.browser_close()

    def put_like_for_user(self, userpage):

        browser = self.browser
        browser.get(userpage)
        time.sleep(4)

        wrong_userpage = '/html/body/div[1]/section/main/div/div/h2'
        if self.xpath_exists(wrong_userpage):
            print("эррор")
            browser.close()
        else:
            like_buttom = '#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.ltpMr.Slqrh > span.fr66n > button'
            browser.find_element(By.CSS_SELECTOR, like_buttom).click()
            print("not error")
            time.sleep(5)
            self.browser_close()

        post_urls = []
        time.sleep(random.randrange(3, 5))
        hrefs = browser.find_elements(By.TAG_NAME, 'a')
        post_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

        post_urls_set = set(post_urls)
        post_urls = list(post_urls_set)

        file_name = userpage.split("/")[2]

        with open(f"{file_name}.txt", 'a') as file:
            for url in post_urls:
                file.write(url + "\n")

        with open(f'{file_name}.txt') as file:
            post_urls_user = file.readlines()

        for url in post_urls_user[0:4]:
            try:

                browser.get(url)
                time.sleep(5)

                browser.find_element(By.CSS_SELECTOR,
                                     '#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.ltpMr.Slqrh > span.fr66n > button').click()

                time.sleep(random.randrange(1, 10))

            except Exception as ex:
                print(ex)
                browser.close()

    def comment_post(self,url):

        browser = self.browser
        browser.get(url)

        browser.find_element(By.CSS_SELECTOR,'#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.ltpMr.Slqrh > span._15y0l > button').click()
        comment = browser.find_element(By.CSS_SELECTOR,'#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.sH9wk._JgwE > div > form > textarea')
        comment.clear()
        comment.send_keys("cute:3")






