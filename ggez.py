# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test2():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://192.168.41.66:4445', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_2(self):
    self.driver.get("https://demo.irplus.in.th/Listed/READY/th/index")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
    self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[9]")))
    self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[9]").click()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".item_footer_1:nth-child(4) span")))
    assert self.driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div[3]/div/div/h4").text == "ค่านิยมองค์กร"
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
    self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[8]")))
    self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[8]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
    self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
  
