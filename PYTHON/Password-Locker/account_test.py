import unittest
from account import Account


class TestAccount(unittest.TestCase):
    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account('jush', 'Hassan', 'Juma', 'mshairi1')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Account.accounts_list = []

    def test_init(self):
        '''
        Test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.user_name, 'jush')
        self.assertEqual(self.new_account.first_name, 'Hassan')
        self.assertEqual(self.new_account.last_name, 'Juma')
        self.assertEqual(self.new_account.pass_word, 'mshairi1')

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
        the accounts list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Account.accounts_list), 1)

    def test_save_mult_accounts(self):
        '''
        Test case to test if we can save multiple accounts in accounts_list
        '''
        self.new_account.save_account()
        test_acc = Account('jush', 'Juma', 'James', 'Moringa')
        test_acc.save_account()
        self.assertEqual(len(Account.accounts_list), 2)

    def test_auth_user(self):
        '''
        method that test if login works fine
        '''
        self.new_account.save_account()
        self.assertTrue(self.new_account.auth_user(
            self.new_account.user_name, self.new_account.pass_word))

    def test_account_exists(self):
        '''
        Test case to test if an account already exists
        '''
        self.new_account.save_account()
        self.assertTrue(Account.account_exists(self.new_account.user_name))

    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove an account from our accounts list
        '''
        self.new_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Account.accounts_list), 0)


if __name__ == '__main__':
    unittest.main()
