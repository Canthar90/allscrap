from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time



def search(search_word, search_number=1, by_pricve=False):
    '''this function will search the search_word and retutrn message containing selected search_number of
    search reasults '''
    driver.get("https://allegro.pl")

    time.sleep(1)
    action.key_down(Keys.ENTER)
    action.key_up(Keys.ENTER)
    action.perform()

    time.sleep(1)
    search_pole = driver.find_element(
        By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div/div[3]/header/div/div/div/div/form/input")

    action.click(on_element=search_pole)
    action.send_keys(search_word)
    action.key_down(Keys.ENTER)
    action.key_up(Keys.ENTER)
    action.perform()

    if by_pricve:
        time.sleep(1)
        sorting_selector = driver.find_element(
            By.XPATH, """/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[3]/div[3]/div/div/div/select""")

        action.click(on_element=sorting_selector)
        action.key_down(Keys.ARROW_DOWN)
        action.key_up(Keys.ARROW_DOWN)
        action.key_down(Keys.ENTER)
        action.key_up(Keys.ENTER)
        action.perform()

    time.sleep(1)

    main_titles = driver.find_elements(
        By.XPATH,
        """/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[5]/div/div/div[1]/div[2]/div/section[2]
        /article[5]/div/div[2]/div[1]/h2/a"""
    )

    main_prices = driver.find_elements(
        By.XPATH,
        """/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[5]/div/div/div[1]/div[2]/div/section[2]
        /article[4]/div/div[2]/div[2]/div/div/span"""
    )
    print(len(main_titles))
    if len(main_titles) == 0:
        print('Sory nie mogę znaleźć wyników dla tego zapytania')
    else:
        message = ''

        print(f"pierwszy tytuł to  {main_titles[0].text}\n  Pierwsza cena to {main_prices[0].text}\n"
            f"first link is {main_titles[0].get_attribute('href')}")




fraze = input("Plis input fraze to be searched in format: !asearch, searched_word (nessesary), \n"
              "number of results(optional) ,by_price(optional) True if you wanna to sort results by the cheapest \n"
              "For example it should look like : !asearch, kopytko, 5, True")

if '!asearch' in fraze:
    fraze = fraze.split(',')
    fraze = [elem.strip() for elem in fraze]
    print(fraze)
    chrome_driver = "./chromedriver/chromedriver.exe"
    s = Service(chrome_driver)
    options = ChromeOptions()
    driver = webdriver.Chrome(service=s, options=options)
    action = ActionChains(driver=driver)
    if len(fraze) == 2:
        search(search_word=fraze[1])
    elif len(fraze) == 3:
        search(search_word=fraze[1], search_number=fraze[2])
    elif len(fraze) == 4:
        search(search_word=fraze[1], search_number=fraze[2], by_pricve=fraze[3])
else:
    print("Prowidet statment is invalid")


