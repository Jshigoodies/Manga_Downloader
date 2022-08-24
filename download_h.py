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

class H_word:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.ignored_exceptions = (
            NoSuchElementException, StaleElementReferenceException,)  # This is a solution that a wished i knew earliers