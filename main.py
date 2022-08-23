from selenium import webdriver
from download import Download
PATH = "chromedriver_win32\chromeDriver.exe"
driver = webdriver.Chrome(PATH)

dl = Download(driver)

while True:
    try:
        print("0. Quit\n1. MangaLife")
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
            dl.imgSave(download_link)
    except Exception as e:
        print(e.__str__())