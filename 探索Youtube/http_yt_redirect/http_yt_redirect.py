import os
import re
import sys
import ssl
import time
import zlib
import brotli
import socket
import signal
import datetime
import threading
###|("url":"https:\/\/(?P<domain1>[\da-z\.-]+\.googlevideo\.com))|("signatureCipher":"s=[^=]+=sig\\\u0026url=https:\/\/(?P<domain2>[\da-z\.-]+\.googlevideo\.com))|("https:\/\/(?P<domain3>youtube.com)")|("(?P<domain4>youtube.com)")|("\/\/(?P<domain5>[\w-]+.[\w-]+.com))|("https:\/\/(?P<domain6>[\w-]+.[\w-]+.com))')
# (?:"|')((?:https?:)?\/?\/?((?:[\da-z\.-]+\.)+[\da-z\.-]+)(?:\/[^\/\"'\n?]+)*\/?(\?[^"'\r\n]*)?)(?:"|')
url_finder = re.compile(b'(?:"|\')(?P<url>(?:https?:)?\\/?\\/?(?P<domain>(?:[\da-z\.-]+\\.){2}[\da-z\.-]+)(?:\\/[^\\/\\"\'\\n?]+)*\\/?(\\?(?P<arg>[^"\'\\r\\n]*))?)(?:"|\')')
cli_finder = re.compile('(?P<url>(?:(?P<protocol>https?):\\/\\/)?(?P<domain>(?:[\\w\\-]+\\.)+[\\w\\-]+)(?::(?P<port>\\d+))?(?P<path>(?:\\/[^\\/\\"\'\\n?]*)*\\/?(?:\\?(?P<arg>[^"\'\\r\\n]*))?))')
don_finder = re.compile(b'Host: (?P<domain>(?:[\\w\\-]+\\.)+[\\w\\-]+)')
sip_finder = re.compile(b'Host: (?P<ip>127.0.0.\d+)')
len_finder = re.compile(b'Content-Length: (?P<length>\\d+)')
abc_finder = re.compile(b'[a-z]')
nam_finder = re.compile(b'[^\w\d]')
hex_finder = re.compile(b'(?P<hex_value>[\dabcdefABCDEF]+\\r\\n)|(\\r\\n)')

def start_thread(function, args=()):
    start = threading.Thread(target=function,  args=args)
    start.setDaemon(True)
    start.start()
    return start

def signal_handler(sig, frame):
    print('Server is Stopped.')
    for i in ClientManager.domains:
        csv1.write(b"\""+i+b"\"\r\n")
    csv2.close()
    csv1.close()
    csv.close()
    sys.exit(0)

class HTTPS_REDIRECT_SERVER():
    def __init__(self, ip, domain, client_manager):
        self.ip = ip #str
        self.domain = domain #bytes
        self.port = 443
        self.crt = os.path.join("certificate/certificate.crt")
        self.key = os.path.join("certificate/privateKey.key")
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        self.context.load_cert_chain(self.crt, self.key)
        self.client_manager = client_manager
        start_server = start_thread(self.main)
        return None
    def main(self): #開個Socket當HTTPS SERVER於127.0.0.%d:443
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock = self.context.wrap_socket(sock, server_side=True)
            try:
                sock.bind((self.ip, self.port))
            except:
                print(2, self.ip, self.port)
            sock.listen(5)
            while 1:
                try:
                    conn, addr = sock.accept()
                    process_conn = start_thread(self.processer, args = (conn, addr)) #接到瀏覽器連接請求後丟給Processer函數處理
                except Exception as e:
                    print(e)
        return 0
    def processer(self, conn, addr): #處理從客戶端收到的connection
        request = conn.recv(1024)
        ip = bytes(self.ip, encoding="utf-8")
        domain = self.domain
        request = request.replace(ip, domain)
        self.client_manager([conn, request, domain])
        return 0

class HTTPS_MAIN_SERVER(HTTPS_REDIRECT_SERVER):
    def __init__(self, ip, domain, request_args, client_manager): #127.0.0.1, webserver, [webpage, domain(hostname), user_agent]
        self.timeout = 10
        self.request_args = request_args
        self.request = "GET %s HTTP/1.1\r\nHost: %s\r\nConnection: keep-alive\r\nUser-Agent: %s\r\n\r\n"
        self.as_client_context = ssl._create_unverified_context() #ssl.create_default_context()
        domain = bytes(domain, encoding="utf-8")
        super().__init__(ip, domain, client_manager)
        conn = self.as_client_context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
        conn.connect((domain, self.port))
        conn.settimeout(self.timeout)
        self.client_manager.domains[domain] = {"server": self, "ip": ip, }
        return None
    def processer(self, conn, addr): #處理從客戶端收到的connection
        request = conn.recv(1024)
        if b"watch?v=" in request.split(b"\r\n")[0] or request.split(b" ")[1]==b"/" or request.split(b" ")[1]==b"":
            try:
                self.request_args[-1] = request.split(b"User-Agent: ")[1].split(b"\r\n")[0].decode(encoding="utf-8")
            except Exception as e:
                print("User-Agent ERROR")
                print(e)
                sys.exit(-1)
            request = bytes(self.request%(*self.request_args, ), encoding = "utf-8")
        ip = bytes(self.ip, encoding="utf-8")
        domain = self.domain
        request = request.replace(ip, domain).replace(b"keep-alive", b"Close")
        self.client_manager([conn, request, domain])
        return 0

