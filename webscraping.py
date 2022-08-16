
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

with open("data.json","w") as f:
    json.dump([],f)

def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
count=0;
driver = webdriver.Chrome(executable_path="C:\\Users\\rasto\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://summerofcode.withgoogle.com/programs/2022/organizations")
driver.implicitly_wait(20)
print(driver.title)
driver.window_handles
anchor = (driver.find_elements(by=By.CLASS_NAME,value= "content"))
isNextDisabled =False
while not isNextDisabled :
    for x in anchor:
        count=count+1
        driver.execute_script("window.open('');")
        driver.implicitly_wait(10)
        url1 = x.get_attribute("href")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url1)
        driver.implicitly_wait(15)
        title = driver.find_element(by=By.CLASS_NAME,value="title").text
        technologies = driver.find_element(by=By.CLASS_NAME, value="tech__content").text
        topics = driver.find_element(by=By.CLASS_NAME, value="topics__content").text
        description = driver.find_element(by=By.CLASS_NAME, value="bd").text
        write_json({
            "title" : title,
            "tech" :technologies,
             "topic" :topics ,
             "description" :  description
             })
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(20)
    buttons = driver.find_element(by=By.CLASS_NAME,value="mat-paginator-navigation-next")
    try:
        buttons.send_keys(Keys.RETURN)
    except:
        break
    anchor = (driver.find_elements(by=By.CLASS_NAME,value= "content"))
driver.quit()
print(count)
