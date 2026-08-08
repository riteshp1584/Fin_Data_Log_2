import urllib.parse

api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # refer to PyCharm for keys
secret_key = 'XXXXXXXXXXXXXXXXXX' # refer to PyCharm for keys
red_url = urllib.parse.quote('https://127.0.0.1:5000', safe="")

url = f'https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={api_key}&redirect_uri={red_url}'
print(url)

# Click the Link below to generate code