class client_manager(): #https client
    def __init__(self):
        self.domains = {} #{"example remote webserver domain": {"server": "HTTPS_REDIRECT_SERVER Object", "ip":"...", }, }
        self.server = ["127.0.0.", 3]
        self.yt_folder = "yt_folder"
        self.conns = []
        self.port = 443
        self.timeout = 10
        self.findex = 1
        self.context = ssl._create_unverified_context() #ssl.create_default_context()
        return None
    def __call__(self, element): #element: [conn, request, domain] 
        start_thread(self.connect, args=(element,))
    def main(self):
        pass
    def connect(self, e):
        anotherConn, request, domain = e
        conn = self.generate_domain(domain) #with webserver
        conn.send(request)
        csv.write(b"\"")
        csv.write(b"\",\"".join(request.split(b"\r\n")))
        csv.write(b"\"\r\n")
        recive = b""
        headers= b""
        eof_data = b""
        transfer_encoding_chunked = 0
        while 1:
            try: #We only care the first recive is including Content-Length or not, and know if this is transfer_encoding_chunked.
                recive += conn.recv(1024)
                if b"\r\n\r\n" in recive: break
            except socket.timeout as e:
                print("TIME OUT", request, "\n")
                return -1
        headers, eof_data = recive.split(b"\r\n\r\n")
        length = len_finder.search(recive)
        typ = "br" if b"Content-Encoding: br" in recive else "gzip" if b"Content-Encoding: gzip" in recive else "deflate" if b"Content-Encoding: deflate" in recive else "no"
        anotherConn.send(headers+b"\r\n\r\n") #.replace(b"keep-alive", b"Close")
        if length:
            length = int(length["length"], 16)
            recive += self.recive(conn, anotherConn, length, typ, eof_data)
        else:
            recive += self.recive_transfer_encoding_chunked(conn, anotherConn, eof_data)
            transfer_encoding_chunked = 1
        #anotherConn.shutdown(socket.SHUT_WR)
        #anotherConn.close()
        #conn.shutdown(socket.SHUT_WR)
        #conn.close()
        start_thread(self.write, args=(request, recive, typ, transfer_encoding_chunked, ))
    def decompress(self, typ, byte):
        return byte if typ=="no" else brotli.decompress(byte) if typ=="br" else zlib.decompress(byte, zlib.MAX_WBITS|16) if typ=="gzip" else zlib.decompress(byte, -zlib.MAX_WBITS)
    def compress(self, typ, byte):
        return byte if typ=="no" else brotli.compress(byte) if typ=="br" else zlib.compress(byte, zlib.MAX_WBITS|16) if typ=="gzip" else zlib.compress(byte, -zlib.MAX_WBITS)
    def recive(self, conn, anotherConn, length, typ, eof_data):
        i = 0
        recive = b""
        while 1:
            try:
                recive_tmp = conn.recv(1024)
            except socket.timeout as e:
                break
            except Exception as e:
                print(1, e)
                break
            if not recive_tmp: break #recive_tmp = b''
            i += len(recive_tmp)
            recive += recive_tmp
            if i>=length: break
        #try:
        #    send = self.decompress(typ, eof_data+recive)
        #    send = self.replace_domain(send)
        #    send = self.compress(typ, send)
        #except:
        #    send = self.replace_domain(eof_data+recive)
        try:
            #anotherConn.send(send)
            anotherConn.send(eof_data+recive)
        except Exception as e:
            print(2, e)
        return recive
    def recive_transfer_encoding_chunked(self, conn, anotherConn, eof_data):
        if eof_data: anotherConn.send(eof_data)
        recive = b""
        while 1:
            try:
                recive_tmp = conn.recv(1024)
            except socket.timeout as e:
                break
            except Exception as e:
                print(3, e)
                break
            if not recive_tmp: break #recive_tmp = b''
            #send_tmp = self.decompress(typ, recive_tmp)
            send_tmp = self.replace_domain(recive_tmp)
            try:
                #print(send_tmp)
                anotherConn.send(send_tmp)
            except Exception as e:
                print(4, e)
                break
            recive += recive_tmp
            if b"0\r\n\r\n" in recive_tmp: break  
        return recive
    def write(self, request, recive, typ, transfer_encoding_chunked=0):
        if not recive: return 0
        h = recive.split(b"\r\n\r\n")
        header = h[0]
        data = b"\r\n\r\n".join(h[1:])
        if transfer_encoding_chunked:
            data = hex_finder.sub(b"", data)
        try:
            data = self.decompress(typ, data)
        except:
            pass
        if not data: return 0
        csv2.write(b"\""+b"\",\"".join(header.split(b"\r\n"))+b"\",\"\",\"\",\"\",\"\",\"from\",\""+b"\",\"".join(request.split(b"\r\n"))+b"\"\r\n")
        filename = ""
        try:
            filename = request.split(b"\r\n")[0].split(b" ")[1].split(b"?")[0].split(b"/")[-1]
            if filename==b"":
                filename = "result_%d.html"
            else:
                filename = filename.decode(encoding="utf-8")
                filename = filename.split(".")
                if len(filename)==1:
                    filename = filename[0]+"_%d"
                else:
                    filename = ".".join(filename[:-1])+"_%d."+filename[-1]
        except:
            filename = "result_%d.html"
        filename = filename%self.findex
        try:
            with open(os.path.join(self.yt_folder, filename), "wb") as html:
                html.write(data)
            self.findex += 1
        except Exception as a:
            print(a)
        return 0
    def insert_domain(self, server_ip, hostname): #keep-alive #注意keep-alive不會中斷連接
        server = HTTPS_REDIRECT_SERVER(server_ip, hostname, self)
        self.domains[hostname] = {"server": server, "ip":server_ip, }
        return 0
    def generate_domain(self, hostname):
        conn = self.context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
        try:
            conn.connect((hostname, self.port))
        except:
            print(-1, hostname)
            return -1
        conn.settimeout(self.timeout)
        return conn
    def replace_domain(self, source_code):
        return url_finder.sub(self.replace, source_code)
        #def replace_domain(self, source_code):
        #    urls = url_finder.finditer(source_code) #call use next(url)
        #    for i in urls:
        #        #print(0, i["url"])
        #        domain = i["domain"] #, c.start("domain"), c.end("domain")
        #        if b"com.google.android" in domain or (not abc_finder.match(domain)): continue
        #        if not domain in self.domains:
        #            result = self.insert_domain(self.server[0]+str(self.server[1]), domain)
        #            if result<0: continue
        #            self.server[1] += 1
        #    for i in self.domains:
        #        source_code.replace(i, bytes(self.domains[i]["ip"], encoding="utf-8"))
        #    return source_code
        0
    def replace(self, i): # i[0]: match
        domain = i["domain"] if i["domain"] else i["domain1"] if i["domain1"] else i["domain2"] if i["domain2"] else i["domain3"] if i["domain3"] else i["domain4"] if i["domain4"] else i["domain5"] if i["domain5"] else i["domain6"]
        if b"com.google.android" in domain or (not abc_finder.match(domain)): return i[0]
        if not domain in self.domains:
            result = self.insert_domain(self.server[0]+str(self.server[1]), domain)
            if result<0: return i[0]
            self.server[1] += 1
        return bytes("%"+str(len(i[0]))+"s", encoding="utf-8")%(i[0].replace(domain, bytes(self.domains[domain]["ip"], encoding="utf-8")))
    def open_url(self, url, ip):
        url = cli_finder.search(url)
        if not url:
            print("URL FORM ERROR")
            sys.exit(-1)
        webpage = url["path"]
        hostname = url["domain"]
        protocol = url["protocol"]
        request_args = [webpage, hostname, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"]
        self.Main_HTTPS_Server = HTTPS_MAIN_SERVER(ip, hostname, request_args, self) # Main_HTTPS_Server
        return 0

csv = open("intercept.csv", "wb")
csv.write(b"Header\r\n")

csv1 = open("domain.csv", "wb")
csv1.write(b"Header\r\n")

csv2 = open("response.csv", "wb")
csv2.write(b"Header\r\n")

ClientManager = client_manager()
ClientManager.open_url(r"https://www.youtube.com/watch?v=piEyKyJ4pFg", "127.0.0.1")

print("Server started, visit https://127.0.0.1, (port:443)")

while 1: #在上面開進程，這裡負責處理按CTRL+C終止
    time.sleep(0.01)
    signal.signal(signal.SIGINT, signal_handler)