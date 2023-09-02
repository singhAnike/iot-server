import os
import django
import requests
from django.middleware.csrf import get_token
from django.http import HttpRequest

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

# Create a dummy HttpRequest object
request = HttpRequest()

# Obtain the CSRF token
csrf_token = get_token(request)

# Define the API endpoint URL
url = 'http://127.0.0.1:8000/api/data/'

# Define the data you want to send in the POST request
data = {'key1': 'value1', 'key2': 'value2'}

# Include the CSRF token in the headers
headers = {'X-CSRFToken': csrf_token}

# Send the POST request with headers
response = requests.post(url, json=data, headers=headers)

# Check the response status code and content
if response.status_code == 200:
    print('POST request successful!')
    print('Response:', response.text)
else:
    print('POST request failed with status code:', response.status_code)
