from rest_framework_simplejwt.tokens import RefreshToken


class TokenSerializer:
    def __init__(self, user=None):
        if user:
            self.user = user
            self.token = self.get_tokens_for_user()

    def get_tokens_for_user(self):
        refresh = RefreshToken.for_user(self.user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

