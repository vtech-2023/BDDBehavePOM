import time
import pandas as pd
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import configreader


# This will contain HOOKS - HOOKS in BEHAVE are like PYTEST DECORATERS/ANNOTATION - @pytest


# Hooks to run before scenario and after scenario.
# Hooks to run before step and after step.
# Hooks to run before all and after all

# After step hook
def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)


# Before step hook
def before_step(context, step):
    pass


# Before Scenario Hook
def before_scenario(context,driver):
    if configreader.ConfigReader("base info", "browser") == "chrome":
        context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        context.driver.maximize_window()
        context.driver.set_page_load_timeout(500)
    if configreader.ConfigReader("base info", "browser") == "firefox":
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        context.driver.maximize_window()
        context.driver.set_page_load_timeout(500)


# After Scenario Hook
def after_scenario(context, driver):
    time.sleep(3)
    context.driver.quit()


def before_feature(context, feature):
    if 'test-data-from-excel' in feature.tags:  # >>> you can have this check on feature.name instead of tag
        path_to_file = 'C:\\Users\\lenovo\\Desktop\\SeleniumPython\\BDDBehavePOM\\Excel\\data.xlsx'
        df = pd.read_excel(path_to_file)
        example = next(sc.examples[0] for sc in feature.scenarios if sc.name == 'login data') # >>> find the first examples object for scenario with given name
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)
