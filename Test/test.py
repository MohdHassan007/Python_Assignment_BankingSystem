import unittest
from unittest.mock import patch
from dao.accountdao import AccountDAO

class TestAccountDAO(unittest.TestCase):
    def test_create_account(self):
        # Mock the __init__ method
        try:
            # Call the AccountDAO constructor
            account_dao = AccountDAO()

            # Assertions
            self.assertIsInstance(account_dao, AccountDAO)  # Check if the object is an instance of AccountDAO

        finally:
            # Restore the original __init__ method
            pass
if __name__ == '__main__':
    unittest.main()
