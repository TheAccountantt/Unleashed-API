import requests
import pandas as pd
import datetime
import hashlib
import hmac
import base64

# Define your credentials
API_ID = "your_api_id"
API_KEY = "your_api_key"
API_BASE_URL = "https://api.unleashedsoftware.com/"

# List of endpoints to retrieve data from
endpoints = ["Invoices", "StockOnHand", "Accounts"]  # Add any other endpoints you need
page_number = 1  # Pagination, can iterate over multiple pages if needed

# Current date in the ISO format
current_date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

# Generate HMAC signature
def get_signature(args, api_key):
    key = bytes(api_key, 'utf-8')
    message = bytes(args, 'utf-8')
    signature = hmac.new(key, message, hashlib.sha256).digest()
    return base64.b64encode(signature).decode()

# Define headers for the request
def get_headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api-auth-id": API_ID,
        "api-auth-signature": get_signature("", API_KEY),
        "client-type": "YourCompany/YourAppName"
    }

# Loop through each endpoint and retrieve data
for endpoint in endpoints:
    url = f"{API_BASE_URL}{endpoint}/{page_number}"
    response = requests.get(url, headers=get_headers())

    # Check response
    if response.status_code == 200:
        data = response.json()
        # Assuming response contains a list of items, convert to DataFrame
        dataframe_name = f"df_{endpoint.lower()}"  # Naming the dataframe based on endpoint
        globals()[dataframe_name] = pd.json_normalize(data['Items'])
        # For Power BI, print the DataFrame
        print(globals()[dataframe_name])
    else:
        print(f"Failed to retrieve data for endpoint '{endpoint}': {response.status_code} - {response.text}")
