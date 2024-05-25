import unittest
from tests.test_change_language import TestChangeLanguage
from tests.test_filter_products import TestFilterProducts
from tests.test_registration import TestRegistration
from tests.test_send_message import TestSendMessage
from tests.test_submit_ad import TestSubmitAd

if __name__ == "__main__":
    # Create a test suite
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.makeSuite(TestRegistration),
        unittest.makeSuite(TestSubmitAd),
        unittest.makeSuite(TestFilterProducts),
        unittest.makeSuite(TestChangeLanguage),
        unittest.makeSuite(TestSendMessage)
    ])

    # Run the test suite with unittest
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
