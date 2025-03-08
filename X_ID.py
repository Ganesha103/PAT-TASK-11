from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Setup WebDriver
driver = webdriver.Chrome()

# Visit the URL
driver.get('https://jqueryui.com/droppable/')

# Wait until the iframe is loaded (the draggable element is inside an iframe)
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, '.demo-frame'))

# Locate the draggable element (white box) and the droppable element (yellow box)
draggable = driver.find_element(By.ID, 'draggable')
droppable = driver.find_element(By.ID, 'droppable')

# Initialize ActionChains
actions = ActionChains(driver)

# Perform drag and drop
actions.drag_and_drop(draggable, droppable).perform()

# Optionally, pause to see the result
import time
time.sleep(3)

# Close the browser
driver.quit()
