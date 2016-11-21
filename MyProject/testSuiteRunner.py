import unittest
from commonWebDriver import DRIVER
from testLogin import *
from testClosePage import *

class TestSuiteRun():
    try:
        assert 'Mail' in DRIVER.title
        print("Preconditions: Target web page is open correctly.")
        loader = unittest.TestLoader()
        testSuite = unittest.TestSuite((
            loader.loadTestsFromTestCase(LoginTests),
            loader.loadTestsFromTestCase(ClosePageTest),
            ))
        runner = unittest.TextTestRunner(verbosity = 2)
        runner.run(testSuite)
        DRIVER.quit()
    except AssertionError as e:      
        print("Target web page is NOT open correctly.")
        DRIVER.quit()
    
if __name__ == "__main__":
    TestSuiteRun()
