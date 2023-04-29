from dotenv import load_dotenv
import requests
import os

load_dotenv()

class Oauth:
    client_id=os.getenv("CLIENT_ID")
    client_secret=os.getenv("CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")
    scope = "identify%20email%20guilds"
    discord_login_url=os.getenv("DISCORD_LOGIN_URL")
    discord_token_url="https://discord.com/api/oauth2/token"
    discord_api_url="https://discord.com/api"

    @staticmethod
    def get_access_token(code):
        payload = {
            "client_id": Oauth.client_id,
            "client_secret": Oauth.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": Oauth.redirect_uri,
            "scope": Oauth.scope
        }

        access_token = requests.post(url = Oauth.discord_token_url, data = payload).json()
        return access_token.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = f"{Oauth.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}
 
        user_object = requests.get(url = url, headers = headers).json()
        return user_object

    @staticmethod
    def get_guilds(access_token):
        url = f"{Oauth.discord_api_url}/users/@me/guilds"
        headers = {"Authorization": f"Bearer {access_token}"}
 
        guilds = requests.get(url = url, headers = headers).json()
        return guilds