#!/usr/bin/env python
# coding: utf-8
# 參考資料
# https://github.com/SurpassHR/Youtube_SignatureCipher_Decryptor
# https://github.com/streamlink/streamlink/blob/master/src/streamlink/plugins/youtube.py
# https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/youtube.py
# https://stackoverflow.com/questions/21510857/best-approach-to-decode-youtube-cipher-signature-using-php-or-js
# https://stackoverflow.com/a/68492807



# https://github.com/wayne931121/Python_URL_Decode

def decodeURIComponent(b):
# https://zh.wikipedia.org/zh-tw/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81
# %21 mean 21hex, => int("21",16) => 33 => chr(33) => "!", result: "!"
    if type(b)==bytes:
        b = b.decode(encoding="utf-8") #byte can't insert utf8 charater
    result = bytearray()
    enter_hex_unicode_mode = 0
    hex_tmp = ""
    now_index = 0
    for i in b:
        if i=='%': #like %51%52, have entered mode, continue appending bytearray
            enter_hex_unicode_mode = 1
            continue
        if enter_hex_unicode_mode:
            hex_tmp += i
            now_index += 1
            if now_index==2: #%51%5F len("51")=2 len("5F")=2
                result.append(int(hex_tmp, 16) )
                hex_tmp = ""
                now_index = 0
                enter_hex_unicode_mode = 0
            continue
        result.append(ord(i))
    result = result.decode(encoding="utf-8")
    return result

#保留字元的百分號編碼
URL_RFC_3986 = {
"!": "%21", "#": "%23", "$": "%24", "&": "%26", "'": "%27", "(": "%28", ")": "%29", "*": "%2A", "+": "%2B", 
",": "%2C", "/": "%2F", ":": "%3A", ";": "%3B", "=": "%3D", "?": "%3F", "@": "%40", "[": "%5B", "]": "%5D",
}

def encodeURIComponent(b):
    # https://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81
    if type(b)==bytes:
        b = b.decode(encoding="utf-8") #byte can't insert utf8 charater
    result = bytearray() #bytearray: rw, bytes: read-only
    for i in b:
        if i in URL_RFC_3986:
            for j in URL_RFC_3986[i]:
                result.append(ord(j))
            continue
        i = bytes(i, encoding="utf-8")
        if len(i)==1:
            result.append(ord(i))
        else:
            for c in i:
                c = hex(c)[2:].upper()
                result.append(ord("%"))
                result.append(ord(c[0:1]))
                result.append(ord(c[1:2]))
    result = result.decode(encoding="ascii")
    return result

def request(url, headers={}): #下載原始碼，Download Source Code。
    req = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    response.close()
    return data

def pretty_print(d):
    if "video" in d['mimeType']:
        i = [d['mimeType'], d['width'], d['height'], d['qualityLabel'].upper(), d['fps'], d['contentLength']]
        s = "Type: %s, W×H %d×%d %s, Fps %d, ContentLength %s. "%(*i, )
        print(s)
        return None
    if "audio" in d['mimeType']:
        i = [d['mimeType'], d['bitrate'], d['audioSampleRate'], d['audioChannels'], d['audioQuality'], d['contentLength']]
        s = "Type: %s, Bitrate %d, Rate %s, Channels %d, Quality %s, ContentLength %s. "%(*i, )
        print(s)
        return None

def pretty_print_assign(d):
    if "video" in d['mimeType']:
        i = [d['mimeType'], d['width'], d['height'], d['qualityLabel'].upper(), d['fps'], d['contentLength']]
        s = "Type: %36s, W×H %5d×%5d %9s, Fps %3d, ContentLength %s. "%(*i, )
        print(s)
        return None
    if "audio" in d['mimeType']:
        i = [d['mimeType'], d['bitrate'], d['audioSampleRate'], d['audioChannels'], d['audioQuality'], d['contentLength']]
        s = "Type: %36s, Bitrate %7d, Rate %6s, Channels %1d, Quality %21s, ContentLength %s. "%(*i, )
        print(s)
        return None

