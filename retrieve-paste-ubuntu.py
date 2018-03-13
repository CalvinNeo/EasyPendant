#coding:utf8

# files
import os
import shutil
from nt import chdir

# utils
import re
import requests

def walk(path, subfixs = ['md']):
    file_lists = []
    for path, dirs, files in os.walk(path):
        # path = dirs + files
        # All dirs will become path so as to be visited iteratively
        for f in files:
            subfix = os.path.splitext(f)[1][1:]  # remove "."
            name = os.path.splitext(f)[0]
            if subfix in subfixs:
                file_lists.append(path + "/" + f.decode("gbk"))

    return file_lists

def take_field(fname):
    f = open(fname, "r")
    dat = f.read()
    pattern = re.compile(r'paste.ubuntu.com/\d+')
    ans = pattern.findall(dat)
    f.close()
    return ans

def get_content(url, dump_root):
    html = requests.get("https://" + url).text.encode("utf8")
    f = open(dump_root + url.replace("paste.ubuntu.com/", "") + ".html", "w")
    f.write(html)
    f.close()

if __name__ == '__main__':
    all_files = walk("F:/Codes/web/source/_posts")
    dump_root = "C:/dump/"
    for (i, fn) in enumerate(all_files):
        for url in take_field( fn ):
            print url
            get_content(url, dump_root)

