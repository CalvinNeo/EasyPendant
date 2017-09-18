#coding:utf8

import os
import shutil
from nt import chdir
import re

file_ext = {
    'cpp' : ".c.cpp.h.hpp"
    ,'lex' : ".l"
    ,'bison' : ".y"
    ,'markdown' : ".md"
}



def valid_ext(ext, langs):
    for lang in langs:
        e = file_ext[lang].split(".")
        e.remove("")
        if ext in e:
            return True
    return False

def walk(path, langs, exclude_files, exclude_pats):
    pats = [] 
    res = []
    for p in exclude_pats:
        pats.append(re.compile(p))
    for path, dirs, files in os.walk(path):
        for fn in files:
            full_path = path + "\\" + fn
            subfix = os.path.splitext(fn)[1][1:]
            name = os.path.splitext(fn)[0]
            skip = True
            if valid_ext(subfix, langs):
                skip = False
            if not skip:
                for f_test in exclude_files:
                    if f_test == fn:
                        skip = True
            if not skip:
                for re_test in pats:
                    if re_test.search(full_path):
                        skip = True
            if not skip:
                try:
                    fd = open(full_path, "r")
                    content = fd.read()
                    res.append(content)
                except:
                    pass
    return '\n'.join(res)

if __name__ == '__main__':
    print walk(ur"", ["cpp"], [], ["git", "vsbuild", "\.flex\.cpp", "\.tab\.cpp", "demos"])