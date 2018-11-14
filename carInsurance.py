# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import config
import gc


TITLES = ["Software Engineer", "Test Engineer", "Computer programmer", "Computer Engineer", "Computer Analyst",
          "Applications Programmer", "Technical Engineer", "Test Engineer", "Consultant"]

jobs = 0
Fi = ["£" + str(num) for num in range(0, 1050, 50)]

email = config.EMAIL
password = config.PASSWORD
value = 4000
car = 1
miles = 6500
bMiles = 500
ExcessVol = 1
Volnad = 1
staDate = 1
radioBL = 1
doesntExist = 0
tallyCounter = 0
NoBProtection = 1

x = 1000

url = 'https://www.moneysupermarket.com/my-account/sign-in/?from=RetrieveQuoteGotoSign&redirect_uri=%2Fcar-insurance%2F%3Ffrom%3DRetrieveQuotePostSign'
options = Options()
options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument("--incognito")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome("lib/chromedriver", options=options)

driver.get(url)

def insert_by_id(id, val):
    driver.find_element_by_id(id).send_keys(val)

def login():
   insert_by_id('emailAddress', email)
   insert_by_id('password', password)
   driver.find_element_by_id('signInButton').click()

def replace_by_name(id, val):
    driver.find_element_by_name(id).clear()
    driver.find_element_by_name(id).send_keys(val)

def replace_by_xpath(id, send_keys=False, val=None, **kwargs):
    str = ""
    for arg, value in kwargs.items():
        str += value
    if send_keys:
        driver.find_element_by_xpath('//*[@id="{}"]{}'.format(id, str)).send_keys(val)
    else:
        driver.find_element_by_xpath('//*[@id="{}"]/{}'.format(id, str)).click()

"""Page 1"""
login()

while x != 0:
    tallyCounter = tallyCounter + 1
    url = 'https://www.moneysupermarket.com/shop/car-insurance/questionset/your-car#?new-journey'

    driver.get(url)
    replace_by_name('vehicleValue', value)
    value = value + 50

    if value == 9000:
        value = 4000

    if car == 1:
        driver.find_element_by_xpath('//*[@id="usageTypeQuestion"]/div[2]/fieldset/ul/li[1]/label').click()

    elif car == 2:
        driver.find_element_by_xpath('//*[@id="usageTypeQuestion"]/div[2]/fieldset/ul/li[2]/label').click()
    elif car == 3:
        driver.find_element_by_xpath('//*[@id="usageTypeQuestion"]/div[2]/fieldset/ul/li[3]/label').click()
        driver.find_element_by_xpath(
            '// *[ @ id = "businessUsageTypeQuestion"] / div[2] / fieldset / ul / li[1] / label').click()
        driver.find_element_by_name('businessMilesPerYear').send_keys(bMiles)
        bMiles = bMiles + 50
        if bMiles == 3000:
            bMiles = 50

    car = car + 1
    if car == 3:
        car = 1

    replace_by_name('personalMilesPerYear', miles)
    miles = miles + 50

    if miles == 13000:
        miles = 6500

    """Page 2""" 
    driver.find_element_by_class_name('btn__text').click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_id('occupationField').clear()

    driver.find_element_by_id('occupationField').send_keys(TITLES[jobs])
    jobs = jobs + 1
    if jobs == 9:
        jobs = 1
        gc.collect()

    def fill_offences():
        offences = ["hasDrivingOffencesQuestion", "drivingOffenceTypeQuestion",
                    "drivingOffenceCodeQuestion"]

        offence_date = {
            "day": "22",
            "month": "11",
            "year": "2017"
        }

        for question in offences:
            replace_by_xpath(id=question, div='div[2]', fieldset='/fieldset', ul='/ul',                                            li='/li[1]', label='/label')

        counter = 1
        for k, v in offence_date.items():
            replace_by_xpath(id="drivingOffenceDate", send_keys=True, val=v, input='/input[{}]'.format                             (str(counter)))
            counter = counter + 1

        offences = ["drivingOffencePenaltyPointsQuestion", "drivingOffencePaidFineQuestion",
                   "drivingOffenceFineAmount", "drivingOffenceBannedQuestion"]
        fine = "100"

        for question in offences:
            if question == "drivingOffencePaidFineQuestion":
                 replace_by_xpath(id=question, div='div[2]', fieldset='/fieldset', ul='/ul',                                            li='/li[1]', label='/label')
            elif question == "drivingOffenceFineAmount":
                replace_by_xpath(id=question, send_keys=True, val=fine)
            else:
                replace_by_xpath(id=question, div='div[2]', fieldset='/fieldset', ul='/ul',                                            li='/li[2]', label='/label')

        replace_by_xpath(id="saveConvictionQuestion", div='div[2]/div', button='/button')

    fill_offences()
    """Page 3"""
    replace_by_xpath(id="motor-insurance", div='/div', nav='/nav/div[1]', button='/button/span')

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
            element = driver.find_element_by_xpath('//*[@id="voluntaryExcess"]')
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
    driver.implicitly_wait(0.5)
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
            try:
                newElement = driver.find_elements_by_class_name('result-table__provider-image')[y]
                newTextE = driver.find_elements_by_xpath('// *[ @ id = "annual-price-label"]')[y]
                y = 10
                break
            except NoSuchElementException:
                print("doesn't exist")

    newText = newTextE.text

    print(newText)
    print(tallyCounter)



    if len(newText) == 3:
        x = 0
        break
    else:
        x = x - 1
