import os
from dotenv import load_dotenv
from flask import Flask, request, redirect

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

client_id = os.getenv("FYERS_CLIENT_ID")
redirect_uri = "http://127.0.0.1:5000/callback"
auth_url = f"https://api-t1.fyers.in/api/v3/generate-authcode?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&state=None"


@app.route('/')
def home():
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Print all query parameters for debugging purposes
    print("Request args:", request.args)

    auth_code = request.args.get('auth_code')
    state = request.args.get('state')

    # If the auth_code is None, it means the code parameter is not being passed correctly
    if auth_code is None:
        return "Failed to get authorization code. Please check the callback URL and parameters."

    return f"Authorization code: {auth_code}, State: {state}"

if __name__ == '__main__':
    app.run(debug=True)
