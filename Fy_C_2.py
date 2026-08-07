import json
from fyers_apiv3 import fyersModel

# Import the function from Fyers_Combined_1.py
from Fyers_Combined_1 import get_access_token

# Hardcoded client ID as requested
client_id = "XC4XXXXM-100"

# Execute the function to open browser, authenticate, and receive access token
access_token = get_access_token()

# Initialize the FyersModel instance
fyers = fyersModel.FyersModel(
    client_id=client_id,
    token=access_token,
    is_async=False,
    log_path=""
)

# # Fetch market status
# response = fyers.market_status()

# https://myapi.fyers.in/docsv3#tag/Data-Api/paths/~1DataApi/post for data parameters
data = {
    "symbol":"NSE:OLAELEC-EQ",
    "resolution":"1W",
    "date_format":"1",
    "range_from":"2026-07-04",
    "range_to":"2026-08-04",
    "cont_flag":"1"
}

response = fyers.history(data=data)
# print(response)

# Print formatted output
pretty_json = json.dumps(response, indent=4)
print(pretty_json)
