#!/usr/bin/env python
# coding: utf-8

def combineFile(folder):
    s, g = os.listdir(folder), []
    mtyp = s[0].split(".")[-1] #media type
    filename = "_".join(".".join(s[0].split(".")[0:-1]).split("_")[0:-1])
    for i in s:
        g.append((int(".".join(i.split(".")[0:-1]).split("_")[-1]),i))
    g.sort()
    target = filename+"."+mtyp
    with open(target, "ab") as f:
        for i, file in g:
            with open(os.path.join(folder, file), "rb") as part:
                f.write(part.read())
    return target    

def main():
    print("Combine File...")
    v = combineFile(os.path.join(folder, "video"))
    a = combineFile(os.path.join(folder, "audio"))
    filename = "_".join(v.split("_")[0:-1])
    cmd = 'ffmpeg -i "%s" -i "%s" -c:v libx264 -c:a aac -y "%s.mp4"'%(v, a, filename)
    print(cmd)
    res = os.system(cmd)
    if res==0:
        os.remove(v)
        os.remove(a)
    return 0

import os, argparse

print("Get User Argument")
#Handle User Argument
parser = argparse.ArgumentParser(description="Youtube Video Downloader, Test on 2022.10.30 zh_TW.")
parser.add_argument("-folder", "-f", help="type the folder that is created by \"live.py\". (str)", type=str, default="")
args = parser.parse_args()
folder = args.folder

if not folder:
    print("Type the folder that is created by \"live.py\"")
    folder = input()

main()






