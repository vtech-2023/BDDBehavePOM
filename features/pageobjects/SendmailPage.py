from features.pageobjects.Base import BaseSettingsPage


class SendmailPage(BaseSettingsPage):

    def __init__(self,driver):
        super().__init__(driver)

    def clickWriteMail(self):
        self.DynamicImplicitWait(40)
        self.ClickLinks("writeMail_XPATH")

    def setTo(self, to):
        self.DynamicImplicitWait(40)
        self.TypeEditBoxEmail("toField_XPATH", to)

    def setSubjectArea(self, subject):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("subject_XPATH",subject)

    def setComposeArea(self,compose):
        self.SwitchFrameAddress("frameCompose_CSSSELECTOR")
        self.TypeEditBox("composeArea_XPATH",compose)

    def clickSendMail(self):
        self.DynamicImplicitWait(40)
        self.SwitchOutFrameAddress()
        self.ClickButton("send_XPATH")

    def clickLogout(self):
        self.DynamicImplicitWait(40)
        self.ClickLinks("logout_XPATH")

    def validlogout(self, expectedTextVal):
        self.DynamicImplicitWait(40)
        self.AssertText("logoutText_XPATH", expectedTextVal)