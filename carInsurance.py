from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options



import random
import config
import time

TITLES = ["Software Engineer", "Test Engineer", "Computer programmer", "Computer Engineer", "Computer Analyst",
          "Applications Programmer", "Technical Engineer", "Test Engineer", "Consultant"]

jobs = 0
Fi = ['£0', '£50', '£100', '£150', '£200', '£250', '£300', '£350', '£400', '£450', '£500', '£700', '£1000']


email = config.EMAIL
password = config.PASSWORD
value = 4000
car = 1
miles = 6500
bMiles = 500
ExcessVol = 1
Volnad = 1
staDate = 2
radioBL = 1
doesntExist = 0
tallyCounter = 0
NoBProtection = 1



x = 1000

url = 'https://www.moneysupermarket.com/my-account/sign-in/?from=RetrieveQuoteGotoSign&redirect_uri=%2Fcar-insurance%2F%3Ffrom%3DRetrieveQuotePostSign'
options = Options()
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--incognito")
#options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome("/Users/MohamedS/Downloads/chromedriver", options=options)
driver.set_window_size(1440, 900)

driver.get(url)

driver.find_element_by_id('emailAddress').send_keys(email)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('signInButton').click()

# ///////////////////////////////////////////////// page 1 #/////////////////////////////////////////////////////////////////

