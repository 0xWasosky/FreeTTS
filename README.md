# FreeTTS

## Chapters

1. Philosophy
2. Api docs 
3. Example in python 
4. Conclusion


## Philosophy

I have struggled to find sites that allow me to convert text to audio without a maximum character limit, so I wanted to build something that can help people solve this problem. :)


## Api docs

**gtt**: 

- Endpoint: **/api/v1/gtt**
- Method: **POST**
- Input data: **Text** and **Language** 
- Input data type: **Json**
- Output data: **Audio file** 
- Output data type: **File** 

Payload example: 

```json
{
    "text": "Hello im john doe", 
    "lang": "en" 
}
```

- Rate limit: **20 per minute**


**langs**:

- Endpoint: **/api/v1/langs**
- Method: **GET**
- Output data: **The supoorted languages** 
- Output data type: **Json** 
- Rate limit: **2 per minute**


## Example in Python

**To convert text to audio**:

```py
import requests


url = "https://0xwassoky.pythonanywhere.com/api/v1/gtt"

text = "hello"
lang = "en"

response = requests.post(url, json={"text": text, "lang": lang})


with open("hello.mp3", "wb") as f:
    f.write(response.content)
```

**To get the languages**:
```py
import requests


url = "http://127.0.0.1:5000/api/v1/langs"

response = requests.get(url)

print(response.json())
```


## Conclusion

I would like to thank everyone who will use this API, and I want to let you all know that you can find it at https://0xwassoky.pythonanywhere.com/."
