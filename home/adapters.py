from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # This function runs before the user is fully logged in
        # It ensures that if the email already exists, it links the account
        pass

    def get_connect_redirect_url(self, request, socialaccount):
        # Directly redirects to your custom redirect view
        return '/login-redirect/'

    def is_auto_signup_allowed(self, request, sociallogin):
        # Forces automatic signup so the user never sees a form
        return True