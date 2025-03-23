import requests


url = "https://0xwassoky.pythonanywhere.com/api/v1/langs"

response = requests.get(url)

print(response.json())