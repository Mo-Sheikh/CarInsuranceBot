from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import random
import config
import time



TITLES = ["Software Engineer", "Test Engineer", "Computer programmer", "Computer Engineer", "Computer Analyst",
          "Applications Programmer", "Technical Engineer", "Test Engineer"]
Fi = ['£0', '£50', '£100', '£150', '£200', '£250', '£300', '£350', '£400', '£450', '£500', '£700', '£1000']
dates = ['Thursday 8th November (Today)', 'Friday 9th November (Tomorrow)', 'Saturday 10th November', '11th', '12th', '13th' '14th', '15th', '16th']


email = config.EMAIL
password = config.PASSWORD
value = config.VALUE
car = config.CAR
miles = config.milesD
bMiles = config.buMiles
volExcess = 5
adVol = config.ADVOLUNTARY
StartDate = config.START


print(value)
print(car)
print(miles)
print(volExcess)


x = 1000

url = 'https://www.moneysupermarket.com/my-account/sign-in/?from=RetrieveQuoteGotoSign&redirect_uri=%2Fcar-insurance%2F%3Ffrom%3DRetrieveQuotePostSign'
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome("/Users/MohamedS/Downloads/chromedriver", options=options)

driver.get(url)


driver.find_element_by_id('emailAddress').send_keys(email)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('signInButton').click()



while x != 0:
    url = 'https://www.moneysupermarket.com/shop/car-insurance/questionset/your-car#?new-journey'



    driver.get(url)
    driver.find_element_by_name('vehicleValue').clear()
    driver.find_element_by_name('vehicleValue').send_keys(value)

    if car == 1:
        driver.find_element_by_xpath('//*[@id="usageTypeQuestion"]/div[2]/fieldset/ul/li[1]/label').click()

    elif car == 2:
        driver.find_element_by_xpath('//*[@id="usageTypeQuestion"]/div[2]/fieldset/ul/li[2]/label').click()
    elif car == 3:
        driver.find_element_by_xpath('//*[@id="usageTypeQuestion"]/div[2]/fieldset/ul/li[3]/label').click()
        driver.find_element_by_xpath('// *[ @ id = "businessUsageTypeQuestion"] / div[2] / fieldset / ul / li[1] / label').click()
        driver.find_element_by_name('businessMilesPerYear').send_keys(bMiles)




    driver.find_element_by_name('personalMilesPerYear').clear()
    driver.find_element_by_name('personalMilesPerYear').clear()
    driver.find_element_by_name('personalMilesPerYear').send_keys(miles)

    driver.find_element_by_class_name('btn__text').click()

    driver.implicitly_wait(2)
    driver.find_element_by_id('occupationField').clear()
    driver.find_element_by_id('occupationField').send_keys(random.choice(TITLES))

    driver.find_element_by_xpath('//*[@id="hasDrivingOffencesQuestion"]/div[2]/fieldset/ul/li[1]/label').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="drivingOffenceTypeQuestion"]/div[2]/fieldset/ul/li[1]/label').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="drivingOffenceCodeQuestion"]/div[2]/fieldset/ul/li[1]/label').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="drivingOffenceDate"]/input[1]').send_keys("22")
    driver.find_element_by_xpath('//*[@id="drivingOffenceDate"]/input[2]').send_keys("11")
    driver.find_element_by_xpath('//*[@id="drivingOffenceDate"]/input[3]').send_keys("2017")
    driver.find_element_by_xpath('//*[@id="drivingOffencePenaltyPointsQuestion"]/div[2]/fieldset/ul/li[2]/label').click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="drivingOffencePaidFineQuestion"]/div[2]/fieldset/ul/li[1]/label').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="drivingOffenceFineAmount"]').send_keys("100")

    driver.find_element_by_xpath('//*[@id="drivingOffenceBannedQuestion"]/div[2]/fieldset/ul/li[2]/label').click()

    driver.find_element_by_xpath('//*[@id="saveConvictionQuestion"]/div[2]/div/button').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="motor-insurance"]/div/nav/div[1]/button/span').click()

    driver.find_element_by_xpath('//*[@id="hasAdditionalDriverQuestion"]/div[2]/fieldset/ul/li[2]/label').click()

    element = driver.find_element_by_xpath('//*[@id="policyStartDate"]')

    Select(element).select_by_index(StartDate)

    driver.find_element_by_xpath('//*[@id="motor-insurance"]/div/nav/div[1]/button/span').click()

    time.sleep(20)

    x = 0

for y in range (10):

    element = driver.find_element_by_xpath('//*[@id="result-table"]/li')[y]

    newElement = element.find_elements_by_class_name("result-table-row__footer")

    if not newElement:
        element = 0
        driver.find_element_by_xpath(' // *[ @ id = "result-table"] / li[1] / div[1] / ul / li[10] / div / button').click()









