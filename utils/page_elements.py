from selenium.webdriver.common.by import By

class PageElements:
    # Registration elements
    SIGN_IN_BUTTON = (By.CLASS_NAME, 'login')
    EMAIL_INPUT = (By.ID, 'email_create')
    CREATE_ACCOUNT_BUTTON = (By.ID, 'SubmitCreate')
    FIRST_NAME_INPUT = (By.ID, 'customer_firstname')
    LAST_NAME_INPUT = (By.ID, 'customer_lastname')
    PASSWORD_INPUT = (By.ID, 'passwd')
    SUBMIT_ACCOUNT = (By.ID, 'submitAccount')
    
    # Login elements
    LOGIN_EMAIL_INPUT = (By.ID, 'email')
    LOGIN_PASSWORD_INPUT = (By.ID, 'passwd')
    LOGIN_BUTTON = (By.ID, 'SubmitLogin')

    # Navigation elements
    WOMEN_CATEGORY = (By.XPATH, "//a[@title='Women']")
    DRESSES_CATEGORY = (By.XPATH, "//a[@title='Dresses']")
    TSHIRTS_CATEGORY = (By.XPATH, "//a[@title='T-shirts']")
