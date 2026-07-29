import os
from dotenv import load_dotenv

# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Load environment variables from the .env file
load_dotenv()

# Define your Fyers API credentials
client_id = os.getenv("FYERS_CLIENT_ID")  # Replace with your client ID
secret_key = "**************"  # Check original code script in PyCharm, hidden here for privacy purposes
redirect_uri = "http://127.0.0.1:5000/callback"  # Replace with your redirect URI
response_type = "code"
grant_type = "authorization_code"

# The authorization code received from Fyers after the user grants access
# Copy and Paste Every Run (generated from the output of Fyers_Work_1.py)
# be careful while copying end comma
auth_code = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIzOUVHMkNMUEtEIiwidXVpZCI6ImJjYjVmNmFiMjg4MjQ2NDg5NzY2ZmFhMmM0MGI4YzIwIiwiaXBBZGRyIjoiIiwibm9uY2UiOiIiLCJzY29wZSI6IiIsImRpc3BsYXlfbmFtZSI6IllQMDYzODAiLCJvbXMiOiJLMSIsImhzbV9rZXkiOiJkMDY4YzRmZDQzYzVkNDZkMzVhYWQ2NmY2ZGMzYThjNTA2ZDBkNDY2NzI2YmVmYjAwYzdkMTliYSIsImlzRGRwaUVuYWJsZWQiOiJOIiwiaXNNdGZFbmFibGVkIjoiTiIsImF1ZCI6IltcImQ6MVwiLFwiZDoyXCIsXCJ4OjBcIixcIng6MVwiXSIsImV4cCI6MTc4NTI1NTk4NywiaWF0IjoxNzg1MjI1OTg3LCJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJuYmYiOjE3ODUyMjU5ODcsInN1YiI6ImF1dGhfY29kZSJ9.NTYaKA-M1d4eHhOwiR4EpOlmYuEqDfle8U4jDBFoNrc"

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

