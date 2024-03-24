import requests
import json
from gtts import gTTS
from mutagen.mp3 import MP3
from moviepy.editor import *
import random
import os
from moviepy.editor import VideoFileClip,concatenate_videoclips
import moviepy.editor as mpy
from moviepy.video.fx.all import crop
api_url = "https://reddit.com/r/amitheasshole/random.json?limit=1"
response = requests.get(api_url, headers = {'User-agent': 'your bot 0.1'})
print(response.status_code)
data = response.json()


selftext = data["data"]["children"][12]["data"]["selftext"]
text = json.dumps(selftext)

text = text.replace("\\n", " ")

print(text)
myobj = gTTS(text=text, lang='en', slow=False)
myobj.save("reddit.mp3")

audio = MP3("reddit.mp3")
length = round(audio.info.length)
print(length) 

clip = VideoFileClip("bg.mp4")
duration = round(clip.duration)
start = random.randint(10, duration - 60)
end = start + length + 2
clip = clip.subclip(start, end)
audio = AudioFileClip("reddit.mp3")
audioClip = CompositeAudioClip([audio])
clip.audio = audioClip
(w, h) = clip.size
cropped_clip = crop(clip, width=600, height=5000, x_center=w/2, y_center=h/2)
cropped_clip.write_videofile("FINAL.mp4")