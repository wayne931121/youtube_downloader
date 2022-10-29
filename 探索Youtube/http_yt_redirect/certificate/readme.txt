# Generate key using openssl:
# To install openssl on windows x64, see here https://github.com/wayne931121/https_client
# Step:
# 1. Install Msys2 Shell
# 2. Install Gcc in mingw64
# 3. Download Source Code from https://github.com/openssl/openssl release
# 4. Run ./Configure
# 5. Finish
# Generate certificate and private key:
# https://www.xolphin.com/support/OpenSSL/Frequently_used_OpenSSL_Commands
# https://stackoverflow.com/questions/60030906/self-signed-certificate-only-works-with-localhost-not-127-0-0-1 # (net::ERR_CERT_COMMON_NAME_INVALID))
# https://helpcenter.gsx.com/hc/en-us/articles/115015960428-How-to-Generate-a-Self-Signed-Certificate-and-Private-Key-using-OpenSSL

```
openssl req -x509 -sha256 -nodes -days 3650 -newkey rsa:2048 -keyout privateKey.key -out certificate.crt -config req.cnf
```

# Check the Private Key and Certificate:
# openssl x509 -in certificate.crt -text
# openssl rsa -in privateKey.key -check
## if browser say "not private connection", install "certificate.crt" in your device.
## (Like Windows10, install certificate to "受信任的根憑證授權單位 Trusted Root Certification Authorities").
## To Delete certificate in windows, use Window+R, and type certmgr.msc.

```
# paste to req.cnf, and remove the last ", " in "IP:127.0.0.1, ......, IP:127.0.0.99, ", change to "IP:127.0.0.1, ......, IP:127.0.0.99"

for i in range(1,100):
    print("IP:127.0.0.%d,"%i, end=" ")
```