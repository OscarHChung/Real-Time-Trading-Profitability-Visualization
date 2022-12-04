import option
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions();
options.add_argument('headless');
options.add_argument('window-size=1200x600');
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))

driver = webdriver.Chrome(options=options)
driver.get('https://www.nasdaq.com/market-activity/most-active')
html = driver.page_source
soup = BeautifulSoup(html, features="html5lib")
most_active_list = soup.find("tbody", {"class": "most-active__body"})


def print_page_data(lyst):
    counter = 0
    max_rows = 10
    for row in lyst:
        if max_rows == 0:
            break
        title = row.find("a", {"class": "firstCell"}).getText()
        change = row.select_one(":nth-child(4)").getText()
        counter += 1

        spaces_num = 10
        if max_rows == 1:
            spaces_num -= 1
        spaces = (spaces_num - len(title)) * " "

        print(str(counter) + ". " + title + spaces + change)
        max_rows -= 1


if __name__ == '__main__':
    print_page_data(most_active_list)
