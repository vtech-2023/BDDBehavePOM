from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from Utilities import configreader
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC


class BaseSettingsPage:

    def __init__(self, driver):
        self.driver = driver

    # KeyWord Driver approach
    def TypeEditBox(self, locator, typeValue):
        if str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
        elif str(locator).endswith("_CSSSELECTOR"):
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).send_keys(
                typeValue)

    # KeyWord Driver approach
    #  https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html?highlight=keys#module-selenium.webdriver.common.keys
    def EnterButtonEditBoxEmail(self, locator):
        if str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_CSSSELECTOR"):
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)


    # KeyWord Driver approach
    def ClickRadio(self, locator):
        global val
        if str(locator).endswith("_ID"):
            val = self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            val = self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_CLASS"):
            val = self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_XPATH"):
            val = self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_CSSSELECTOR"):
            val = self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()

    # KeyWord Driver approach
    def ClickCheckbox(self, locator):
        global val
        if str(locator).endswith("_ID"):
            val = self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass
        elif str(locator).endswith("_NAME"):
            val = self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass
        elif str(locator).endswith("_CLASS"):
            val = self.driver.find_element_by_class_name(
                configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass
        elif str(locator).endswith("_XPATH"):
            val = self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass
        elif str(locator).endswith("_CSSSELECTOR"):
            val = self.driver.find_element_by_css_selector(
                configreader.ConfigReader("locators", locator)).is_selected()
            if val == False:
                self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()
            elif val == True:
                pass

    # KeyWord Driver approach
    def ClickButton(self, locator):
        if str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()
        elif str(locator).endswith("_CSSSELECTOR"):
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()

    # KeyWord Driver approach
    def ClickLinks(self, locator):
        if str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_CLASS"):
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_CSSSELECTOR"):
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_LINKTEXT"):
            self.driver.find_element_by_link_text(configreader.ConfigReader("locators", locator)).click()

        elif str(locator).endswith("_PARTIALLINKTEXT"):
            self.driver.find_element_by_partial_link_text(configreader.ConfigReader("locators", locator)).click()



    # KeyWord Driver approach
    def SwitchFrameAddress(self, locator):
        global addressFrame
        if str(locator).endswith("_ID"):
            addressFrame = self.driver.find_element_by_id(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)
        elif str(locator).endswith("_NAME"):
            addressFrame = self.driver.find_element_by_name(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)
        elif str(locator).endswith("_CLASS"):
            addressFrame = self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)
        elif str(locator).endswith("_XPATH"):
            addressFrame = self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)
        elif str(locator).endswith("_CSSSELECTOR"):
            addressFrame = self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator))
            self.driver.switch_to.frame(addressFrame)

    # Switch out of frame to main page
    def SwitchOutFrameAddress(self):
        self.driver.switch_to.default_content()

    # Implicit wait
    def DynamicImplicitWait(self, timePeriod):
        self.driver.implicitly_wait(timePeriod)

    # Static Wait:
    def StaticWait(self, timePeriod):
        time.sleep(timePeriod)

    # # Explicit Wait
    # def DynamicExplcitWait(self, locator, timePeriod):
    #     global wait
    #     wait = WebDriverWait(self.driver, timePeriod)
    #     if str(locator).endswith("_XPATH"):
    #         wait.until(EC.element_located_to_be_selected(By.XPATH, (configreader.ConfigReader("locators", locator))))
    #     elif str(locator).endswith("_CSSSELECTOR"):
    #         wait.until(EC.element_located_to_be_selected(By.CSS_SELECTOR, configreader.ConfigReader("locators", locator)))


    # Assert based functions
    # Assert by title of the page
    # Assert by text present in an element - text property of Selenium - find text by any 8 locators
    # Assert by the attribute value - use the get_attribute()
    def AssertTitle(self, extectedTitle):
        valTitle = self.driver.title
        assert valTitle == extectedTitle

    def AssertText(self, locator, expectedTextVal):
        if str(locator).endswith("_ID"):
            actualTextVal = self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).text
            assert actualTextVal == expectedTextVal
        elif str(locator).endswith("_NAME"):
            actualTextVal = self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).text
            assert actualTextVal == expectedTextVal
        elif str(locator).endswith("_CLASS"):
            actualTextVal = self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).text
            assert actualTextVal == expectedTextVal
        elif str(locator).endswith("_XPATH"):
            actualTextVal = self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).text
            assert actualTextVal == expectedTextVal
        elif str(locator).endswith("_CSSSELECTOR"):
            actualTextVal = self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).text
            assert actualTextVal == expectedTextVal
        elif str(locator).endswith("_TAGNAME"):
            actualTextVal = self.driver.find_element_by_tag_name(configreader.ConfigReader("locators", locator)).text
            assert actualTextVal == expectedTextVal
        elif str(locator).endswith("_LINKTEXT"):
            actualTextVal = self.driver.find_element_by_link_text(configreader.ConfigReader("locators", locator)).text
            assert actualTextVal == expectedTextVal
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            actualTextVal = self.driver.find_element_by_partial_link_text(configreader.ConfigReader("locators", locator)).text
            assert actualTextVal == expectedTextVal


    def TypeEditBoxEmail(self, locator, typeValue):
        if str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
            self.driver.find_element_by_id(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
            self.driver.find_element_by_name(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
            self.driver.find_element_by_class_name(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).send_keys(typeValue)
            self.driver.find_element_by_xpath(configreader.ConfigReader("locators", locator)).send_keys(Keys.RETURN)
        elif str(locator).endswith("_CSSSELECTOR"):
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).click()
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).send_keys(
                typeValue)
            self.driver.find_element_by_css_selector(configreader.ConfigReader("locators", locator)).send_keys(
                Keys.RETURN)





