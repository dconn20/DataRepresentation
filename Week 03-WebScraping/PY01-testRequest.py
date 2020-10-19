# Retrieve a web page from the web.

import requests

page = requests.get("https://github.com/dconn20/DataRepresentation")
print(page)
print("-----------------")
print(page.content)
