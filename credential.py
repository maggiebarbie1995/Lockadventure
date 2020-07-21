# credential_array = []
from user import User
class Credential:
    """
    a class that generates new credential for users
    """
    pass
    credential_array = []
    user_credentials_list = []

@classmethod
def check_user(cls,first_name,password):
    current_user = ''
    for user in User. users_array:
        if (user.first_name == first_name and user.password == password):
            current_user = user.first_name
            return current_user

def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

def save_credential(self):
        """
        save_contact method saves credentials objects into credential_array
        """
        Credential.credential_array.append(self)       

