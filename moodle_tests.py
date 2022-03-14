import unittest
import moodle_locators as locators
import moodle_methods as methods

class MoodleAppPositiveTestCases(unittest.TestCase): # container for our tests

    @staticmethod # signal to unittest that this is a function inside class , there is also classmethod
    def test_create_new_user(): # test in the name is mandatory
        methods.setUp()
        methods.log_in(locators.admin_username, locators.admin_password)
        methods.create_new_user()
        methods.search_user()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.check_new_user_can_login()
        methods.log_out()
        methods.log_in(locators.admin_username, locators.admin_password)
        methods.delete_user()
        methods.log_out()
        methods.tearDown()
        
