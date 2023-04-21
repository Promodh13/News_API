import requests
from send_email import send_email

api_key = "490151a62b4049ca8a9d1ffa73602ccc"
url = "https://newsapi.org/v2/everything?q="\
    "tesla&from=2023-03-21&sortBy=publishedAt&apiKey="\
    "490151a62b4049ca8a9d1ffa73602ccc"

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

body = ""
# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
