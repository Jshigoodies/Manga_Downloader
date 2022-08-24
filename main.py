from selenium import webdriver
from download import Download
PATH = "chromedriver_win32\chromeDriver.exe"
driver = webdriver.Chrome(PATH)
import os
dl = Download(driver)

while True:
    try:
        print("0. Quit\n1. MangaLife\n2. H-word")
        num = input()
        if int(num) == 0:
            driver.quit()
            exit(0)
        elif int(num) == 1:
            print("Enter Manga Link: ")
            download_link = ""
            download_link = input()
            driver.get(download_link)
            print(driver.title)
            dl.showChapters()
            driver.implicitly_wait(10)  # slow the fk down

            folder = driver.title
            folder = folder.replace(' ', '_')
            folder = folder.replace('|', '_')
            os.mkdir(folder)
            dl.imgSave(download_link, title=folder)
        elif int(num) == 2:
            print("Enter Hentai Link: ")
            download_link = ""
            download_link = input()
            driver.get(download_link)
            print(driver.title)
    except Exception as e:
        print(e.__str__())