while x != 0:
    tallyCounter = tallyCounter + 1
    url = 'https://www.moneysupermarket.com/shop/car-insurance/questionset/your-car#?new-journey'

    driver.get(url)
    driver.find_element_by_name('vehicleValue').clear()
    driver.find_element_by_name('vehicleValue').send_keys(value)

    value = value + 50

    if value == 9000:
        value = 4000

    if car == 1:
        driver.find_element_by_xpath('//*[@id="usageTypeQuestion"]/div[2]/fieldset/ul/li[1]/label').click()

    elif car == 2:
        driver.find_element_by_xpath('//*[@id="usageTypeQuestion"]/div[2]/fieldset/ul/li[2]/label').click()
    elif car == 3:
        driver.find_element_by_xpath('//*[@id="usageTypeQuestion"]/div[2]/fieldset/ul/li[3]/label').click()
        driver.find_element_by_xpath('// *[ @ id = "businessUsageTypeQuestion"] / div[2] / fieldset / ul / li[1] / label').click()
        driver.find_element_by_name('businessMilesPerYear').send_keys(bMiles)
        bMiles = bMiles + 50
        if bMiles ==3000:
            bMiles = 50

    car = car + 1
    if car == 3:
        car = 1

    driver.find_element_by_name('personalMilesPerYear').clear()
    driver.find_element_by_name('personalMilesPerYear').clear()
    driver.find_element_by_name('personalMilesPerYear').send_keys(miles)
    miles = miles + 50

    if miles == 13000:
        miles = 6500

    # ///////////////////////////////////         page 2      ///////////////////////////////////////////////////////////////////////////////
    driver.find_element_by_class_name('btn__text').click()
    driver.implicitly_wait(2)
    driver.find_element_by_id('occupationField').clear()

    driver.find_element_by_id('occupationField').send_keys(TITLES[jobs])
    jobs = jobs + 1
    if jobs == 9:
        jobs = 1



    driver.find_element_by_xpath('//*[@id="hasDrivingOffencesQuestion"]/div[2]/fieldset/ul/li[1]/label').click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="drivingOffenceTypeQuestion"]/div[2]/fieldset/ul/li[1]/label').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="drivingOffenceCodeQuestion"]/div[2]/fieldset/ul/li[1]/label').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="drivingOffenceDate"]/input[1]').send_keys("22")
    driver.find_element_by_xpath('//*[@id="drivingOffenceDate"]/input[2]').send_keys("11")
    driver.find_element_by_xpath('//*[@id="drivingOffenceDate"]/input[3]').send_keys("2017")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="drivingOffencePenaltyPointsQuestion"]/div[2]/fieldset/ul/li[2]/label').click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="drivingOffencePaidFineQuestion"]/div[2]/fieldset/ul/li[1]/label').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="drivingOffenceFineAmount"]').send_keys("100")

    driver.find_element_by_xpath('//*[@id="drivingOffenceBannedQuestion"]/div[2]/fieldset/ul/li[2]/label').click()

    driver.find_element_by_xpath('//*[@id="saveConvictionQuestion"]/div[2]/div/button').click()
    driver.implicitly_wait(1)

    # ////////////////////////////////// Page 3 ////////////////////////////////////////////////////////

    driver.find_element_by_xpath('//*[@id="motor-insurance"]/div/nav/div[1]/button/span').click()
    try:
        element = driver.find_element_by_xpath('//*[@id="voluntaryExcessQuestion"]/div[2]/fieldset/ul')
    except NoSuchElementException:
        elements = driver.find_element_by_xpath('//*[@id="voluntaryExcess"]')
        Select(elements).select_by_index(ExcessVol)
        ExcessVol = ExcessVol + 1
        if ExcessVol == 13:
            ExcessVol = 1
        doesntExist = 1

    if doesntExist == 0:




        if radioBL == 1:

            driver.find_element_by_xpath('//*[@id="voluntaryExcessQuestion"]/div[2]/fieldset/ul/li[1]/label').click()

        elif radioBL == 2:

            driver.find_element_by_xpath('//*[@id="voluntaryExcessQuestion"]/div[2]/fieldset/ul/li[2]/label').click()


        elif radioBL == 3:

            driver.find_element_by_xpath('//*[@id="voluntaryExcessQuestion"]/div[2]/fieldset/ul/li[3]/label').click()

        elif radioBL == 4:

            driver.find_element_by_xpath('//*[@id="voluntaryExcessQuestion"]/div[2]/fieldset/ul/li[4]/label').click()

        else:
            driver.find_element_by_xpath('//*[@id="voluntaryExcessQuestion"]/div[2]/fieldset/ul/li[5]/label').click()
            driver.implicitly_wait(1)
            element = driver.find_element_by_xpath('//*[@id="voluntaryExcess"]')
            driver.implicitly_wait(1)
            Select(element).select_by_index(Volnad)
            Volnad = Volnad + 1
            if Volnad == 9:
                Volnad = 1

    radioBL = radioBL + 1



    if NoBProtection == 1:
        driver.find_element_by_xpath(
            '// *[ @ id = "protectedNoClaimsQuestion"] / div[2] / fieldset / ul / li[2] / label').click()

    elif NoBProtection == 2:
        driver.find_element_by_xpath(
            '// *[ @ id = "protectedNoClaimsQuestion"] / div[2] / fieldset / ul / li[1] / label').click()

    if NoBProtection == 1:
        NoBProtection = 2
    elif NoBProtection == 2:
        NoBProtection = 1



    driver.find_element_by_xpath('//*[@id="hasAdditionalDriverQuestion"]/div[2]/fieldset/ul/li[2]/label').click()

    element = driver.find_element_by_xpath('//*[@id="policyStartDate"]')

    Select(element).select_by_index(staDate)
    staDate = staDate + 1
    if staDate == 7:
        staDate = 1


    # ////////////////////////////////// Retrieve quote button ////////////////////////////////////////////////////////

    driver.find_element_by_xpath('//*[@id="motor-insurance"]/div/nav/div[1]/button/span').click()







    for y in range(0, 10):
        nonTele = "// *[ @ id = \"result-table\"] / li[" + str(y + 1) + "] / footer / div / div / section / div[3] / a"
        try:
            element = driver.find_element_by_xpath(nonTele)
            text = element.text
            if text != 'More info':

                newElement = driver.find_elements_by_class_name('result-table__provider-image')[y]
                newTextE = driver.find_elements_by_xpath('// *[ @ id = "annual-price-label"]')[y]

                y = 10
                break
        except NoSuchElementException:

            newElement = driver.find_elements_by_class_name('result-table__provider-image')[y]
            newTextE = driver.find_elements_by_xpath('// *[ @ id = "annual-price-label"]')[y]
            y = 10
            break


    newText = newTextE.text

    print(newText)
    print(tallyCounter)



    if len(newText) == 3:
        x = 0
        break
    else:
         x = x -1




