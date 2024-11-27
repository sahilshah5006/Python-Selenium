Amazon Product Search and Details Fetcher with Selenium
This Python script automates searching for products on Amazon India (amazon.in), retrieving basic details (title and price), and navigating to product pages.

Prerequisites
Python (version 3.x)
Selenium (pip install selenium)
Chrome WebDriver (compatible with your Chrome version): Download from ChromeDriver download page

Script Functionality

Search for Products:
Opens Amazon India and searches based on a user-provided query (e.g., "laptop").
Validates successful search results loading.

Fetch Product Details:
Extracts title and price of the first three products displayed on the search page.
Validates successful extraction of both title and price.

Navigate to Product Page:
Clicks on the first three product links.
Navigates to the product page for each and validates successful switching.
Closes the product page tab and returns to the search results.

Logging and Error Handling:
Logs each step with success/failure messages for better tracking.
Includes error handling to capture and log any issues during execution.


Getting Started
Install Dependencies:

Bash
pip install selenium

Configure WebDriver Path:


Python

Run the Script:

Save the script as amazonTestCase.py (or any preferred name).

Open a terminal, navigate to the script's directory, and run:

Bash
python amazonTestCase.py

Expected Output:

Each step will be logged with success/failure messages.
Product details (title and price) will be displayed if extraction is successful.
This restructured README.md provides a clearer overview, separates functionality, and includes important notes about usage and potential issues.
