from django.contrib.auth.tokens import PasswordResetTokenGenerator 
from django.contrib.auth.models import User
 

class TokenGenerator(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):  
        return ({{user.id}})  
account_activation_token = TokenGenerator()  