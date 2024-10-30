# Unleashed API Integration with Power BI Using Python

Unleashed is an inventory management software tool owned by Access Financials.

This project provides a solution for connecting the Unleashed API to Power BI using Python. The script allows you to fetch data from various endpoints such as Invoices, StockOnHand, and Accounts directly into Power BI, enabling real-time analysis and reporting.

## Prerequisites

- **Python**: Ensure Python is installed and configured with Power BI.
- **Packages**: Install the required packages using the following command:
  ```sh
  pip install requests pandas

  Unleashed API Credentials: You need an API ID and an API Key, available from your Unleashed account.
Instructions
Step 1: Set Up Your Python Script
Clone the Repository: Clone this repository to get started.

git clone <repository-url>
cd <repository-directory>

Edit Credentials: Open the Python script and update your credentials.

# Define your credentials

<vscode_annotation details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'> </vscode_annotation> API_ID = "your_api_id" API_KEY = "your_api_key"


### Step 2: Update Endpoints

Modify the `endpoints` list in the Python script to include the endpoints you need. You can add or remove endpoints based on your requirements.
```python
# List of endpoints to retrieve data from
endpoints = ["Invoices", "StockOnHand", "Accounts"]  # Add any other endpoints you need

Step 3: Run the Python Script in Power BI
Open Power BI Desktop.
Go to Home > Get Data > More > Python Script.
Paste the Script: Copy and paste the Python script provided into the Python script editor in Power BI.
Load the Data: After running the script, you will see tables for each endpoint. Select and load them into Power BI for further analysis.
Step 4: Refresh Data
Data Refresh: Each time you refresh your Power BI dataset, the Python script will be executed to fetch the most recent data from the Unleashed API.

Python Script Overview
Authentication: Uses HMAC-SHA256 to generate a signature for secure access.
Multiple Endpoints: The script fetches data from multiple endpoints and stores them in separate DataFrames.
Pagination: The script can be adjusted to handle pagination for large datasets.
Notes
Data Volume: For large datasets, consider using pagination to split data into manageable chunks.