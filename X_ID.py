from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class JQueryDragDrop:
    """Class to automate the drag-and-drop operation on jQuery UI."""
    
    def __init__(self, url):
        """Initialize WebDriver and open the target URL."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Implicit wait for elements to load
    
    def perform_drag_drop(self):
        """Perform drag-and-drop operation."""
        # Switch to the iframe where the elements exist
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))
        
        # Locate draggable and droppable elements using XPath
        source_element = self.driver.find_element(By.XPATH, "//div[@id='draggable']")
        target_element = self.driver.find_element(By.XPATH, "//div[@id='droppable']")
        
        # Perform drag-and-drop action
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()
        
        print("Drag and Drop operation completed successfully!")
    
    def close_browser(self):
        """Close the WebDriver session."""
        self.driver.quit()

# Usage Example
jquery_ui = JQueryDragDrop("https://jqueryui.com/droppable/")
jquery_ui.perform_drag_drop()
jquery_ui.close_browser()
