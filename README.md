# youtube downloader
download youtube video, decrypt signature cipher, test on 2022.10.29 zh_TW.

```cmd
C:\Users\Username\Downloads>python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg -h
Get User Argument
usage: youtube.py [-h] [-url URL] [-list] [-quality QUALITY] [-download] [-print PRINT]
                  [-fullPrint FULLPRINT] [-combine COMBINE] [-transform TRANSFORM]
                  [-remove REMOVE] [-audioOnly] [-videoOnly]

Youtube Video Downloader, Test on 2022.10.30 zh_TW.

optional arguments:
  -h, --help            show this help message and exit
  -url URL, -u URL      input a youtube url. (str)
  -list, -l             List all information of a youtube video, like video quality.
  -quality QUALITY, -q QUALITY
                        select a quality you want to view or download. Like Best, best, 1080,
                        720, 360, 240. (str, default:"")
  -download, -d         download the video. (required install ffmpeg on your device.)
  -print PRINT, -p PRINT
                        print the information and url that we get of a video. (int 1 or 0,
                        default:1)
  -fullPrint FULLPRINT, -fp FULLPRINT
                        print information and decrypt function that extract from base.js and
                        other debug values. (int 1 or 0, default:0)
  -combine COMBINE, -c COMBINE
                        after downloading, combine the video and audio or not. (int 1 or 0,
                        default:1)
  -transform TRANSFORM, -tr TRANSFORM
                        after downloading, transform the media format or not. (int 1 or 0,
                        default:1)
  -remove REMOVE, -r REMOVE
                        after downloading, remove the original medias we downloaded or not. (int
                        1 or 0, default:1)
  -audioOnly, -a        only download audio.
  -videoOnly, -v        only download video.
```
```cmd
Example:
python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg
python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg -list
python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg -q best -download
```
```cmd
C:\Users\Username\Downloads>python youtube.py -u https://www.youtube.com/watch?v=piEyKyJ4pFg -l
Get User Argument
Download Source Code From Youtube...
Type:      video/mp4; codecs="avc1.64002a", W×H  1920× 1080   1080P60, Fps  60, ContentLength 11491441.
Type:             video/webm; codecs="vp9", W×H  1920× 1080   1080P60, Fps  60, ContentLength 21524684.
Type:    video/mp4; codecs="av01.0.09M.08", W×H  1920× 1080   1080P60, Fps  60, ContentLength 20388193.
Type:      video/mp4; codecs="avc1.4d401f", W×H  1280×  720      720P, Fps  30, ContentLength 6739974.
Type:             video/webm; codecs="vp9", W×H  1280×  720      720P, Fps  30, ContentLength 8669807.
Type:      video/mp4; codecs="avc1.4d4020", W×H  1280×  720    720P60, Fps  60, ContentLength 4441714.
Type:             video/webm; codecs="vp9", W×H  1280×  720    720P60, Fps  60, ContentLength 8892222.
Type:    video/mp4; codecs="av01.0.08M.08", W×H  1280×  720    720P60, Fps  60, ContentLength 11289786.
Type:      video/mp4; codecs="avc1.4d401f", W×H   854×  480      480P, Fps  30, ContentLength 2481594.
Type:             video/webm; codecs="vp9", W×H   854×  480      480P, Fps  30, ContentLength 4589130.
Type:    video/mp4; codecs="av01.0.04M.08", W×H   854×  480      480P, Fps  30, ContentLength 4808813.
Type:      video/mp4; codecs="avc1.4d401e", W×H   640×  360      360P, Fps  30, ContentLength 1837997.
Type:             video/webm; codecs="vp9", W×H   640×  360      360P, Fps  30, ContentLength 3351050.
Type:    video/mp4; codecs="av01.0.01M.08", W×H   640×  360      360P, Fps  30, ContentLength 3175510.
Type:      video/mp4; codecs="avc1.4d4015", W×H   426×  240      240P, Fps  30, ContentLength 1131067.
Type:             video/webm; codecs="vp9", W×H   426×  240      240P, Fps  30, ContentLength 2204153.
Type:    video/mp4; codecs="av01.0.00M.08", W×H   426×  240      240P, Fps  30, ContentLength 2073347.
Type:      video/mp4; codecs="avc1.4d400c", W×H   256×  144      144P, Fps  30, ContentLength 707892.
Type:             video/webm; codecs="vp9", W×H   256×  144      144P, Fps  30, ContentLength 1780751.
Type:    video/mp4; codecs="av01.0.00M.08", W×H   256×  144      144P, Fps  30, ContentLength 1596870.
Type:        audio/mp4; codecs="mp4a.40.2", Bitrate  130494, Rate  44100, Channels 2, Quality  AUDIO_QUALITY_MEDIUM, ContentLength 3762144.
Type:            audio/webm; codecs="opus", Bitrate   60499, Rate  48000, Channels 2, Quality     AUDIO_QUALITY_LOW, ContentLength 1461482.
Type:            audio/webm; codecs="opus", Bitrate   79303, Rate  48000, Channels 2, Quality     AUDIO_QUALITY_LOW, ContentLength 1936759.
Type:            audio/webm; codecs="opus", Bitrate  150852, Rate  48000, Channels 2, Quality  AUDIO_QUALITY_MEDIUM, ContentLength 3822436.
```
Should you use this to download youtube video?<br>
A: No, use youtube-dl instead, because I may not maintain this project.

