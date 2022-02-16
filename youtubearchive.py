import subprocess #imports subprocess, which is used to run windows commands through python
from time import sleep #allows the program to wait before closing
import os #allows me to grab the current directory, among many other functions

url="https://www.youtube.com/watch?v=" #generic youtube url stripped of its identifier, the id will be appended to this
direc=(os.path.dirname(__file__)+"\\") #grabs the directory of the current script
oop=('-o "'+direc+"videos\\%(channel_id)s\\%(id)s\\%(title)s.%(ext)s"+'" ') #ensures the video will be properly named and saved in the correct location
oper=("--all-subs --write-thumbnail --write-info-json ") #other paramaters that download more of the video's data

iden="" #enter the video ID to be downloaded here, example "dQw4w9WgXcQ"

cmd=(direc+"youtube-dl.exe "+oop+oper+url+iden) #creates the command that will download the video
print(cmd) #prints the command in the python terminal

subprocess.call(cmd,shell=True) #runs the command, downloading the selected video
sleep(5) #waits before ending the program