from typing import Counter
from requests.models import CONTENT_CHUNK_SIZE, iter_slices
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import os
from urllib.parse import urlparse

class Bot:

    links = []

    def __init__(self, file_type, username, password, page):
        self.username = username
        self.password = password
        self.page = page

        self.login_by_xpath(username, password)
        sleep(2)
        # go to page
        self.go_to_page(page, file_type)

    def login_by_xpath(self, username, password):

        print(username, password)

        self.driver = webdriver.Chrome("D:/Servers dj/insta_scraping/driver/chromedriver.exe")
        self.driver.get('https://instagram.com/')
        sleep(5)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        
        sleep(3)

        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)

        sleep(3)

# /html/body/div[4]/div/div/button[1]
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept All')]").click() # clicking 'not now btn'


        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(8)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click() # clicking 'not now btn'
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click() 

    def go_to_page(self, page, file_type):
        print("Now we are here")


        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        
        if file_type == "video":

            self.driver.get(f"https://www.instagram.com/{page}/channel")

            sleep(2)
            
            links = self.driver.find_elements_by_tag_name("a")

            def condition(links):
                link =  ".com/tv/" in links.get_attribute('href')
                return link

            valid_video_links = list(filter(condition, links))


            for i in range(len(valid_video_links)):
                link = valid_video_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

            for link in self.links:
                self.driver.get(link)
                video = self.driver.find_element_by_tag_name('video')
                url = video.get_attribute('src')
                base_url = urlparse(url).path
                filename = os.path.basename(base_url)
                filepath = os.path.join(data_dir, filename)

                if os.path.exists(filepath):
                    continue
                with requests.get(url, stream=True) as r:
                    try:
                        r.raise_for_status()
                    except:
                        continue
                    with open(filepath, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)

        else:
            self.driver.get(f"https://www.instagram.com/{page}")

            sleep(2)

            links = self.driver.find_elements_by_tag_name("a")

            def condition(links):
                return ".com/p/" in links.get_attribute("href")
            
            valid_post_links = list(filter(condition, links))

            for i in range(len(valid_post_links)):
                link = valid_post_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

            for link in self.links:
                self.driver.get(link)
                img = self.driver.find_element_by_tag_name('img')
                url = img.get_attribute('src')
                base_url = urlparse(url).path
                filename = os.path.basename(base_url)
                filepath = os.path.join(data_dir, filename)

                if os.path.exists(filepath):
                    continue
                with requests.get(url, stream=True) as r:
                    try:
                        r.raise_for_status()
                    except:
                        continue
                    with open(filepath, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)


    def login(self, username, password):
        self.driver = webdriver.Chrome("D:/Servers dj/insta_scraping/chromedriver.exe")
        self.driver.get('https://instagram.com/')
        sleep(5)

        #target username
        username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

        #enter username and password
        # username.clear()
        username.send_keys(username)
        # password.clear()
        password.send_keys(password)

        #target the login button and click it
        button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


def main():
    # Choose post or video
    my_bot = Bot('post')

if __name__ == '__main__':
    main()
