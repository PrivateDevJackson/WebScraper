from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def fetch_vehicle_data(registration_number):
    url = "https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej?execution=e4s1"
    
    # Use Selenium to interact with the webpage
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        # Wait for the input field to be present
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'soegeord'))
        )

        # Type the registration number into the input field
        input_field.send_keys(registration_number)

        # Locate and click the submit button
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'fremsoegKtBtn'))
        )
        submit_button.click()

        # Wait for the new page to load
        WebDriverWait(driver, 10).until(EC.url_changes(url))

        # Use BeautifulSoup to parse the HTML content of the new page
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Customize this part based on the structure of the HTML on the website
        # Here, we're trying to extract the text from a specific HTML element
        data_element = soup.find('div', {'class': 'bluebox'})

        if data_element:
            data = data_element.text.strip()
            return data
        else:
            print("Could not find the data element on the page.")
            return None

    finally:
        # Close the browser window
        driver.quit()

def main():
    registration_number = "" # <--- enter your registration number here
    data = fetch_vehicle_data(registration_number)

    if data:
        print(f"Data for vehicle with registration number {registration_number}:\n{data}")

if __name__ == "__main__":
    main()
