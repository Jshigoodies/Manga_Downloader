from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

import sys, os
import time

class Download:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.ignored_exceptions = (
            NoSuchElementException, StaleElementReferenceException,)  # This is a solution that a wished i knew earlier

    def imgSave(self, website):
        not_done = True
        num = 0
        while not_done:
            num = num + 1
            print("link: " + str(num))
            try: # go to each chapter and flip through pages
                time.sleep(0.5)
                chapter = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/a[' + str(num) + ']')))
                time.sleep(1) # slow the fk down
                chapter.click()

                flip_pages = True
                #########################################
                page_num = 2 # the first page starts at div tag num 2. Idk why.
                while flip_pages:
                    try:
                        # save img
                        time.sleep(1)  # slow the fk down
                        img = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, '//*[@id="TopPage"]/div[' + str(page_num) + ']/div/img')))
                        time.sleep(1)  # slow the fk down
                        current_page = self.driver.current_url
                        source = img.get_attribute('src')
                        time.sleep(1)  # slow the fk down
                        self.driver.get(source)
                        time.sleep(1)  # slow the fk down
                        self.driver.save_screenshot('Chapter_' + str(num) + '_' + str(page_num) + '.png')
                        time.sleep(1)  # slow the fk down
                        self.driver.get(current_page)
                        # flip pages

                        time.sleep(1)  # slow the fk down
                        next = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, '/html/body/nav/div/div[3]/ul[2]/li[3]/a')))
                        time.sleep(1)  # slow the fk down
                        next.click()
                        page_num = page_num + 1
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                        print(e.__str__())
                        flip_pages = False
                        print("done flipping pages")
                # done flipping through pages and downloading them
                #########################################
                time.sleep(1)  # slow the fk down
                self.driver.get(website)
                time.sleep(1)  # slow the fk down
                self.showChapters()
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print(e.__str__())
                print("Done Downloading")

    def showChapters(self):
        try:
            # self.driver.implicitly_wait(5) # page doesn't load fast
            show_all = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div/i')))
            show_all.click()
        except Exception as e:
            print(e.__str__())
            print("could not load all chapters")

        print("showing all chapters")
