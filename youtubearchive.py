import subprocess #imports subprocess, which is used to run windows commands through python
import time #used for grabbing unix time and making program wait to close
import os #allows me to grab the current directory, among many other functions

direc=(os.path.dirname(__file__)+"\\") #grabs the directory of the current script
oop=('-o "'+direc+"youtube\\%(channel_id)s\\%(id)s\\%(title)s.%(ext)s"+'" ') #ensures the video will be properly named and saved in the correct location
oper=("-i -w --all-subs --write-thumbnail --write-info-json --audio-quality 0 -f bestvideo+bestaudio/best ") #other paramaters that download more of the video's data

iden="" #enter the video or playlist ID to be downloaded here, example "dQw4w9WgXcQ"

now=str(int(time.time())) #grabs the time in unix time
logs=(direc+"logs\\"+now+".log") #creates the location to place the log file, and how to name the log file
l=" | tee "+logs+" -a" #placed at the end of the command to ensure output is saved to console and file

cmd=(direc+"youtube-dl.exe "+oop+oper+'"'+iden+'"'+l) #creates the command that will download the video

subprocess.call("echo "+cmd,shell=True) #prints the command both to console and to the log file
subprocess.call(cmd,shell=True) #runs the command, downloading the selected video
time.sleep(2) #waits before ending the program
