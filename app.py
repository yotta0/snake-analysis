from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

import re

options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
options.experimental_options['prefs'] = {
    'profile.managed_default_content_settings.images': 2,
}
options.add_argument('--headless')

params = "filetype"
extension = "pdf"
search_keywords = input('Please enter keywords to search for pdfs\r\n')
if len(search_keywords.split()) > 1:
    search_input = '+'.join(search_keywords.split())

url = f'https://www.google.com/search?q={search_keywords}+{params}+{extension}&num=1000'

driver = webdriver.Chrome(options=options)
driver.get(url)

minutes = float(input('Type how many in minutes do you want the program search for pdfs\r\n'))

for i in range(round(minutes * 60)):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

pdf_list = []

count = 0
for a in soup.find_all('a', href=True):
    count += 1
    if re.match('^https://.*\.pdf$', a['href']):
        url = a['href']
        pdf_list.append(url)

print(f'Found {len(pdf_list)} documents.')
df = pd.DataFrame({
    'documentos': pdf_list
})

archive_type = input('Type the archive type\r\n(csv or xlsx)\r\n')
if archive_type == 'csv':
    df.to_csv('links.csv', index=False, encoding='utf-8')
else:
    df.to_excel('links.xlsx', index=False)
