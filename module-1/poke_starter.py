# Jeff Peterson
# ASTR119
# poke.py
# Calculates number of bytes read from a URL and the download rate in MB/s
#Run with: python poke.py

import requests
import time

#url = 'http://ucsc.edu'
url =(input("Enter a URL: "))

#response = requests.get(url)
start = time.time()
response = requests.get(url)
end = time.time()
elapsed = end - start

nbytes = len(response.content)
mbytes = nbytes / 1e6 #1 million bytes = 1 megabyte
rate = mbytes / elapsed #megabytes per second

print(f"{nbytes} bytes read from {url}")
print(f"Download rate: {rate:.3g} MB/s")