# The core function to decrypt
def Rwa(a):
    a=list(a);RB["ss"](a, 4);RB["jM"](a,6);RB["jM"](a,45);RB["e0"](a,3);return "".join(a)
def ss(a, *args):
    a.reverse()
def jM(a, b):
    c=a[0];a[0]=a[b%len(a)];a[b%len(a)]=c
def e0(a, b):
    for e in range(0,b)[::-1]: a.pop(e)

class Decrypt_2022_10_29_zh_TW():
    def __init__(self):
        self.decrypt_function = [] # (self.elements, self.execute)
        self.signature_cipher = ""
        self.function_name = ""
        self.execute = [] # execute = [($function_name, $arg), ...]
        self.elements = {} # elements = {$function_name: $function, ...}
        return None
    def __call__(self, content):
        result = self.decrypt(content)
        return result
    def decrypt(self, content, prt=0): # content: base.js source code => str
        self.__init__()
        ######################################################################################################################
        """
        Regex:
        
        \w{2}=function\(a\){a=a\.split\(""\).+?return a\.join\(""\)};
        
        Example:
        
        EA=function(a){a=a.split("");DA.ss(a,4);DA.jM(a,6);DA.jM(a,45);DA.e0(a,3);return a.join("")};
        """
        decrypt = re.search('\\w{2}=function\\(a\\){a=a\\.split\\(""\\)(?P<elements>.+?)return a\\.join\\(""\\)};', content)
        if not decrypt: return -1
        if prt: print(decrypt[0])
        ######################################################################################################################
        """
        Regex:
        
        \w{2}.\w{2}\(a,\d+\)
        
        Example:
        
        DA.ss(a,4)
        DA.jM(a,6)
        DA.jM(a,45)
        DA.e0(a,3)
        """
        re.sub('(?P<function_name>\\w{2}).(?P<element_function_name>\\w{2})\\(a,(?P<arg>\\d+)\\)', self.process, decrypt[0])
        if not self.execute: return -2
        ######################################################################################################################
        """
        Regex:
        
        var %2s={(\w{2}:function\(a(,b)?\){.+?},?\n?)+};
        
        Example: 
        
        var DA={ss:function(a){a.reverse()},
        jM:function(a,b){var c=a[0];a[0]=a[b%a.length];a[b%a.length]=c},
        e0:function(a,b){a.splice(0,b)}};
        """
        core = re.search('var %s={(\\w{2}:function\\(a(,b)?\\){.+?},?\\n?)+};'%self.function_name, content)
        if not core: return -3
        core = core[0]
        if prt: print(core)
        ######################################################################################################################
        """
        Regex:
        
        \w{2}:function\(a\){a\.reverse\(\)}
        \w{2}:function\(a,b\){var c=a\[0\];a\[0\]=a\[b%a\.length\];a\[b%a\.length\]=c}
        \w{2}:function\(a,b\){a.splice\(0,b\)}
        
        Example:
        
        define elements                                                  => elements = {}
        ss:function(a){a.reverse()}                                      => elements["ss"]=ss
        jM:function(a,b){var c=a[0];a[0]=a[b%a.length];a[b%a.length]=c}  => elements["jM"]=jM
        e0:function(a,b){a.splice(0,b)}                                  => elements["e0"]=e0
        """
        # example elements = {"ss": ss, "jM": jM, "e0": e0}
        e = re.search('(?P<name>\\w{2}):function\\(a\\){a\\.reverse\\(\\)}', core)["name"]
        self.elements[e] = ss
        e = re.search('(?P<name>\\w{2}):function\\(a,b\\){var c=a\\[0\\];a\\[0\\]=a\\[b%a\\.length\\];a\\[b%a\\.length\\]=c}', core)["name"]
        self.elements[e] = jM
        e = re.search('(?P<name>\\w{2}):function\\(a,b\\){a.splice\\(0,b\\)}', core)["name"]
        self.elements[e] = e0
        ######################################################################################################################
        self.decrypt_function = (self.elements, self.execute)
        if prt:
            print(self.elements)
            print(self.execute)
        return self.decrypt_function
    def process(self, match):
        element_function_name = match["element_function_name"]
        arg = int(match["arg"])
        self.function_name = match["function_name"]
        self.execute.append((element_function_name, arg))
        return match[0]
    def Decrypt_Signature_Cipher(self, SignatureCipher):
        SignatureCipher = decodeURIComponent(SignatureCipher)
        SignatureCipher = list(SignatureCipher)
        for i in self.execute:
            function_name, arg = i
            function = self.elements[function_name]
            function(SignatureCipher, arg)
        SignatureCipher = encodeURIComponent(SignatureCipher)
        self.signature_cipher = SignatureCipher
        return SignatureCipher

