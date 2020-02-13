from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class IgBot:
    comments_text = [
        'Dope!', 'This is fantastic!', 'Awesome!',
        '100%', 'Sickk beats', 'Great job', 'Well done!', 'Your posts are amazing',
    ]

    def __init__(self, username, password):
        self.driver = webdriver.Chrome('./../chromedriver.exe')
        self.username = username
        self.password = password


    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(1)
        username_input = driver.find_element_by_xpath("//input[@aria-label='Phone number, username, or email']")
        password_input = driver.find_element_by_xpath("//input[@aria-label='Password']")

        username_input.clear()
        username_input.send_keys(self.username)

        password_input.clear()
        password_input.send_keys(self.password)

        try:
            login_btn = driver.find_element_by_xpath('//button[@type="submit"]')
            login_btn.click()
            time.sleep(2)
        except:
            print('Error logging in')


    def likes(self, hashtag, scrollDepth=0):
        driver = self.driver
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(2)
        for i in range(scrollDepth):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)

        elements = driver.find_elements_by_class_name('_9AhH0')

        ##Will only like a maximum of 5 photos
        ###wraped in a new function?
        max_num = None
        if len(elements) > 50:
            max_num = 50
        else:
            max_num = len(elements)
        ###


        for i in range(max_num):
            sleeptime = random.randint(18, 28)
            time.sleep(sleeptime)
            elem = elements[i]
            elem.click()
            time.sleep(1)
            like_button = driver.find_element_by_css_selector('.fr66n .wpO6b')
            like_button.click()
            time.sleep(1)
            driver.back()
            time.sleep(random.randint(1,8))


    def comments(self, hashtag, scrollDepth=0):
        driver = self.driver
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(2)

        for i in range(scrollDepth):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)

        elements = driver.find_elements_by_css_selector('.Nnq7C .v1Nh3 a')
        hrefs = [elem.get_attribute('href') for elem in elements]
        hrefs = [link for link in hrefs if '/p/' in link]

        ##Will only like a maximum of 5 photos
        ###wraped in a new function?
        max_num = None
        if len(elements) > 50:
            max_num = 50
        else:
            max_num = len(elements)
        #

        for i in range(max_num):
            sleeptime = random.randint(18, 28)
            time.sleep(sleeptime)
            time.sleep
            href = hrefs[i]
            driver.get(href)
            time.sleep(2)
            comment_input = lambda : driver.find_element_by_tag_name('textarea')
            comment_input().click()
            comment_input().clear()
            time.sleep(1)

            comment  = random.choice(self.comments_text)
            for letter in comment:
                comment_input().send_keys(letter)
                delay = random.randint(1, 7) / 30
                time.sleep(delay)

            comment_input().send_keys(Keys.RETURN)


    def get_top_hashtags(self, hashtag):
        driver = self.driver
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(2)
        hrefs = driver.find_elements_by_tag_name('a')
        hrefs = [elem.get_attribute("text") for elem in hrefs]
        hrefs = [item for item in hrefs if '#' in item]

        return hrefs



myBot = IgBot(#Login credentials, #password)
myBot.login()
# myBot.likes('lofi')

# myBot.comments('lofi')

myBot.get_top_hashtags('newyork')












