class Account:
  """
  Class that generates an instance of an account
  """
  def __init__(self,user_name,first_name,last_name,pass_word):
    '''
    __init__ method that helps us define properties for our objects.

    Args:
        user_name:Account user login user name
        first_name: Account user login first name.
        last_name : Account user login last name.
        pass_word:Account user login password
    '''
    self.user_name=user_name
    self.first_name=first_name
    self.last_name=last_name
    self.pass_word=pass_word

  accounts_list=[] #Empty accounts list

  def save_account(self):
    '''
    save_account method saves account objects into accounts_list
    '''
    Account.accounts_list.append(self)

  @classmethod
  def auth_user(cls,username,password):
    '''
    auth_user return true if login details are correct
    '''
    for account in cls.accounts_list:
      if account.user_name==username and account.pass_word==password:
        return True
      
    return False 

  @classmethod
  def account_exists(cls,username):
    '''
    Method that checks if an account already exists.
    Args:
        username: username to search if account already exists
    Returns :
        Boolean: True or false depending if the account exists
    '''
    for account in cls.accounts_list:
      if account.user_name==username:
        return True

    return False       

  
  def delete_account(self):
    '''
    delete_acount method deletes the saved account from the accounts_list
    '''
    Account.accounts_list.remove(self)     

    

