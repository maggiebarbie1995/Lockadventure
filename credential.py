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
