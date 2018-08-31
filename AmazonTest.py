import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait

email = 'angealhelwey@gmail.com'
password = '12801988'
url = 'https://www.amazon.com/'
search_key = 'samsung'
chrome = webdriver.Chrome()
chrome.get(url)

if url == chrome.current_url:
    print('You are in home page')
login_link = 'nav-link-accountList'
chrome.find_element_by_id(login_link).click()
mail_area = 'ap_email'
chrome.find_element_by_id(mail_area).send_keys(email)
continue_button = 'continue'
chrome.find_element_by_id(continue_button).click()
password_area = 'ap_password'
chrome.find_element_by_id(password_area).send_keys(password)
singIn_button = 'signInSubmit'
chrome.find_element_by_id(singIn_button).click()
search_area = '//input[@name="field-keywords"]'
chrome.find_element_by_xpath(search_area).send_keys(search_key)
search_button = '//div[@class="nav-search-submit nav-sprite"]'
chrome.find_element_by_xpath(search_button).click()

results_xpath = 's-result-count'
results = chrome.find_element_by_id(results_xpath).text

if results.split('"')[1] == 'samsung':
    print('Results for Samsung')
else:
    print('Results for ' + results.split('"')[1])

page_xpath = '//span[@class="pagnLink"]/a'
page = chrome.find_element_by_xpath(page_xpath).text

if page == '2':
    chrome.find_element_by_xpath('//span[@class="pagnLink"]').click()
else:
    print('You are going to ' + page + 'page')

product_name_xpath = '//li[@id][3]//h2'
product_name = chrome.find_element_by_xpath(product_name_xpath).text

current_url = chrome.current_url.split('page=')[1]
current_page = current_url.split('&')[0]
if current_page == '2':
    print('You are in Second page')
else:
    print('You are in ' + current_page)

chrome.find_element_by_xpath(product_name_xpath).click()
wish_list_xpath = 'wishListDropDown'
chrome.find_element_by_id(wish_list_xpath).click()
list_name_xpath = '//span[@class="a-size-small atwl-hz-dd-list-name a-nowrap"]'
wait.WebDriverWait(chrome, 5).until(
    EC.element_to_be_clickable((By.XPATH, list_name_xpath)))
list_name = chrome.find_element_by_xpath(list_name_xpath).text

if list_name == 'Shopping List':
    drop_down_first_li = '//div[@id="atwl-popover-inner"]//li[2]'
    chrome.find_element_by_xpath(drop_down_first_li).click()
else:
    drop_down_second_li = '//div[@id="atwl-popover-inner"]//li'
    chrome.find_element_by_xpath(drop_down_second_li).click()

continue_page_button = 'WLHUC_continue'
wait.WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.ID, continue_page_button)))
chrome.find_element_by_id(continue_page_button).click()
profile_list_hover_path = 'nav-link-accountList'
profile_list_hover = chrome.find_element_by_id(profile_list_hover_path)
hover = ActionChains(chrome).move_to_element(profile_list_hover)
hover.perform()
profile_list_path = '//div[@id="nav-flyout-wl-items"]//a[2]'
wait.WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.XPATH, profile_list_path)))
chrome.find_element_by_xpath(profile_list_path).click()

line_number = 1
try:
    while True:
        line_xpath = '//ul[@id="g-items"]/li[' + str(line_number) + ']//h3/a'
        line_name = chrome.find_element_by_xpath(line_xpath).text
        if line_name == product_name:
            break
        else:
            line_number = line_number + 1
            if line_number == 12:
                print('Can\'t find product')
                break
                chrome.close()
except Exception as e:
    print('Cant\'t Find product')
    chrome.close()
if product_name == line_name:
    print('Current product.')
else:
    print(product_name)
    print(line_name)
    print('Can\'t find product')

try:
    line_delete_xpath = '//ul[@id="g-items"]/li[' + str(line_number) + ']//input[@name="submit.deleteItem"]'
    chrome.find_element_by_xpath(line_delete_xpath).click()

    undo_xpath = '//li[1]//span[@id="undo-delete"]'
    wait.WebDriverWait(chrome, 5).until(
        EC.element_to_be_clickable((By.XPATH, undo_xpath)))
    alert_message_xpath = '//ul/li[' + str(line_number) + ']//div[@class="a-alert-content"]'
    alert_message = chrome.find_element_by_xpath(alert_message_xpath).text
    if 'Deleted' == alert_message:
        print(alert_message + ' In Favorite \nProduct name : ' + product_name)
    else:
        print('Warning' + alert_message)
except Exception as e:
    alert_message_xpath = '//h4[@class="a-alert-heading"]'
    alert_message = chrome.find_element_by_xpath(alert_message_xpath).text
    print('Deleted Error: ')
    print(e)

chrome.close()
