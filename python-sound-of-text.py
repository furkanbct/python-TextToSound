import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

chrome_options = Options()

chrome_options.add_argument("window-size=0,0")
while True:

    print("""
    [1]TR
    [2]EN
    [3]FR
    [4]DE
    [5]IT
    """)

    dil = int(input("Please Select a Language :"))

    yazı = input("Write the text to be read :")

    print("Please Do Not Close The Window !!!")

    print("Please Wait...")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://soundoftext.com")

    sec = Select(driver.find_element_by_class_name("field__select"))
    if dil == 1:
        sec.select_by_value("tr-TR")
    if dil == 2:
        sec.select_by_value("en-US")
    if dil == 3:
        sec.select_by_value("fr-FR")
    if dil == 4:
        sec.select_by_value("de-DE")
    if dil == 5:
        sec.select_by_value("it-IT")

    driver.find_element_by_name("text").send_keys(yazı)

    driver.find_element_by_css_selector("#app > div:nth-child(1) > div > form > div:nth-child(3) > input").click()

    time.sleep(4)

    driver.find_element_by_css_selector("#app > div.section.section--colored > div > div > div:nth-child(2) > a:nth-child(1)").click()

    download = input("Do You Want To Download Sound File ?(y or n) :")

    if download == "y":
        driver.find_element_by_css_selector("#app > div.section.section--colored > div > div > div.card__actions > a:nth-child(2)").click()
        print("Downloading...")
        time.sleep(5)
        print("Audio File Downloaded To Default Download Location")
        driver.close()
    if download == "n":
        driver.close()
