import os
from dotenv import load_dotenv

# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Load environment variables from the .env file
load_dotenv()

# Define your Fyers API credentials
client_id = os.getenv("FYERS_CLIENT_ID")  # Replace with your client ID
secret_key = os.getenv("FYERS_SECRET_KEY") # in .env file
redirect_uri = "http://127.0.0.1:5000/callback"  # Replace with your redirect URI
response_type = "code"
grant_type = "authorization_code"

# The authorization code received from Fyers after the user grants access
# Copy and Paste Every Run (generated from the output of Fyers_Work_1.py)
# be careful while copying end comma
auth_code = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIzOUVHMkNMUEtEIiwidXVpZCI6ImI2MzI5ZDcxMzFkMDRhYzc4Yzc4M2Q2MTE4YjU0MjMzIiwiaXBBZGRyIjoiIiwibm9uY2UiOiIiLCJzY29wZSI6IiIsImRpc3BsYXlfbmFtZSI6IllQMDYzODAiLCJvbXMiOiJLMSIsImhzbV9rZXkiOiJhZjg0NDE3Yzk1NzQ1ZjE0MzdiMTI2YTIwZDU5YjlkY2QyZWY0MDg3NTllYzhjYjIxNWZjYjMzMSIsImlzRGRwaUVuYWJsZWQiOiJOIiwiaXNNdGZFbmFibGVkIjoiTiIsImF1ZCI6IltcImQ6MVwiLFwiZDoyXCIsXCJ4OjBcIixcIng6MVwiXSIsImV4cCI6MTc4NTM0MDg3MiwiaWF0IjoxNzg1MzEwODcyLCJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJuYmYiOjE3ODUzMTA4NzIsInN1YiI6ImF1dGhfY29kZSJ9.vRlc6KS2HGXOTI1Gdo9CEDIhM8WJrwQaAj2r-wjJ6KQ"

# Create a session object to handle the Fyers API authentication and token generation
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token()

# Print the response, which should contain the access token and other details
print(response)

access_token = response.get('access_token', None)
if access_token:
    print(f"Access Token: {access_token}")
else:
    print(f"Access Token not found in the response")

