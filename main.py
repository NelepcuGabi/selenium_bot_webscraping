from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 
import time
import pandas as pd

#variables
website = 'https://adamchoi.co.uk/teamgoals/detailed'
xpath = '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]'

country = input("enter what country you want:")

#action
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options =options)  
driver.get(website)
WebDriverWait(driver,5).until(
    EC.visibility_of_element_located((By.XPATH, xpath))
)
button = driver.find_element(By.XPATH,xpath)
button.click()


drop_down = Select(driver.find_element(By.ID, "country"))
drop_down.select_by_visible_text(country)
time.sleep(3)



#lists
matches = driver.find_elements(By.TAG_NAME,'tr')
date = []
home_team = []
score = []
away_team = []
#scrapping the data we want and putting it in the lists
for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home = match.find_element(By.XPATH, './td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)
    


driver.quit()


df = pd.DataFrame({'date': date, 'home_team':home_team, 'score': score,'away_team': away_team})
df.to_csv('footbal_data.csv', index=False)
print(df)