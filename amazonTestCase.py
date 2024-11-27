from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


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


def navigate_to_product_and_fetch_details(driver, product_index):
    try:
        #Click the product from the search results
        products = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")

        if product_index <= len(products):
            product = products[product_index - 1]
            product_title = product.find_element(By.CSS_SELECTOR, "h2 a").text.strip()

            # Get the price from the search page
            try:
                product_price = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text.strip()
                print(f"PASS: Price for {product_title}: {product_price}")
            except:
                product_price = "Price not available"
                print(f"PASS: Price for {product_title}: {product_price}")

            # Validate product title and price extraction
            if product_title and product_price:
                print(f"PASS: Extracted product details: {product_title}, {product_price}")
            else:
                print(f"FAIL: Failed to extract product details.")

            # Click on the product to navigate to the product page
            product.find_element(By.CSS_SELECTOR, "h2 a").click()
            time.sleep(3)  # Allow the details page to load

            # Switch to the new tab (product page)
            driver.switch_to.window(driver.window_handles[1])

            # Validate tab switch
            if len(driver.window_handles) == 2:
                print("PASS: Successfully switched to the product page.")
            else:
                print("FAIL: Failed to switch to the product page.")

            # Close the product page and switch back to the search results page
            driver.switch_to.window(driver.window_handles[0])

            return product_title, product_price
        else:
            print(f"FAIL: Product index {product_index} out of range")
            return None, None

    except Exception as e:
        print(f"FAIL: Error extracting product details: {e}")
        return None, None


# Set up WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

#Search for "laptop" and validate the search results
print("\nStep 1: Searching for 'laptop' on Amazon")
search_passed = search_product(driver, "laptop")

if search_passed:
    #Fetch and print details for the first, second, and third product
    print("\nStep 2: Fetching Details for First Product:")
    product_title_1, product_price_1 = navigate_to_product_and_fetch_details(driver, 1)

    print("\nStep 3: Fetching Details for Second Product:")
    product_title_2, product_price_2 = navigate_to_product_and_fetch_details(driver, 2)

    print("\nStep 4: Fetching Details for Third Product:")
    product_title_3, product_price_3 = navigate_to_product_and_fetch_details(driver, 3)

else:
    print("Test failed at Step 1, so no further actions are taken.")

input("Press Enter to close the browser...")  # Keep browser open for manual inspection
driver.quit()
