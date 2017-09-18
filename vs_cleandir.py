#coding:utf8

import os
import shutil
from nt import chdir

if __name__ == '__main__':
    delfile = {'sdf', 'iobj', 'ipdb', 'obj', 'pdb', 'ilk', 'tlog', 'pch', 'ipch', 'db'}
    deldir = {'tlog'}
    prjbase = []
    for path, dirs, files in os.walk(r"F:\Codes\COMPETITION\ACM"):
        # 返回值说明:
        # path-> 该path下的dirs和files
        # 所有的dirs都会成为path并被枚举子元素
    # for ele in os.listdir("F:\\Codes\\Python\\EasyPendant")
    #     # 返回值说明:
    #     # 返回path下的所有直接子元素
        for f in files:
            surfix = os.path.splitext(f)[1][1:]
            if surfix == 'sln':
                prjbase.append(path + os.path.dirname(f))
                prjname = os.path.splitext(f)[0]
            if surfix in delfile:
                print "del file ",  f.decode('gbk').encode('utf8') 
                try:
                    os.remove(os.path.join(path, f))
                except WindowsError:
                    print "file removing failure at: ", f.decode('gbk').encode('utf8') 
        for d in dirs:
            surfix = os.path.splitext(d)[1][1:]
            if surfix in deldir:
                print "del dir ", d.decode('gbk').encode('utf8')
                try:
                    shutil.rmtree(os.path.join(path, d))
                except WindowsError:
                    print "directory removing failure at: ", d.decode('gbk').encode('utf8')

    for item in prjbase:
        print item.decode('gbk').encode('utf8')