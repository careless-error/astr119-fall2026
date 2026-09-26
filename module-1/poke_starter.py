import requests

url = 'http://ucsc.edu'
response = requests.get(url)
nbytes = len(response.content)

print(f"{nbytes} bytes read from {url}")