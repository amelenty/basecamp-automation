import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


testcases = {
	'19+35' : '54',
	'77*13' : '1001',
	'95/20' : '4.75',
	'20-32' : '-12'
}

def myclick(c, driver):
    if c == '*':
        c = 'x'
    driver.find_element(By.XPATH, "//input[@value='" + c + "']").click()
    
def runtestcase(key, driver):
    for c in key:
        myclick(c, driver)
    myclick('=', driver)
    assert driver.find_element_by_id("resultsbox").get_attribute('value') == testcases[key]
    myclick('C', driver)

@pytest.fixture(scope="module")
def chrome(request):
    testcases = {
        '19+35' : '54',
        '77*13' : '1001',
        '95/20' : '4.75',
        '20-32' : '-12'
    }
    browser = webdriver.Chrome()
    browser.get('file:///C:/Users/ada.melentyeva/Documents/BaseCamp/Automation/calc.html')
    def fin():
        browser.quit()
    request.addfinalizer(fin)
    return browser

def test_basic_math(chrome):
    for testcase in testcases:
        runtestcase(testcase, chrome)
