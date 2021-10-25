# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# link = "http://suninjuly.github.io/selects1.html"
# browser.get(link)
#
# num1 = browser.find_element_by_id("num1").text
# num2 = browser.find_element_by_id("num2").text
# num3 = int(num1)+int(num2)
# browser.find_element_by_tag_name("select").click()
# browser.find_element_by_css_selector("[value='%d']"%num3).click()
# browser.find_element_by_class_name("btn").click()
# time.sleep(5)
# browser.quit()


# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.support.ui import Select
#
# class Find_file(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome('./chromedriver_linux64/chromedriver')
#
#     # def test_work(self):
#     #     driver = self.driver
#     #     driver.get("http://demo.guru99.com/test/yahoo.html")
#     #     output = driver.find_element_by_tag_name("strong").text
#     #     self.assertIn("This is DEMO site for TESTING purpose",output)
#
#
# #########################################################################
#     def test_tab1(self):
#         driver = self.driver
#         driver.get("http://demo.guru99.com/test/yahoo.html")
#         elem = driver.find_element_by_id("pager1").click()
#         elem_1 = driver.find_element_by_class_name("slide2").get_attribute("textContent")
#         self.assertIn("Buddy vs. Buddy",elem_1)
#         time.sleep(2)
#     def test_tab2(self):
#         driver = self.driver
#         driver.get("http://demo.guru99.com/test/yahoo.html")
#         second = driver.find_element_by_id("pager2").click()
#         elem_2 = driver.find_element_by_class_name("slide3").get_attribute("textContent")
#         self.assertIn("Facebook™Friendly",elem_2)
#         time.sleep(2)
#     def test_tab3(self):
#         driver = self.driver
#         driver.get("http://demo.guru99.com/test/yahoo.html")
#         third = driver.find_element_by_id("pager3").click()
#         elem_3 = driver.find_element_by_class_name("slide4").get_attribute("textContent")
#         self.assertIn("Share Away,All From Here",elem_3)
#         time.sleep(2)
#     def test_tab4(self):
#         driver = self.driver
#         driver.get("http://demo.guru99.com/test/yahoo.html")
#         fourth = driver.find_element_by_id("pager4").click()
#         elem_4 = driver.find_element_by_class_name("slide5").get_attribute("textContent")
#         self.assertIn("IM On Mobile",elem_4)
#         time.sleep(2)
#     def test_tab5(self):
#         driver = self.driver
#         driver.get("http://demo.guru99.com/test/yahoo.html")
#         fifth = driver.find_element_by_id("pager5").click()
#         elem_5 = driver.find_element_by_class_name("slide6").get_attribute("textContent")
#         self.assertIn("Always On Chats",elem_5)
#         time.sleep(2)
#     def test_tab6(self):
#         driver = self.driver
#         driver.get("http://demo.guru99.com/test/yahoo.html")
#         sixth = driver.find_element_by_id("pager6").click()
#         elem_6 = driver.find_element_by_class_name("slide7").get_attribute("textContent")
#         self.assertIn("Tabbed IMs",elem_6)
#         time.sleep(2)
#     def test_tab7(self):
#         driver = self.driver
#         driver.get("http://demo.guru99.com/test/yahoo.html")
#         seventh = driver.find_element_by_id("pager7").click()
#         elem_7 = driver.find_element_by_class_name("slide8").get_attribute("textContent")
#         self.assertIn("See What's Inside The New Yahoo! Messenger",elem_7)
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()





# import time
#
# class Register(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#
#     def test_1(self):
#         driver=self.driver
#         driver.get("http://demo.guru99.com/test/login.html")
#         self.assertIn("Login Page", driver.title)
#         elem = driver.find_element_by_name("email")
#         elem.clear()
#         elem.send_keys("tigranyan-lyov@mail.ru")
#         elem2 = driver.find_element_by_name("passwd")
#         elem2.clear()
#         elem2.send_keys("Hayastan")
#
#         driver.find_element_by_id("SubmitLogin").click()
#         assert "No results found." not in driver.page_source
#         #spin = driver.find_element_by_class_name('error-copy')
#         #output = spin.find_element_by_xpath('.//preceding::h3[1]').text
#         output = driver.find_element_by_tag_name("h3").text
#         print(output)
#         self.assertEqual("Successfully Logged in...", output)
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()

# def mfunc(*args):
#     num = 0
#     for el in args:
#         if type(el) == int:
#             num+=el
#         else:
#             print("not int")
#     return num
# print(mfunc(7))
# print(mfunc(14,5))
# print(mfunc(7,'78',4))

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
