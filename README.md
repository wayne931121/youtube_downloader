# youtube_downloader
download youtube video, decrypt signature cipher, test on 2022.10.29 zh_TW.

```cmd
C:\Users\sky66\Downloads>python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg -h
Get User Argument
usage: youtube.py [-h] [-url URL] [-list] [-quality QUALITY] [-download] [-print PRINT] [-fullPrint FULLPRINT]

Youtube Video Downloader, Test on 2022.10.30 zh_TW.

optional arguments:
  -h, --help            show this help message and exit
  -url URL, -u URL      input a youtube url
  -list, -l             List all information of a youtube video, like video quality.
  -quality QUALITY, -q QUALITY
                        select a quality you want to view or download. Like Best, best, 1080, 720, 360, 240.
  -download, -d         download the video. (required install ffmpeg on your device.)
  -print PRINT, -p PRINT
                        print the information and url that we get of a video
  -fullPrint FULLPRINT, -fp FULLPRINT
                        print information and decrypt function that extract from base.js and other debug values
```
Should you use this to download youtube video?
A: No, use youtube-dl instead, because I may not maintain this project.

This project can do what?
A: This project simply show you how to download youtube video use python.
This project include Decrypt_2022_10_29_zh_TW class that be used to decrypt signature cipher

How does this project work?
1. Get the youtube page source code.
2. Get video name, base.js url, video infomation from source code. The base.js is the script including decrpyt function, in the different video or time may have different base.js url in source code, and its decrypt function will have different name, argument, sequence, but same content inner function.
3. Extract the decrypt function inner base.js by using regex.
4. If this video is protected, use decrypt function to decrypt the signature cipher and add it to video url that both have been finded in video information.
5. Downloading video and audio by url use thread and range.
6. Using FFmpeg transform their format to mp4 (h264,aac).
7. Complete
