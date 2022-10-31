import logging
import time

import allure
from allure_commons._allure import severity
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import configreader
from Utilities.LogUtil import Logger

from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.SendmailPage import SendmailPage

log = Logger(__name__, logging.INFO)


@given(u'we navigate to Rediffmail account')
def step_impl(context):
    context.reg = LoginPage(context.driver)
    context.reg.open(configreader.ConfigReader("base info", "URL"))
    log.logger.info("Navigated to Rediffmail Login Page")


@when(u'we validate the username text')
def step_impl(context):
    context.reg.validUsernameText("Username")
    log.logger.info("Username Text Validated")


@when(u'we type in the "{username}" edit box')
def step_impl(context, username):
    context.reg.setUsername(username)
    log.logger.info("Username field typed")


@when(u'we validate the password text')
def step_impl(context):
    context.reg.validPasswordText("Password")
    log.logger.info("Password Text Validated")


@when(u'we type in the "{password}" field')
def step_impl(context, password):
    context.reg.setPassword(password)
    log.logger.info("Password field typed")


@when(u'we click on the sign in button')
def step_impl(context):
    context.reg.clickSignIn()
    log.logger.info("Signin button clicked")
    time.sleep(6)



@then(u'we validate inbox page opens')
def step_impl(context):
    context.reg.validWriteMailText("Write mail")
    log.logger.info("Write mail text typed")

@given(u'we click in write mail link')
def step_impl(context):
    context.send = SendmailPage(context.driver)
    context.send.clickWriteMail()
    log.logger.info("Write Mail Clicked")



@when(u'we fill the "{to}" field')
def step_impl(context, to):
    time.sleep(6)
    context.send.setTo(to)
    log.logger.info("To field typed")



@when(u'we type the "{subject}" area')
def step_impl(context, subject):
    context.send.setSubjectArea(subject)
    log.logger.info("Subject field typed")



@when(u'type in "{compose}" area')
def step_impl(context,compose):
    context.send.setComposeArea(compose)
    log.logger.info("Compose field typed")



@when(u'we click on send button')
def step_impl(context):
    context.send.clickSendMail()
    log.logger.info("Send Button Clicked")



@when(u'we click on logout link')
def step_impl(context):
    context.send.clickLogout()
    log.logger.info("Logout link clicked")


@then(u'we validate that we have logded out of rediffmail account')
def step_impl(context):
    context.send.validlogout()
    log.logger.info("Validate text after logout")
