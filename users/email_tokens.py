from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountActivationToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return user.pk + timestamp + user.is_active


account_activation_token = AccountActivationToken()
