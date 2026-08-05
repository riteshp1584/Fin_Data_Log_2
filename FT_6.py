from fyers_apiv3 import fyersModel
import json

client_id = "XC4XXXXM-100" # obtained by sample code in Fyers API documentation, no need to change in each run
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZDoxIiwiZDoyIiwieDowIiwieDoxIl0sImF0X2hhc2giOiJnQUFBQUFCcWFGWTVJZnlzY3BiLTRvY3RaUTBnNF84NmktUmUtdEhTb1FUaXNtR1c3di1XMExlSU1Tcnh4OVJ5THdTdmtxblFoY0pFNzdZTU1wTFJ0ZVpOZ0pOLW16N0VoNGs5bEdVdWZmRjBpdHR4blFkUE9QTT0iLCJkaXNwbGF5X25hbWUiOiIiLCJvbXMiOiJLMSIsImhzbV9rZXkiOiJkMDY4YzRmZDQzYzVkNDZkMzVhYWQ2NmY2ZGMzYThjNTA2ZDBkNDY2NzI2YmVmYjAwYzdkMTliYSIsImlzRGRwaUVuYWJsZWQiOiJOIiwiaXNNdGZFbmFibGVkIjoiTiIsImZ5X2lkIjoiWVAwNjM4MCIsImFwcFR5cGUiOjEwMCwiZXhwIjoxNzg1Mjg1MDAwLCJpYXQiOjE3ODUyMjI3MTMsImlzcyI6ImFwaS5meWVycy5pbiIsIm5iZiI6MTc4NTIyMjcxMywic3ViIjoiYWNjZXNzX3Rva2VuIn0.Cse5WS-um7M9wA7qO7wbh4x2Y7yiT2GZLQ-ZQI6r_vA"

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

# https://myapi.fyers.in/docsv3#tag/Data-Api/paths/~1DataApi/put for data parameters
data = {
    "symbol":"BSE:LATENTVIEW-A",
    "ohlcv_flag":"1"
}

response = fyers.depth(data=data)
# print(response)

pretty_json = json.dumps(response, indent=4)
print(pretty_json)
