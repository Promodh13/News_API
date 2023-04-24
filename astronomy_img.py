import streamlit as st
import requests

st.set_page_config(layout="wide")

apikey = "4L0DijBdYgPCDe8V8PTE9nUAZPOUJfH3zXdaeYaB"

url = f"https://api.nasa.gov/planetary/apod?api_key={apikey}"

response = requests.get(url)
data = response.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

img_filepath = "img.png"
response1 = requests.get(image_url)
with open(img_filepath, 'wb') as file:
    file.write(response1.content)

st.title(title)
st.image(img_filepath)
st.write(explanation)