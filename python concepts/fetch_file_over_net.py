# pip install requests

"""
program to use requests library to read text content over web/internet/network
"""

import requests

url = "http://example.com/test.txt"
response = requests.get(url)

if response.status_code == 200:
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("File saved successfully!")
else:
    print("Download failed")

# # Option 2-------------------------------------------------------

# # If file is large (recommended approach)
# # For large files, use streaming:

# url = "http://example.com/test.txt"
# with requests.get(url, stream=True) as response:
#     response.raise_for_status()
#     with open("test.txt", "wb") as f:
#         for chunk in response.iter_content(chunk_size=8192):
#             f.write(chunk)
# print("File downloaded successfully!")