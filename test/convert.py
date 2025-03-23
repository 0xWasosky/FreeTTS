import requests


url = "https://0xwassoky.pythonanywhere.com/api/v1/gtt"

text = "hello"
lang = "en"

response = requests.post(url, json={"text": text, "lang": lang})


with open("hello.mp3", "wb") as f:
    f.write(response.content)
