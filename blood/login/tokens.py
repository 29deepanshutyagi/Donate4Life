from django.contrib.auth.tokens import PasswordResetTokenGenerator

from typing import Text

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self,user,timestamp):
        return (
        Text(user.pk) + Text(timestamp) 
        # text_type(user.profile.signup_confirmation)
        )

generate_token = TokenGenerator()
