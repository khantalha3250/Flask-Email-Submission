from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Form Data: A dictionary to store field locators and corresponding values
form_data = {
    '//input[@aria-labelledby="i1 i4"]': "Khan Mohd Talha",               # Full Name
    '//input[@aria-labelledby="i6 i9"]': "7456763250",             # Contact Number
    '//input[@aria-labelledby="i11 i14"]': "khanmohdta@gmail.com",  # Email ID
    '//textarea[@aria-labelledby="i16 i19"]': "Opp, Teli Gali, Vijay Nagar, Andheri East, Mumbai, Maharashtra",  # Full Address
    '//input[@aria-labelledby="i21 i24"]': "400053",               # Pin Code
    '//input[@aria-labelledby="i31"]': "19-11-2003",               # Date of Birth
    '//input[@aria-labelledby="i32 i35"]': "Male",                 # Gender
    '//input[@aria-labelledby="i37 i40"]': "GNFPYC"                # Verification Code
}

# Initialize the driver
driver = webdriver.Chrome() 
try:
    form_url = "https://forms.gle/WT68aV5UnPajeoSc8"
    driver.get(form_url)
    time.sleep(3)  

    # Fill out the form 
    for xpath, value in form_data.items():
        element = driver.find_element(By.XPATH, xpath)
        element.send_keys(value)
        time.sleep(1)  # Small delay for stability

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//div[@role="button" and @aria-label="Submit"]')
    submit_button.click()

    # Wait for confirmation page
    time.sleep(5)

    # Take a screenshot of the confirmation page
    driver.save_screenshot("confirmation_page.png")
    print("Screenshot saved as confirmation_page.png")

finally:
    # Close the driver
    driver.quit()
