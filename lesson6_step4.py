# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()


# from selenium import webdriver
# import math
# from numpy import log as ln
# import time
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get("http://SunInJuly.github.io/execute_script.html")
#
# def calcp(x):
#     return str(ln(abs(12*math.sin(int(x)))))
#
# try:
#     x_el = browser.find_element_by_id("input_value")
#     print(x_el.text)
#     x = x_el.text
#     y = calcp(x)
#     print(y)
#     num = browser.find_element_by_id("answer")
#     num.send_keys(y)
#     button = browser.find_element_by_id("robotCheckbox").click()
#     button2 = browser.find_element_by_id("robotsRule")
#     browser.execute_script("window.scrollBy(0, 150);")
#     button2.click()
#     browser.find_element_by_class_name("btn").click()
# finally:
#     time.sleep(10)
#     browser.quit()

# from selenium import webdriver
# import time
# import os
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get("http://suninjuly.github.io/file_input.html")
# try:
#     name = browser.find_element_by_name("firstname")
#     name.send_keys("Lyov")
#     lname = browser.find_element_by_name("lastname")
#     lname.send_keys("Tigranyan")
#     email = browser.find_element_by_name("email")
#     email.send_keys("jon.rembo.93@mail.ru")
#     file = browser.find_element_by_id("file")
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, "mtext.txt")
#     file.send_keys(file_path)
#     submit = browser.find_element_by_class_name("btn").click()
# finally:
#     time.sleep(10)
#     browser.quit()

# from selenium import webdriver
# import time
# import os
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get("http://suninjuly.github.io/file_input.html")
# try:
#     name = browser.find_element_by_name("firstname")
#     name.send_keys("Lyov")
#     lname = browser.find_element_by_name("lastname")
#     lname.send_keys("Tigranyan")
#     email = browser.find_element_by_name("email")
#     email.send_keys("jon.rembo.93@mail.ru")
#     file = browser.find_element_by_id("file").click()
#     #current_dir = os.path.abspath(os.path.dirname(__file__))
#     #file_path = os.path.join(current_dir, "ml.txt")
#     file.send_keys('/home/ubuntu/QA_selenium/mtext.txt')
#     submit = browser.find_element_by_class_name("btn")
# finally:
#     time.sleep(10)
#     browser.quit()







# import math
# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get("http://suninjuly.github.io/math.html")
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# try:
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#
#     num = browser.find_element_by_id("answer")
#     num.send_keys(y)
#     rob = browser.find_element_by_id("robotCheckbox").click()
#     rule = browser.find_element_by_id("robotsRule").click()
#     submit = browser.find_element_by_class_name("btn-default").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# ########## Find ATTRIBUT value with help GET_ATTRIBUT #######################
# import math
# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get("http://suninjuly.github.io/get_attribute.html")
#
#
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# try:
#     x_element = browser.find_element_by_id("treasure")
#     x = x_element.get_attribute("valuex")
#     y = calc(x)
#
#     num = browser.find_element_by_id("answer")
#     num.send_keys(y)
#     rob = browser.find_element_by_id("robotCheckbox").click()
#     rule = browser.find_element_by_id("robotsRule").click()
#     submit = browser.find_element_by_class_name("btn-default").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# from numpy import log as ln
# import time
# import math
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get('http://suninjuly.github.io/alert_accept.html')
#
# text = browser.find_element_by_class_name("btn").click()
# alert = browser.switch_to.alert
# alert.accept()
#
# def calcp(x):
#     return str(ln(abs(12*math.sin(int(x)))))
#
# x_el = browser.find_element_by_id("input_value")
# x = x_el.text
# y = calcp(x)
#
# row = browser.find_element_by_id("answer")
# row.send_keys(y)
# submit = browser.find_element_by_class_name('btn').click()
#
# time.sleep(10)
# browser.quit()

# from selenium import webdriver
# import math
# import time
# from numpy import log as ln
#
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get('http://suninjuly.github.io/redirect_accept.html')
#
# submit = browser.find_element_by_class_name("trollface").click()
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
#
# def calcp(x):
#     return str(ln(abs(12*math.sin(int(x)))))
#
# x_el = browser.find_element_by_id("input_value")
# x = x_el.text
# y = calcp(x)
#
# row = browser.find_element_by_id("answer")
# row.send_keys(y)
# submit = browser.find_element_by_class_name("btn").click()
#
# time.sleep(10)
# browser.quit()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get("http://suninjuly.github.io/explicit_wait2.html")
# try:
#
#     button = WebDriverWait(browser , 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$95"))
#     button2 = browser.find_element_by_id("book").click()
# finally:
#     time.sleep(10)
#     browser.quit()



# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get('https://www.tutorialspoint.com/questions/category/data-structure')
#
# els = browser.find_elements_by_class_name('cat-img')
# for el in els:
#     print(el.get_property('alt'))

# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get('https://www.tutorialspoint.com/questions/category/data-structure')
#
# els = browser.find_element_by_class_name('toc chapters trending')
# el2 = els.find_elements_by_tag_name('li')
# for el in el2[2:]:
#     text = el.click()
#     textfin = browser.find_element_by_class_name('qa_post').text
#     print(textfin)
#     time.sleep(2)
# browser.quit()


# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# browser.get('https://www.tutorialspoint.com/index.htm')
#
# search = browser.find_element_by_class_name('input')
# search.send_keys('python')
# button = browser.find_element_by_id('btnSearch').click()
#
# obob = browser.find_elements_by_class_name('col-md-4')
# for el in obob[:10]:
#     try:
#         data = el.find_element_by_tag_name('h4')
#         ver = data.text
#         price = el.find_element_by_class_name('price').text
#         print(ver,price)
#     except Exception as err:
#         print("No h48")
# time.sleep(5)
# browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
browser.get('https://www.tutorialspoint.com/index.htm')

search = browser.find_element_by_class_name('input')
search.send_keys('python')
button = browser.find_element_by_id('btnSearch').click()
time.sleep(5)
checkbox = browser.find_element_by_class_name('product-courses').click()
time.sleep(5)
mjson = []

#page1 = browser.find_element_by_class_name("pagination")
#page = page1.find_elements_by_tag_name('a')
def get_data_of_one_page():
    all_div = browser.find_elements_by_class_name('col-md-4')
    for el in all_div:
        tmp = {}
        title = el.find_element_by_tag_name('h4').text
        author = el.find_element_by_class_name('h25')
        aut = author.find_element_by_tag_name('a').text
        duration = el.find_element_by_class_name('course-list-video')
        dur = duration.find_element_by_tag_name('span').text
        price = el.find_element_by_tag_name('b').text
        tmp["title"] = title
        tmp["aut"] = aut
        tmp["duration"] = dur
        tmp["price"] = price
        mjson.append(tmp)

pagination = browser.find_elements_by_class_name("page-item")
mhref = []

for el in pagination:
    try:
        mhref.append(el.find_element_by_tag_name('a').get_property('href'))
    except Exception as err:
        print(err)

for href in mhref:
    browser.get(href)
    time.sleep(5)
    get_data_of_one_page()

#print(dict(mjson))
browser.quit()

import json
print(json.dumps(mjson, indent=2, sort_keys=True))
# pagination = browser.find_element_by_class_name("pagination")
# ml = pagination.find_elements_by_class_name("page-item")
#
# for el in ml[2:-1]:
#     new = el.find_element_by_tag_name('a').click()

#

#print(new)

#print(mjson)


# for element in page[2:]:
#     element = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CLASS_NAME, "page-item")))
#     element.click()
#     time.sleep(5)
#     all_div2 = browser.find_elements_by_class_name('col-md-4')
#     for el in all_div2:
#         tmp = {}
#         title = el.find_element_by_tag_name('h4').text
#         author = el.find_element_by_class_name('h25')
#         aut = author.find_element_by_tag_name('a').text
#         duration = el.find_element_by_class_name('course-list-video')
#         dur = duration.find_element_by_tag_name('span').text
#         price = el.find_element_by_tag_name('b').text
#         tmp["title"] = title
#         tmp["aut"] = aut
#         tmp["duration"] = dur
#         tmp["price"] = price
#         mjson.append(tmp)

# import unittest
# from selenium import webdriver
# import time
# import re
#
# class Find_more(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome('./chromedriver_linux64/chromedriver')
#
#     def test_price(self):
#         driver = self.driver
#         driver.get("https://www.tutorialspoint.com/index.htm")
#         search = driver.find_element_by_class_name('input')
#         search.send_keys('python')
#         button = driver.find_element_by_id('btnSearch').click()
#         time.sleep(5)
#         all_div = driver.find_elements_by_class_name('col-md-4')
#         prices = []
#         for el in all_div:
#             price = el.find_element_by_class_name('price').text
#             prices.append(int(re.findall(r'\d+', price)[0]))
#         prices.sort()
#         self.assertGreater(prices[-1],50)
#         time.sleep(5)

    # def test_if(self):
    #     driver = self.driver
    #     driver.get("https://www.tutorialspoint.com/index.htm")
    #     search = driver.find_element_by_class_name('input')
    #     search.send_keys('python')
    #     button = driver.find_element_by_id('btnSearch').click()
    #     time.sleep(5)
    #     count = driver.find_element_by_id("total").text
    #     num = re.findall(r'\d+',count)
    #     if num:
    #         num = num[0]
    #     self.assertEqual(int(num),307)
    #     time.sleep(5)
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()
