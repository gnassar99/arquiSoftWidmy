import requests
from social_core.backends.oauth import BaseOAuth2
from social_django.models import UserSocialAuth


class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('picture', 'picture')
    ]
    
    def authorization_url(self):
        """Return the authorization endpoint."""
        return "https://" + self.setting('DOMAIN') + "/authorize"
    
    def access_token_url(self):
        """Return the token endpoint."""
        return "https://" + self.setting('DOMAIN') + "/oauth/token"
    
    def get_user_id(self, details, response):
        """Return current user id."""
        return details['user_id']
    
    def get_user_details(self, response):
        url = 'https://' + self.setting('DOMAIN') + '/userinfo'
        headers = {'authorization': 'Bearer ' + response['access_token']}
        resp = requests.get(url, headers=headers)
        userinfo = resp.json()
        
        return {
            'username': userinfo['nickname'],
            'first_name': userinfo['name'],
            'picture': userinfo['picture'],
            'user_id': userinfo['sub']
        }

def getRole(request):
    user = request.user
    print("requested user: ", user)
    try:
        auth0_user = UserSocialAuth.objects.get(user=user, provider='auth0')
        print("auth0_user: ", auth0_user)
        access_token = auth0_user.extra_data['access_token']
        print("access_token: ", access_token)
        url = "https://widmy-g3.us.auth0.com/userinfo"  # Replace 'your-auth0-domain' with your actual Auth0 domain
        headers = {'authorization': 'Bearer ' + access_token, 
                    'content-type': 'application/json'}
        resp = requests.get(url, headers=headers)
        print("resp: ", resp.content)        
        userinfo = resp.json()
        print("userinfo: ", userinfo)
        if userinfo["nickname"] == "medico":
            role = "Medico"
        elif userinfo["nickname"] == "paciente":
            role = "Paciente"
        elif userinfo["nickname"] == "gerente":
            role = "Gerente"
        elif userinfo["nickname"] == "enfermero":
            role = "Enfermero"
        # role = userinfo.get('widmy-g3.com/role')  # Replace 'widmy-g3.com/role' with the actual role claim name
        print("role: ", role)

        return role
    except UserSocialAuth.DoesNotExist:
        return None