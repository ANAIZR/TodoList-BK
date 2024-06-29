from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    tokens = RefreshToken.for_user(user)

    return {
        # refresh sera usando en un futuro para volver a crear un nuevo token
        # cuando el original expire
        "refresh": str(tokens),
        # lo que usaremos ahora es el access_token
        "access": str(tokens.access_token),
    }
