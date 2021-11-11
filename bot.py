from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from secret import pw

class Bot:

    links = []

    def __init__(self):
        self.login_by_xpath('rezaizadi_ij', pw)
        # self.login('rezaizadi_ij', pw)

        sleep(2)

        # go to page
        self.go_to_page('')

    def login_by_xpath(self, username, password):
        self.driver = webdriver.Chrome("D:/Servers dj/insta_scraping/chromedriver.exe")
        self.driver.get('https://instagram.com/')
        sleep(5)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        
        sleep(1)

        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)

        sleep(1)

# /html/body/div[4]/div/div/button[1]
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept All')]").click() # clicking 'not now btn'


        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click() # clicking 'not now btn'
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click() 
        # sleep(3)
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

        # sleep(3)

        # page = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        # page.send_keys('deutsch_cafe_a1_b1')



    def go_to_page(self, page):
        print("Now we are here")

        self.driver.get(f"https://www.instagram.com/{page}/channel")

        sleep(2)
        
        all_videos_links = self.driver.find_element_by_tag_name("a")

        def condition(links):
            return ".com/tv" in links.get_attribute('href')

        valid_video_links = list(filter(condition, all_videos_links))

        for i in range(9):
            link = valid_video_links[i].get_attribute('href')
            if link not in self.all_videos_links:
                self.valid_video_links.append(link)

        print(len(valid_video_links))
        print("all the href are", valid_video_links)
        # for link in all_videos_links:
        #     self.get(link)



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
    my_bot = Bot()

if __name__ == '__main__':
    main()