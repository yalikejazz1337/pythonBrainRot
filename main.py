import requests
import json
from gtts import gTTS
api_url = "https://reddit.com/r/amitheasshole/random.json?limit=1"
response = requests.get(api_url)
data = response.json()


selftext = data["data"]["children"][4]["data"]["selftext"]
text = json.dumps(selftext)

text = text.replace("\\n", "\n")
print(text)
myobj = gTTS(text=text, lang='en', slow=False)
myobj.save("reddit.mp3")


