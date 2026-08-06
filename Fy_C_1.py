# Fyers Combined 1

import os
import threading
import webbrowser
from dotenv import load_dotenv, set_key
from flask import Flask, request
from fyers_apiv3 import fyersModel
from werkzeug.serving import make_server

# Load environment variables
env_file = ".env"
load_dotenv(dotenv_path=env_file)

app = Flask(__name__)

captured_auth_code = None
server_instance = None

client_id = os.getenv("FYERS_CLIENT_ID")
secret_key = os.getenv("FYERS_SECRET_KEY")
redirect_uri = "http://127.0.0.1:5000/callback"
response_type = "code"
grant_type = "authorization_code"

auth_url = f"https://api-t1.fyers.in/api/v3/generate-authcode?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}&state=sample_state"


class ServerThread(threading.Thread):
    def __init__(self, app):
        super().__init__()
        self.server = make_server('127.0.0.1', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()


@app.route('/callback')
def callback():
    global captured_auth_code, server_instance
    captured_auth_code = request.args.get('auth_code')

    if not captured_auth_code:
        return "Failed to retrieve auth_code from FYERS callback.", 400

    threading.Thread(target=server_instance.shutdown).start()
    return "<h1>Authorization Successful!</h1><p>You can close this tab and return to PyCharm.</p>"


def get_fyers_auth_code():
    global server_instance, captured_auth_code
    captured_auth_code = None  # Reset state
    server_instance = ServerThread(app)
    server_instance.start()

    print("Opening browser for FYERS login...")
    webbrowser.open(auth_url)

    server_instance.join()
    return captured_auth_code


def get_access_token():
    """Primary function to generate and return the access token."""
    auth_code = get_fyers_auth_code()

    if not auth_code:
        raise RuntimeError("Failed to capture FYERS authorization code.")

    session = fyersModel.SessionModel(
        client_id=client_id,
        secret_key=secret_key,
        redirect_uri=redirect_uri,
        response_type=response_type,
        grant_type=grant_type
    )

    session.set_token(auth_code)
    response = session.generate_token()

    token = response.get('access_token', None)

    if token:
        set_key(env_file, "FYERS_ACCESS_TOKEN", token)
        print("Access token generated and saved to .env successfully!")
        return token
    else:
        raise RuntimeError(f"Failed to generate access token. Response: {response}")


# Allow running standalone to generate token manually
if __name__ == '__main__':
    access_token = get_access_token()
    print(f"Generated Access Token: {access_token}")
