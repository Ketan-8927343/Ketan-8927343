from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the LinkedIn login page
driver.get("https://www.linkedin.com/login")
time.sleep(3)

# Finding the email and password input fields
email_field = driver.find_element("id", "username")
password_field = driver.find_element("id", "password")

# Entering the email and password
email_field.send_keys("ketan95744@gmail.com")
password_field.send_keys("Ketan@6800")

# Submitting the login form
password_field.send_keys(Keys.RETURN)

# Waiting for the home page to load
time.sleep(5)

# Verifying that the login was successful
assert "LinkedIn" in driver.title

# Searching for a connection
search_bar = driver.find_element("class name", "search-global-typeahead__input")
search_bar.send_keys("John Doe")
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Clicking on a search result
search_result = driver.find_element("class name", "search-result__result-link")
search_result.click()

# Waiting for the profile page to load
time.sleep(5)

# Sending a message to the connection
message_button = driver.find_element("class name", "message-anywhere-button")
message_button.click()

# Typing the message
message_input = driver.find_element("class name", "msg-form__contenteditable")
message_input.send_keys("Hello, John! How are you?")

# Sending the message
send_button = driver.find_element("class name", "msg-form__send-button")
send_button.click()

# Waiting for the message to be sent
time.sleep(5)

# Closing the webdriver
driver.close()