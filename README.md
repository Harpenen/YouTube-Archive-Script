# YouTube-Archive-Script
A simple script that archives YouTube videos.
youtube-dl.exe is required, and can be found at https://github.com/ytdl-org/youtube-dl/releases
Works on windows, currently does not work on Linux.
Currently unfinished.

# Dependencies
You will need python3 installed to run the script. Which version of python3 you have shouldn't matter but this was written for python3.9.
youtube-dl.exe is required and can be found here https://github.com/ytdl-org/youtube-dl/releases .
ffmpeg isn't needed, but is recommended. without it the video may end up looking like sh**. it can be found here https://www.ffmpeg.org/download.html#releases .
The program uses the python modules "os", "subprocess", and "time". These are included with python normally and should not need to be installed.

# Use Instructions
MAKE SURE YOU HAVE ENOUGH DISK SPACE IF YOU ARE DOWNLOADING LONG AND/OR MANY VIDEOS!!
Download youtubearchive.py and place it in an isolated folder.
Get youtube-dl.exe from https://github.com/ytdl-org/youtube-dl/releases and place it in the same folder as youtubearchive.py.
(RECOMMENDED) Get FFmpeg from https://www.gyan.dev/ffmpeg/builds/ or https://github.com/BtbN/FFmpeg-Builds/releases and move ffnpeg.exe from the bin folder to the same folder as youtubearchive.py.
Open youtubearchive.py with a text editor and change the iden variable to the video's ID. Make sure to save (Ctrl+S).
Run youtubearchive.py, make sure you have .py files set to open with the python interpreter.
The script will download the video to youtubearchive.py's directory in \videos\CHANNELID\VIDEOID\ .
All subtitles for the video, the video's thumbnail, and the video's metadata will also be downloaded.

# Errors
If you get a "HTTP Error 403: Forbidden" type error, just wait a minute or so and try again.
If you get "The uploader has not made this video available in your country", the video is blocked in your country, and you should try using a VPN. If you know of a better way to bypass geo-restrictions please let me know.
