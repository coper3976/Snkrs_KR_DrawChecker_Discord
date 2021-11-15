from selenium import webdriver
import sys, os
from bs4 import BeautifulSoup, element
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import datetime
from discord_hooks import Webhook
import discord


client = discord.Client()
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/93.0.4577.82 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--headless')
# options.add_argument("--window-size = 1920,1080")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--allow-running-insecure-content')
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server = 'direct : //'")
# options.add_argument("--proxy-bypass-list = *")
options.add_argument("--start-maximized") 
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('disable-infobars')

# 디스코드 
def send_embed(name, size, result, img_link, ID):
    # Create embed to send to webhook
    discord_webhook = ''
    if result in "당첨":
        embed = Webhook(discord_webhook, color=65280)
    else:
        result in "미당첨" 
        embed = Webhook(discord_webhook, color=16711680)

    # Set author info
    embed.set_author(icon='https://static-breeze.nike.co.kr/kr/ko_kr/cmsstatic/theme/52/android-icon-36x36.png')

    embed.add_field(name="Account Name", value=ID)    
    embed.add_field(name="Product", value=name)
    embed.add_field(name="Product Code / Size", value=size)
    embed.add_field(name="Result", value=result)
    embed.set_thumbnail(img_link)
    # Set footer
    embed.set_footer(text='@DrawChecker V1.0', icon='https://static-breeze.nike.co.kr/kr/ko_kr/cmsstatic/theme/52/android-icon-36x36.png', ts=True)

    # Send Discord alert
    embed.post()

def send_resultalert(everyone):
    # Create embed to send to webhook
    discord_webhook = ''
    embed = Webhook(discord_webhook)
    embed.add_field(name="Got'em", value=everyone)    
    # Send Discord alert
    embed.post()

def parsing():
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    divs = soup.find_all(class_='order-list')
    for div in divs:
        result = div.find('span', class_="btn-order-detail thedraw").text.strip()
        name = div.find('span', class_="tit").text.strip()
        size = div.find('span', class_="opt").text.strip()

        if result in "당첨":
            print(name, size,"/", result)
        else:
            result in "미당첨" 
            print(name, size,"/", result) 
            
def discord_alert():
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    divs = soup.find_all(class_='order-list')
    divss = soup.find_all(class_='customer-aside mypage pc-only')

    for div in divs:
        everyone = "@everyone"
        result = div.find('span', class_="btn-order-detail thedraw").text.strip()
        name = div.find('span', class_="tit").text.strip()
        size = div.find('span', class_="opt").text.strip()
        img_link = div.find('div', class_='img-wrap').img['src'].strip().replace('?browse', '') 
        for div in divss:
            ID = div.find('div', class_="customer-name").text.strip()
            if result in "당첨":
                send_embed(name, size, result, img_link, ID)
                send_resultalert(everyone)
            elif result in "미당첨" :
                send_embed(name, size, result, img_link, ID)

def loginclick() :
        driver.find_element_by_xpath('/html/body/section/section/div/div/div[2]/div/div[2]/div/button').click()

#계정1
def sendID1():
    xpath = driver.find_element_by_xpath('//*[@id="j_username"]')
    xpath.send_keys("")

    xpath2 = driver.find_element_by_xpath('//*[@id="j_password"]')
    xpath2.send_keys("")
#계정2
def sendID2():
    xpath = driver.find_element_by_xpath('//*[@id="j_username"]')
    xpath.send_keys("")

    xpath2 = driver.find_element_by_xpath('//*[@id="j_password"]')
    xpath2.send_keys("")

    
print("------------------Start Parsing----------")

driver = webdriver.Chrome(r'./chromedriver', options=options)

###############################################################################
print("-----------------계정1--------------------------")

driver.get('https://www.nike.com/kr/ko_kr/account/theDrawList')

sendID1()
loginclick()
time.sleep(1)
discord_alert()
parsing()
time.sleep(2)

driver.get('https://www.nike.com/kr/ko_kr/logout')


print("-----------------계정2--------------------------")

driver.get('https://www.nike.com/kr/ko_kr/account/theDrawList')

sendID2()
loginclick()
time.sleep(1)
discord_alert()
parsing()
time.sleep(2)

driver.quit()
os.system('pause')