def audio_size(d):
    return d['bitrate']*int(d['audioSampleRate'])*int(d['audioChannels'])

def video_size(d):
    return d['width']*d['height']*d['fps']

#https://github.com/wayne931121/Https/blob/main/https_client.py
def client(url, conn_index, index, datas, buffersize=4096):
    prt = 0
    reg = '(?P<url>(?:(?P<protocol>https?):\\/\\/)?(?P<domain>(?:[\\w\\d\\-]+\\.)+[\\w\\d\\-]+)(?::(?P<port>\\d+))?(?P<path>(?:\\/[^\\/\\"\'\\n?]*)*\\/?(?:\\?(?P<arg>[^"\'\\r\\n]*))?))'
    reg1 = b'Content-Length: (?P<length>\\d+)'
    content_finder = re.compile(reg1)
    url_ = re.search(reg, url)
    url = url_["url"]
    port = url_["port"]
    webpage = url_["path"]
    hostname = url_["domain"]
    protocol = url_["protocol"]
    if not webpage: webpage = "/"
    port =  "443"
    request_args = [webpage, hostname, port, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"]
    request = bytes("GET %s HTTP/1.1\r\nHost: %s:%s\r\nConnection: keep-alive\r\nUser-Agent: %s\r\n\r\n"%(*request_args, ), encoding = "utf-8")
    context = ssl._create_unverified_context()  #ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.connect((hostname, int(port)))
    conn.sendall(request)
    conn.settimeout(10)
    recive = b"" # $recive <- All we recive
    recive_tmp = b""
    recive_content = b""
    recive_headers = b""
    eof_data = b""
    #print("Request:\n %s\n"%request) #print the request we sended to server.
    while 1:
        try:
            recive_tmp = conn.recv(buffersize) #first response will include headers. #Include content length(hex).
            recive += recive_tmp
            if prt:
                print(recive_tmp)
            if b"\r\n\r\n" in recive_tmp:
                recive_headers, eof_data = recive.split(b"\r\n\r\n")
                break
        except socket.timeout as e:
            print("TIME OUT")
    #The normal recive_tmp: "$headers\r\n\r\n" -> next recv
    #The fact recive_tmp: "$headers\r\n\r\n......some data after '\r\n\r\n'......" -> next recv
    #The length is the length in Content-Length Header Value
    length = content_finder.search(recive)
    recive_content = eof_data + recive_file(conn, int(length["length"]), eof_data, buffersize)
    datas[index] = recive_content #在被分配好的陣列區塊存入媒體數據，store media datas to datas arrays assign index.
    conn.shutdown(socket.SHUT_WR)
    conn.close()
    conn_index.append(None) #conn_index的長度代表完成幾個進程，len(conns) is the the threading quantity that completed。
    return 0

def recive_file(conn, length, eof_data, buffersize):
    i = 0 # i is now length of all data we have recv.
    i += len(eof_data)
    recive = b""
    recive_tmp = b""
    while 1:
        try:
            recive_tmp = conn.recv(buffersize)
            i += len(recive_tmp)
        except socket.timeout as e:
            print("TIME OUT 3s")
            break
        if i>=length :
            recive += recive_tmp[:length-i] if i>length else recive_tmp
            break
        if not recive_tmp: break #recive_tmp = b''
        recive += recive_tmp
    return recive

def media_connect(media, filename): #快取大小65536, buffersize=65536
    media["contentLength"] = int(media["contentLength"])
    conns = [] #此長度為完成的進程數 len(conns) is the the threading quantity that completed
    index = 0 #開過的進程數 all the threading quantity including completed or not completed
    i = 0
    mod = 1 if media["contentLength"]%65536!=0 else 0
    datas = [b'' for i_ in range(media["contentLength"]//65536+mod)]
    limit = 9 #最多併發進程
    while i<media["contentLength"]:
        if index-len(conns)<limit:
            start, end = i, min(i+65535, media["contentLength"]-1)
            url = media["url"]+"&range=%d-%d"%(start, end)
            threading.Thread(target=client, args=(url, conns, index, datas)).start()
            i = end+1
            sys.stdout.write("\rRange: %d-%d %02d"%(start, end, i/media["contentLength"]*100)+"%")
            sys.stdout.flush()
            index += 1
        time.sleep(0.1)
    while len(conns)<index: #等待進程結束 waiting for all threading complete
        time.sleep(0.01)
    with open(filename, "wb") as f:
        f.write(b"".join(datas))
    print("")
    return datas

def media_download(video, audio, title):
    print("Downloading Video And Audio...")
    video_filename = "%s_video.%s"%(title, video["mimeType"].split("/")[1].split(";")[0])
    audio_filename = "%s_audio.%s"%(title, audio["mimeType"].split("/")[1].split(";")[0])
    video_datas = media_connect(video, video_filename) #下載影片視頻資料 Download video data
    audio_datas = media_connect(audio, audio_filename) #下載影片音訊資料 Download audio data
    cmd = 'ffmpeg -i "%s" -i "%s" -c:v libx264 -c:a aac -y "%s.mp4"'%(video_filename, audio_filename, title)
    print("\nTransform Type:\n%s\n"%cmd)
    os.system(cmd)
    os.remove(video_filename)
    os.remove(audio_filename)
    datas_getter = lambda :(video_datas, audio_datas) #不能直接印出資料，因為影片資料太大可能造成電腦當機。
    return datas_getter

def process_title(match):
    # https://stackoverflow.com/questions/29314231/what-is-39-and-why-does-google-search-replace-it-with-apostrophe
    return chr(int(match["ascii_code"]))

def list_availbale(datas): #列出影片所有可用資訊，包含畫質大小。
    for e in datas:
        pretty_print_assign(e)
    return 0

def Main(quality="", prt=1, prt_full=0, list_all=False, download=False):
    if quality not in ["best", "Best", ""]:
        try:
            quality = int(quality)
        except:
            print("Not pretty set quality, use default all quality.")
            quality = ""
    elif quality=="Best":
        quality = "best"
    print("Download Source Code From Youtube...")
    decrypt = Decrypt_2022_10_29_zh_TW()
    html = request(url)
    yt = re.search(b"var ytInitialPlayerResponse = (?P<ytInitialPlayerResponse>{(?:[^;]+; codecs)*[^;]+);", html)
    js = re.search(b'jsUrl":"(?P<url>.+?base.js)"', html) # Example:"jsUrl":"/s/player/19fc75cf/player_ias.vflset/zh_TW/base.js"
    title = re.search(b'<meta name="title" content="(?P<title>.+?)">', html)
    
    if not yt or not js or not title:
        print("ERROR -1: not yt js title")
        #print(content)
        raise Exception(-1)
    yt = yt["ytInitialPlayerResponse"]
    js = js["url"]
    title = title["title"].decode(encoding="utf-8")
    title = re.sub('&#(?P<ascii_code>\d{0,3});', process_title, title)
    try:
        yt = json.loads(yt)
    except Exception as e:
        print(e)
        #print(yt)
        raise Exception(-2)
    
    datas = yt["streamingData"]["adaptiveFormats"] if yt["streamingData"]["adaptiveFormats"] else yt["streamingData"]["formats"]
    flag = "signatureCipher" in datas[0] #是否加密
    videos = []
    audios = []
    i = 0
    
    if list_all:
        list_availbale(datas)
        return (0, 0, 0)
    
    if flag:
        js = 'https://www.youtube.com'+js.decode(encoding="utf-8")
        print("Download Source Code From %s"%js)
        js = request(js).decode(encoding="utf-8")
        status = decrypt.decrypt(js, prt=prt_full)
        if (type(status)==int) and (status<0): raise Exception("Error: code %d"%status)
    
    while i<len(datas):
        media_url = ""
        sigcipher = ""
        data = datas[i]
        if flag:
            a = [e.split("=") for e in data["signatureCipher"].split("&")]
            media_url = decodeURIComponent(a[2][1])
            sigcipher = a[0][1]
            if prt_full: print("\n\nSignature Cipher: "+sigcipher)
        else:
            media_url = data["url"]
        
        if sigcipher: 
            sigcipher = decrypt.Decrypt_Signature_Cipher(sigcipher)
            media_url = media_url+"&alr=yes&sig="+sigcipher
        i += 1
        if prt and quality!="best" and (quality=="" or ("video" in data["mimeType"] and data["height"]==quality)):
            print("\n")
            pretty_print(data)
            print(media_url)
        data["url"] = media_url
        if "video" in data["mimeType"]:
            videos.append((video_size(data), media_url, data))
        if "audio" in data["mimeType"]:
            audios.append((audio_size(data), media_url, data))
    if prt and quality=="best":
        video = max(videos)
        audio = max(audios)
        print("\n")
        pretty_print(video[2])
        print(video[1])
        print("\n")
        pretty_print(audio[2])
        print(audio[1])
    download_datas = []
    if download:
        videos.sort()
        audios.sort()
        video = ""
        audio = ""
        if quality=="best" or quality=="":
            video = videos[-1][2]
        else:
            for video in videos[::-1]:
                if video[2]["height"]==quality:
                    video = video[2]
                    break
        audio = audios[-1][2]
        if not video or not audio:
            print("Quality Not Match URL")
            return -1
        print("\n")
        download_datas = media_download(video, audio, title)
    print("\ncomplete")
    return (videos, audios, download_datas)

"""
Test URL

https://www.youtube.com/watch?v=UF8uR6Z6KLc
https://www.youtube.com/watch?v=piEyKyJ4pFg
"""
import re, time, ssl, socket, sys, json, os
import subprocess, threading, argparse
import urllib.parse
import urllib.request

print("Get User Argument")
#Handle User Argument
parser = argparse.ArgumentParser(description="Youtube Video Downloader, Test on 2022.10.30 zh_TW.")
parser.add_argument("-url", "-u", help="input a youtube url", type=str, default="")
parser.add_argument("-list", "-l", help="List all information of a youtube video, like video quality.", action="store_true")
parser.add_argument("-quality", "-q", help="select a quality you want to view or download. Like Best, best, 1080, 720, 360, 240.", type=str, default="")
parser.add_argument("-download", "-d", help="download the video. (required install ffmpeg on your device.)", action="store_true")
parser.add_argument("-print", "-p", help="print the information and url that we get of a video", type=int, default=1)
parser.add_argument("-fullPrint", "-fp", help="print information and decrypt function that extract from base.js and other debug values", type=int, default=0)
args = parser.parse_args()
url, list_all, quality, download, prt, prt_full = args.url, args.list, args.quality, args.download, args.print, args.fullPrint
if not url:
    print("Input a url")
    url = input()
error = 0
while error<3:
    try:
        result = Main(quality, prt, prt_full, list_all, download)
        break
    except Exception as e:
        print("Error: %s, reconnecting to youtube."%e)
        error += 1
if error==3:
    print("Failed")





