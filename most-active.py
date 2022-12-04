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
driver.get('https://www.tradingview.com/markets/stocks-usa/market-movers-active/')
html = driver.page_source
soup = BeautifulSoup(html, features="html5lib")
most_active_list = soup.findAll("tr", {"class": "row-EdyDtqqh listRow"})


def print_page_data(lyst):
    counter = 0
    positive_counter = 0
    negative_counter = 0
    neutral_counter = 0

    for row in lyst:
        title = row.find("a", {"class": "apply-common-tooltip tickerNameBox-hMpTPJiS tickerName-hMpTPJiS"}).getText()
        if (row.find("span", {"class": "positive-C2C2Vilj"}) is None) and (row.find("span", {"class": "negative-C2C2Vilj"}) is None):
            change = "0.00%"
            neutral_counter += 1
        elif row.find("span", {"class": "negative-C2C2Vilj"}) is None:
            change = "+" + row.find("span", {"class": "positive-C2C2Vilj"}).getText()
            positive_counter += 1
        else:
            change = row.find("span", {"class": "negative-C2C2Vilj"}).getText()
            negative_counter += 1
        counter += 1

        spaces_num = 10
        spaces = (spaces_num - len(title)) * " "

        print(str(counter) + ". " + title + spaces + change)
        if counter == 100:
            print("Positive Stocks: " + str(positive_counter))
            print("Negative Stocks: " + str(negative_counter))
            print("Neutral Stocks: " + str(neutral_counter))


if __name__ == '__main__':
    print_page_data(most_active_list)
