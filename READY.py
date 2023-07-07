# Generated by Selenium IDE
import pytest
import time
import json
from SC import take_screenshot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestREADY100():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://192.168.41.66:4445', desired_capabilities=DesiredCapabilities.CHROME)
    #self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_rEADY100(self):
    try:
      self.driver.get("https://demo.irplus.in.th/Listed/READY/th/index")
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
      time.sleep(3)
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
      #WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ยอมรับทั้งหมด")))
      #self.driver.find_element(By.LINK_TEXT, "ยอมรับทั้งหมด").click()
      time.sleep(2)
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[3]/div/div/div/div[2]/img")))
      elements = self.driver.find_elements(By.XPATH, "//div[@id=\'body-bg\']/section[3]/div/div/div/div[2]/img")
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),\'ราคาหลักทรัพย์\')]")))
      self.driver.find_element(By.XPATH, "//a[contains(text(),\'ราคาหลักทรัพย์\')]").click()
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
      time.sleep(2)
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),\'ดูข้อมูลเพิ่มเติม\')]")))
      self.driver.find_element(By.XPATH, "//a[contains(text(),\'ดูข้อมูลเพิ่มเติม\')]").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
      time.sleep(2)
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),\'ดูกิจกรรมอื่นๆ\')]")))
      self.driver.find_element(By.XPATH, "//a[contains(text(),\'ดูกิจกรรมอื่นๆ\')]").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
      time.sleep(2)
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),\'ดูข่าวสารอื่นๆ\')]")))
      self.driver.find_element(By.XPATH, "//a[contains(text(),\'ดูข่าวสารอื่นๆ\')]").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
      time.sleep(2)
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[5]/div/div/div/a")))
      self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[5]/div/div/div/a").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
      time.sleep(2)
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[5]/div/div/div[2]/a")))
      self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[5]/div/div/div[2]/a").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
      time.sleep(2)
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[5]/div/div/div[3]/a")))
      self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[5]/div/div/div[3]/a").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[4]").click()
      time.sleep(2)
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[9]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[9]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div[3]/div/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div[3]/div/div/h4").text == "ค่านิยมองค์กร"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[8]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[8]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/div/h4").text == "การเปลี่ยนแปลงและพัฒนาการที่สำคัญ"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601776\']/a/div)[3]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601776\']/a/div)[3]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/div/h4").text == "โครงสร้างองค์กร"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16548267\']/a/div)[2]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16548267\']/a/div)[2]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/div/h4").text == "คณะกรรมการบริษัท"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//li[@id=\'nav-16744764\']/a/div")))
      self.driver.find_element(By.XPATH, "//li[@id=\'nav-16744764\']/a/div").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section/div/div/div/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section/div/div/div/div/h4").text == "คณะผู้บริหาร"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16744764\']/a/div)[2]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16744764\']/a/div)[2]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3").text == "การกำกับดูแลกิจการ"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/a/div)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16744764\']/a/div)[3]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16744764\']/a/div)[3]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section/div/div/div/h3").text == "ข้อมูลนำเสนอแบบมัลติมีเดีย"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[2]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[2]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[2]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[7]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[7]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/h3").text == "งบการเงิน"
      self.driver.switch_to.frame(0)
      self.vars["window_handles"] = self.driver.window_handles
      self.driver.find_element(By.LINK_TEXT, "2566").click()
      self.vars["win7773"] = self.wait_for_window(2000)
      self.vars["root"] = self.driver.current_window_handle
      self.driver.switch_to.window(self.vars["win7773"])
      self.driver.find_element(By.ID, "income").click()
      self.driver.close()
      self.driver.switch_to.window(self.vars["root"])
      self.driver.switch_to.frame(0)
      self.vars["window_handles"] = self.driver.window_handles
      self.driver.find_element(By.LINK_TEXT, "2565").click()
      self.vars["win2147"] = self.wait_for_window(2000)
      self.driver.switch_to.window(self.vars["win2147"])
      self.driver.find_element(By.ID, "cash").click()
      self.driver.close()
      self.driver.switch_to.window(self.vars["root"])
      self.driver.switch_to.frame(0)
      self.vars["window_handles"] = self.driver.window_handles
      self.driver.find_element(By.LINK_TEXT, "2564").click()
      self.vars["win4390"] = self.wait_for_window(2000)
      self.driver.switch_to.window(self.vars["win4390"])
      self.driver.find_element(By.ID, "income").click()
      self.driver.close()
      self.driver.switch_to.window(self.vars["root"])
      self.vars["window_handles"] = self.driver.window_handles
      self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-danger").click()
      self.vars["win3763"] = self.wait_for_window(2000)
      self.driver.switch_to.window(self.vars["win3763"])
      self.driver.close()
      self.driver.switch_to.window(self.vars["root"])
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[2]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[2]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[2]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[10]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[10]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3").text == "ข้อมูลสำคัญทางการเงิน"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[2]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[2]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[2]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[9]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[9]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3").text == "คำอธิบายและบทวิเคราะห์"
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539118\']/a/div)[5]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/div/div")))
      elements = self.driver.find_elements(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/div/div")
      assert len(elements) > 0
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[8]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[8]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3").text == "การประชุมผู้ถือหุ้น"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[11]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[11]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div[2]")))
      elements = self.driver.find_elements(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div[2]")
      assert len(elements) > 0
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[10]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[10]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3").text == "นโยบายและประวัติการจ่ายเงินปันผล"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[11]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[11]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3").text == "ปฏิทินกิจกรรมนักลงทุนสัมพันธ์"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[12]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[12]").click()
      WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, "//body")))
      elements = self.driver.find_elements(By.XPATH, "//body")
      assert len(elements) > 0
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[3]").click()
      self.vars["window_handles"] = self.driver.window_handles
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601775\']/a/div)[13]").click()
      self.vars["win5152"] = self.wait_for_window(2000)
      self.vars["root"] = self.driver.current_window_handle
      self.driver.switch_to.window(self.vars["win5152"])
      self.driver.close()
      self.driver.switch_to.window(self.vars["root"])
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[4]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[4]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[4]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[9]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[9]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3").text == "แบบ 56-1 One Report"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[4]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[4]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[4]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[12]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[12]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3").text == "บทวิเคราะห์"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[10]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[10]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div[2]/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div[2]/div/h4").text == "ประกาศจากตลาดหลักทรัพย์"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[13]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[13]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div[2]/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div[2]/div/h4").text == "ข่าวสารล่าสุด"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[14]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[14]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div[2]/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div[2]/div/h4").text == "ห้องข่าวประชาสัมพันธ์"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[5]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[15]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[15]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div[2]/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div[2]/div/h4").text == "ข่าวจากหนังสือพิมพ์"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[11]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16539192\']/a/div)[11]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'wrapper\']/section[2]/div/div/div/h3").text == "สอบถามข้อมูล"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[16]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[16]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/h3").text == "รับข่าวสารทางอีเมล"
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[6]")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[6]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-17601772\']/span/i)[6]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[17]")))
      self.driver.find_element(By.XPATH, "(//li[@id=\'nav-16728556\']/a/div)[17]").click()
      WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/div/h4")))
      assert self.driver.find_element(By.XPATH, "//div[@id=\'body-bg\']/section[2]/div/div/div/div/h4").text == "ติดต่อนักลงทุนสัมพันธ์"
    except AssertionError as e:
            # If an assertion error occurs, capture a screenshot and attach it to the Allure report
            allure.attach(self.driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e
  
