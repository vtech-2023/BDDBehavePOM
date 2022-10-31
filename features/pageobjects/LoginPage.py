from Utilities import configreader
from features.pageobjects.Base import BaseSettingsPage


class LoginPage(BaseSettingsPage):

    def __init__(self,driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)
        self.DynamicImplicitWait(40)

    def validUsernameText(self, expectedText):
        self.DynamicImplicitWait(40)
        self.AssertText("usernaneText_XPATH", expectedText)

    def setUsername(self, username):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("username_ID",username)

    def validPasswordText(self, expectedTextVal):
        self.DynamicImplicitWait(40)
        self.AssertText("passwordText_XPATH", expectedTextVal)

    def setPassword(self, password):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("password_ID",password)

    def clickSignIn(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("signinButton_NAME")

    def validWriteMailText(self, expectedTextVal):
        self.DynamicImplicitWait(40)
        self.AssertText("writeMailText_XPATH", expectedTextVal)




