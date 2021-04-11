import time
from selenium import webdriver

driver = webdriver.Firefox()
print('Please open the video playing page')
input('if the video is playing, please press enter:')
while True:
    try:
        driver.find_element_by_link_text('继续')
    except:
        print('继续弹窗还没出现')
        time.sleep(8)