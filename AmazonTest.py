from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait

email = 'angealhelwey@gmail.com'
password = '12801988'
url = 'https://www.amazon.com/'
chrome = webdriver.Chrome()
chrome.get(url)

if url == chrome.current_url:
    print('You are in home page')

chrome.find_element_by_id('nav-link-accountList').click()
chrome.find_element_by_id('ap_email').send_keys(email)
chrome.find_element_by_id('continue').click()
chrome.find_element_by_id('ap_password').send_keys(password)
chrome.find_element_by_id('signInSubmit').click()

chrome.find_element_by_xpath('//input[@name="field-keywords"]').send_keys('samsung')
chrome.find_element_by_xpath('//div[@class="nav-search-submit nav-sprite"]').click()
results = chrome.find_element_by_id('s-result-count').text

if results.split('"')[1] == 'samsung':
    print('Results for Samsung')
else:
    print('Results for ' + results.split('"')[1])

current_page = chrome.find_element_by_xpath('//span[@class="pagnLink"]/a').text
chrome.find_element_by_xpath('//span[@class="pagnLink"]').click()

if current_page == '2':
    print('You are in second page')
else:
    print('You are in ' + current_page)

product_name = chrome.find_element_by_xpath('//li[@id][3]//h2').text
chrome.find_element_by_xpath('//li[@id][3]//h2').click()
chrome.find_element_by_id('wishListDropDown').click()
wait.WebDriverWait(chrome, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//span[@class="a-size-small atwl-hz-dd-list-name a-nowrap"]')))
list_name = chrome.find_element_by_xpath('//span[@class="a-size-small atwl-hz-dd-list-name a-nowrap"]').text

if list_name == 'Shopping List':
    chrome.find_element_by_xpath('//div[@id="atwl-popover-inner"]//li[2]').click()
else:
    chrome.find_element_by_xpath('//div[@id="atwl-popover-inner"]//li').click()

wait.WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.ID, 'WLHUC_continue')))
wish_product_name = chrome.find_element_by_xpath('//ul[@class="w-product"]//a').text

if wish_product_name == product_name:
    print('Current Product')

chrome.find_element_by_id('WLHUC_continue').click()
element_hover = chrome.find_element_by_id('nav-link-accountList')
hover = ActionChains(chrome).move_to_element(element_hover)
hover.perform()
wait.WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="nav-flyout-wl-items"]//a[2]')))
chrome.find_element_by_xpath('//div[@id="nav-flyout-wl-items"]//a[2]').click()

while True:
    line_number = 1
    line_name = chrome.find_element_by_xpath('//ul[@id="g-items"]/li[' + str(line_number) + ']//h3/a').text
    if line_name == product_name:
        break
    else:
        line_name += 1
chrome.find_element_by_xpath(
    '//ul[@id="g-items"]/li[' + str(line_number) + ']//input[@name="submit.deleteItem"]').click()
wait.WebDriverWait(chrome, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//li[1]//span[@id="undo-delete"]')))
alert_message = chrome.find_element_by_xpath('//ul/li[' + str(line_number) + ']//div[@class="a-alert-content"]').text
if 'Deleted' == alert_message:
    print(alert_message + ' In Favorite \nProduct name : ' + product_name)
else:
    print('Warning' + alert_message)

chrome.close()
