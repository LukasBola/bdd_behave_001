#!/usr/bin/env python3
# -*- coding: utf-8 -*-
### Author: Łukasz Bola

Feature: Test of car dealer site

	Scenario: log in 
		Given the page is loaded	
		When I fill username 
		When I fill password
		When I click zaloguj
		Then the home page is diplayed