import os
import random
import time
from subprocess import Popen

directory = os.path.join(os.path.dirname(os.path.realpath(file)), 'videos')

videos = []

def getVideos():
global videos
videos = []
for file in os.listdir(directory):
if file.lower().endswith('.mp4'):
videos.append(os.path.join(directory, file))

def playVideos():
global videos
if len(videos) == 0:
getVideos()
time.sleep(5)
return
random.shuffle(videos)
for video in videos:
playProcess = Popen(['vlc', '--fullscreen', '--no-xlib', '--no-osd', '--loop', video])
playProcess.wait()

while True:
playVideos()
