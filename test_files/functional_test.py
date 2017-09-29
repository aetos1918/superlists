from selenium import webdriver
import unittest

# browser = webdriver.Firefox()
# browser.get("http://localhost:8000")
# try:
# 	assert 'To Do' in browser.title
# except AssertionError:
# 	print("Hacker Online")
# finally:
# 	browser.quit()

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrive_later(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Django', self.browser.title)
		self.fail("Finish the test")

if __name__ == "__main__":
	unittest.main(warnings='ignore')
