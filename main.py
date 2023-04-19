import requests

api_key = "490151a62b4049ca8a9d1ffa73602ccc"
url = "https://newsapi.org/v2/everything?q=" \
        "tesla&from=2023-03-19&sortBy=publishedAt&apiKey=" \
        "490151a62b4049ca8a9d1ffa73602ccc"

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])