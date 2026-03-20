import requests 
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "id": 1,
    "name":"arjun",
    "role":"ai"
}
response = requests.post(url,json = data)
print(response.json())