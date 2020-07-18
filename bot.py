from selenium import webdriver
from time import sleep
from secrets import pwd
from selenium.webdriver.common.keys import Keys
from random import randint


class Bot():

    links = []

    comments = [
        'good one!', 'Awesome!'
    ]

    accounts = [
        'w.innie.c', 'thebestofphoto'
    ]

    def __init__(self):
        self.login('negoen')
        #self.like_comment_by_hashtag('minimalist')
        self.comment_on_account()

    def login(self, username):
        self.driver = webdriver.Chrome(executable_path= "/Users/tenzin/Downloads/chromedriver-2")
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        username_input = self.driver.find_element_by_xpath(
            "//input[@name='username']")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath(
            "//input[@name='password']")
        password_input.send_keys(pwd)
        login_btn = self.driver.find_element_by_xpath(
            "//button[@type='submit']")
        login_btn.click()
        sleep(2)
        save_login_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        save_login_info.click()
        sleep(2)
        turn_on_notifications = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        turn_on_notifications.click()
        sleep(2)
        # try:
        #     self.driver.find_element_by_xpath(
        #         '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        # except:
        #     pass
        # try:
        #     self.driver.find_element_by_xpath(
        #         '/html/body/div[4]/div/div/div[3]/button[2]').click()
        # except:
        #     pass

    def comment_on_account(self):
        for account in self.accounts:
            # get to profile page
            self.driver.get('https://www.instagram.com/{}/'.format(account))
    #         # get most recent photo
            links = self.driver.find_elements_by_tag_name('a')

            def condition(link):
                return '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))
            last_photo_url = valid_links[0].get_attribute('href')
            self.driver.get(last_photo_url)
            # comment on the photo
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            self.driver.find_element_by_xpath(
                "//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0, 1)])
            sleep(2)
            self.driver.find_element_by_xpath(
                "//button[@type='submit']").click()
            sleep(2)

    def like_comment_by_hashtag(self, hashtag):
        search_box = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        search_box.send_keys('#' + hashtag)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').send_keys(Keys.ENTER)
        sleep(2)

        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)

            # like
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').send_keys(Keys.ENTER)
            sleep(2)

            # comment
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            self.driver.find_element_by_xpath(
                "//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0, 1)])
            sleep(2)
            self.driver.find_element_by_xpath(
                "//button[@type='submit']").click()
            sleep(2)


def main():
    my_bot = Bot()


if __name__ == '__main__':
    main()
