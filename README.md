Unleashed API Integration with Power BI Using Python

This project provides a solution for connecting the Unleashed API to Power BI using Python. The script allows you to fetch data from various endpoints such as Invoices, StockOnHand, and Accounts directly into Power BI, enabling real-time analysis and reporting.

Prerequisites

Python (configured with Power BI)

Packages: Install the required packages

Unleashed API Credentials:

You need an API ID and an API Key, available from your Unleashed account.

Instructions

Step 1: Set Up Your Python Script

Clone the Repository: Clone this repository to get started.

Edit Credentials: Open the Python script and update your credentials.

Step 2: Update Endpoints

Modify the endpoints list in the Python script to include the endpoints you need. 

You can add or remove endpoints based on your requirements.

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

Security: Keep your API credentials secure. Do not share them publicly.

Data Volume: For large datasets, consider using pagination to split data into manageable chunks.