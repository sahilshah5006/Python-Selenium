from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()


def search_product(driver, search_query):
    try:
        #Open Amazon.in
        driver.get("https://www.amazon.in")
        time.sleep(2)

        #Find the search bar and enter the query
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        #Wait for the search results to load
        time.sleep(3)
        print("PASS: Search results loaded successfully.")
        return True
    except Exception as e:
        print(f"FAIL: Search operation failed. Error: {e}")
        return False

def gotpprodpage(driver):
    product = driver.find_element(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
    product_title = product.find_element(By.CSS_SELECTOR, "h2 a").text.strip()
    product.find_element(By.CSS_SELECTOR, "h2 a").click()
    time.sleep(3)  # Allow the details page to load
    product_price = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text.strip()
    print(f"Product name:{product_title}")
    print(f"Product price:{product_price}")
    time.sleep(3)  # Wait for the product to be added to the cart

    try:
        add_to_cart_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-button"]'))
        )

        # Scroll into view if necessary
        driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)

        # Click the button
        add_to_cart_button.click()
        print("PASS: 'Add to Cart' button clicked successfully.")
    except Exception as e:
        print(f"FAIL: Unable to click 'Add to Cart' button. Error: {e}")

search_passed = search_product(driver, "Laptop")
gotpprodpage(driver)
input("Press Enter to close the browser...")  # Keep browser open for manual inspection
driver.quit()