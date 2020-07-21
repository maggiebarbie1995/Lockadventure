# credential_array = []
from user import User
class Credential:
    """
    a class that generates new credential for users
    """
    pass
    credential_list = []
    user_credentials_list = []
    @classmethod
    def check_user(cls,first_name,password):
        current_user = ''
        for user in User. users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
            return current_user

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credential(self):
        """
        save_contact method saves credentials objects into credential_list
        """
        Credential.credential_list.append(self)

    @classmethod
    def display_credential(cls):
        """
        method that returns the credential list
        """
        return cls.credential_list


