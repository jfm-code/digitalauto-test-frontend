from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from class_method import BaseTest
from set_up import Base
import unittest
import json
import requests
from actions import click_sign_in, enter_email, enter_password, submit_sign_in