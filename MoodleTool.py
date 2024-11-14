
# Importation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
from datetime import datetime
import os
load_dotenv()
# Make selenium and Firefox work together
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
geckodriver_path = "/snap/bin/geckodriver"
driver_service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(options=options, service=driver_service)

def MoodleCheckin():
    # Opens Moodle
    driver.get('https://moodle.becode.org/login/index.php')

    # Log In
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, 'loginbtn')

    username_field.send_keys('bxl-2024-10-bouman-huart')
    password=os.getenv('PASSWORD')
    password_field.send_keys(password)  
    login_button.click()

    # Waits for loggin in 
    driver.implicitly_wait(10)
    try:
        driver.get('https://moodle.becode.org/mod/attendance/view.php?id=1009')
    except :
        driver.implicitly_wait(10)
        driver.get('https://moodle.becode.org/mod/attendance/view.php?id=1009')

    try:
        checkin_button = driver.find_element(By.LINK_TEXT, "Check in")
        checkin_button.click()
    except :
        print('checkin button not available')
    current_day = datetime.now().strftime("%A").lower()

    
    Homework = {'monday','tuesday','thursday',}
    CampusDay = {'wednesday','friday'}
    # Perform action based on the current day
    location_field = driver.find_element(By.NAME, "location")
  
    if current_day in Homework:
        driver.execute_script("arguments[0].value = 'athome';", location_field)
    elif current_day in CampusDay:
        driver.execute_script("arguments[0].value = 'oncampus';", location_field)
    else:
        print('maybetheweekend')
   
    Done_button = driver.find_element(By.NAME,"submitbutton")                                      
    Done_button.click()
    
    driver.implicitly_wait(10)
    #driver.quit()"""
MoodleCheckin()



