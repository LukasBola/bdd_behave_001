#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from behave import *
import time

@given('the page is loaded')
def step_impl(context): 
	context.browser.get('http://salon.rpgit.pl/')
	time.sleep(1)
	

@when('I fill username')
def step_impl(context):
	username_input = context.browser.find_element_by_xpath('//input[@id="id_username"]')
	username_input.send_keys('lukasz.bola')
	time.sleep(1)

@when('I fill password')
def step_impl(context):
	password_input = context.browser.find_element_by_xpath('//input[@id="id_password"]')
	password_input.send_keys('Welcome1')
	time.sleep(1)

@when('I click zaloguj')
def step_impl(context):
	login_button = context.browser.find_element_by_xpath('//button[@id="id_login_btn"]')
	login_button.click()
	time.sleep(3)

@then('the home page is diplayed')
def step_impl(context):
	context.browser.find_element_by_xpath('//table[@id="customers"]')
	