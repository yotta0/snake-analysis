import urllib.request
import requests as r

params = "filetype"
extension = "pdf"
search_input = input('Search here')
url = f'www.google.com/search?q={search_input}+{params}+{extension}'

# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(url) as response, open('document.pdf', 'wb') as out_file:
    data = response.read() # a `bytes` object
    out_file.write(data)