This project can do what?<br>
A: This project simply show you how to download youtube video use python.
This project include Decrypt_2022_10_29_zh_TW class that be used to decrypt signature cipher.

## How does this project work?
1. Get the youtube page source code.
2. Get video name, base.js url, video infomation from source code. The base.js is the script including decrpyt function, in the different video or time may have different base.js url in source code, and its decrypt function will have different name, argument, sequence, but same content inner function.
3. Extract the decrypt function inner base.js by using regex.
4. If this video is protected, use decrypt function to decrypt the signature cipher and add it to video url that both have been finded in video information.
5. Downloading video and audio by url use thread and range.
6. Using FFmpeg transform their format to mp4 (h264,aac).
7. Complete

## References:<br>
[https://github.com/SurpassHR/Youtube_SignatureCipher_Decryptor](https://github.com/SurpassHR/Youtube_SignatureCipher_Decryptor)<br>
[https://github.com/streamlink/streamlink/blob/master/src/streamlink/plugins/youtube.py](https://github.com/streamlink/streamlink/blob/master/src/streamlink/plugins/youtube.py)<br>
[https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/youtube.py](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/youtube.py)<br>
[https://stackoverflow.com/a/68492807](https://stackoverflow.com/a/68492807)

Also see:
[https://stackoverflow.com/a/74223304/19470749](https://stackoverflow.com/a/74223304/19470749)

## Write Downloading Code:

If you want to write this like me, first go youtube website seeing browser developer tools network, second go to see the youtube website source code, third go to see youtube base.js source code, you also need to use find function, set breakpoint in base.js. It is not needing that see the full source code, just roughly view to find some interesting infomation like googlevideo.com.

## Decrypt SignatureCipher:

If you want to decrypt signatureCipher, there is one thing to attention. When you get the decrypt function in base.js, that's not mean you get the currect decrypt function, because in different youtube video may have different base.js url and different decrypt function name, sequence, argument in it. If use wrong decrypt function or give full argument but some is error, rr$d---sn-$s-$s.googlevideo.com will keep 403 forbidden. If not give necessary parameter, it will response "404 Not Found. That’s an error". The real decrypt function in different base.js is not much different, it only change name, rearrange the real decrypt function, and replace the arguments that the real decrypt function will use (int). When you use the currect decrypt function, it will successfully get the video.<br>
When you want to find the decrypt function in base.js, the key words are: split(""), encodeURIComponent, decodeURIComponent, signature, sig.<br>
In 2022.10.$day, it format like that:

```javascript
//Common
//Rwa(a){a.split("")...}
Rwa=function(a){a=a.split("");RB.ss(a,4);RB.jM(a,6);RB.jM(a,45);RB.e0(a,3);return a.join("")};
var RB={ss:function(a){a.reverse()},
jM:function(a,b){var c=a[0];a[0]=a[b%a.length];a[b%a.length]=c},
e0:function(a,b){a.splice(0,b)}};

//Qwa(a){a.split("")...}
Qwa=function(a){a=a.split("");PB.Co(a,14);PB.Co(a,14);PB.Zo(a,56);PB.GZ(a,2);return a.join("")};
var PB={Co:function(a,b){var c=a[0];a[0]=a[b%a.length];a[b%a.length]=c},
Zo:function(a){a.reverse()},
GZ:function(a,b){a.splice(0,b)}};

//Common
QE = function(a, b, c) {  //### This Function will decrypt signatureChiper ###//
    b = void 0 === b ? "" : b;
    c = void 0 === c ? "" : c;
    a = new g.SB(a,!0);
    a.set("alr", "yes");
    c && (c = Rwa(decodeURIComponent(c)), //### This Line will decrypt signatureChiper ###//
    a.set(b, encodeURIComponent(c)));
    return a
}

QE = function(a, b, c) {  //### This Function will decrypt signatureChiper ###//
    b = void 0 === b ? "" : b;
    c = void 0 === c ? "" : c;
    a = new g.SB(a,!0);
    a.set("alr", "yes");
    c && (c = Qwa(decodeURIComponent(c)), //### This Line will decrypt signatureChiper ###//
    a.set(b, encodeURIComponent(c)));
    return a
}

RE=function(a,b,c){b=void 0===b?"":b;c=void 0===c?"":c;a=new g.SB(a,!0);a.set("alr","yes");c&&(c=Rwa(decodeURIComponent(c)),a.set(b,encodeURIComponent(c)));return a};
```
What you can search in base.js is "{a=a.split("")", and continue search the function name inner just find.

You can also see the details in:<br>
https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/youtube.py#L1403

## Base.js

Base.js is the script which be use to decrypt signature cipher. 

Format:
```
Windows:

https://www.youtube.com/s/player/${Js_Id}/player_ias.vflset/${Country}/base.js
Android:

https://www.youtube.com/s/player/${Js_Id}/player-plasma-ias-tablet-${Country}/base.js
```
Here are some base.js url I catched: (2022/10/${day})<br>
[https://www.youtube.com/s/player/4bbf8bdb/player_ias.vflset/zh_TW/base.js](https://www.youtube.com/s/player/4bbf8bdb/player_ias.vflset/zh_TW/base.js)
[https://www.youtube.com/s/player/24c6f8bd/player_ias.vflset/zh_TW/base.js](https://www.youtube.com/s/player/24c6f8bd/player_ias.vflset/zh_TW/base.js)
[https://www.youtube.com/s/player/64588dad/player_ias.vflset/zh_TW/base.js](https://www.youtube.com/s/player/64588dad/player_ias.vflset/zh_TW/base.js)
[https://www.youtube.com/s/player/4bbf8bdb/player-plasma-ias-tablet-zh_TW.vflset/base.js](https://www.youtube.com/s/player/4bbf8bdb/player-plasma-ias-tablet-zh_TW.vflset/base.js)
[https://www.youtube.com/s/player/24c6f8bd/player-plasma-ias-tablet-zh_TW.vflset/base.js](https://www.youtube.com/s/player/24c6f8bd/player-plasma-ias-tablet-zh_TW.vflset/base.js)
[https://www.youtube.com/s/player/64588dad/player-plasma-ias-tablet-zh_TW.vflset/base.js](https://www.youtube.com/s/player/64588dad/player-plasma-ias-tablet-zh_TW.vflset/base.js)
