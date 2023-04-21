import requests
from send_email import send_email

topic = "tesla"

api_key = "490151a62b4049ca8a9d1ffa73602ccc"
url = f"https://newsapi.org/v2/everything?q={topic}&"\
    "from=2023-03-21&"\
    "sortBy=publishedAt&"\
    "apiKey=490151a62b4049ca8a9d1ffa73602ccc&" \
    "language=en"

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

body = ""
# Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" \
               + body + article["title"] + "\n" +\
               "\n" + article["url"]\
               + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
