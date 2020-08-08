import requests

param = {"q": "pizza"}
r = requests.get("http://bing.com/search", params = param)
print("Status:", r.status_code)
print(r.url)

f = open("./page.html", "w+")
f.write(r.text)
