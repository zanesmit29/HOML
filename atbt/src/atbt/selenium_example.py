from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# Finding elements on a page
#browser.get('https://inventwithpython.com')
# elems = browser.find_elements(By.CSS_SELECTOR, 'p') #gets a list of the p elements within the URL
# print(elems[0].text)

# Clicking elements on a page
# browser.get('https://automatetheboringstuff.com/example3.html')
# link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
# type(link_elem)
# link_elem.click()

# Filling out and submitting forms
# browser.get('https://automatetheboringstuff.com/example3.html')
# user_elem = browser.find_element(By.ID, 'login_user')
# user_elem.send_keys('your_real_user_name')
# password_elem = browser.find_element(By.ID, 'login_pass')
# password_elem.send_keys('your_real_password_here')
# password_elem.submit() # This will do the same as clicking the submit button 

# Sending special keys
browser.get('https://nostarch.com')
html_elem = browser.find_element(By.TAG_NAME, 'html')
html_elem.send_keys(Keys.END) # Scrolls to the bottom
html_elem.send_keys(Keys.HOME) # Scrolls to top

