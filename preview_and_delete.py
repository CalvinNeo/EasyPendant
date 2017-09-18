#coding:utf8

# files
import os
import shutil
from nt import chdir

# utils
import re

# meta reading
from docx import Document
import docx
import win32com 

zippostfix = ['zip', 'tar', 'gz', '7z', 'rar', 'bz']
copyre = ['新 %s', '%s \([0-9]+\)']
delimwidth = 30

def list_correspond_zip(f):
    pass

def list_correspond_copy(f):
    pass

def delete_intact_folder_ifexist_zip(path):
    pass

def preview_doc(f):
    document = Document(f)
    docText =  '\n'.join([
        paragraph.text.encode('utf8') for paragraph in document.paragraphs if paragraph.text.encode('utf8').strip() != ''
    ])
    # http://www.jb51.net/article/17560.htm
    # 字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。 
    # decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。 
    # encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。 

    # ref http://stackoverflow.com/questions/2153920/returning-the-first-n-characters-of-a-unicode-string
    # 对utf8使用slicing可能会导致错误, 这里得先decode到内部码
    deuni = docText.decode('utf8')
    return deuni[0: min(200, len(docText))].encode('utf8')

def walk(path):
    for path, dirs, files in os.walk(path):
        # 返回值说明:
        # path-> 该path下的dirs和files
        # 所有的dirs都会成为path并被枚举子元素
    # for ele in os.listdir("F:\\Codes\\Python\\EasyPendant")
    #     # 返回值说明:
    #     # 返回path下的所有直接子元素
        for f in files:
            surfix = os.path.splitext(f)[1][1:]
            name = os.path.splitext(f)[0]
            if surfix == "docx":
                print "Preview %s" % name
                print '-' * delimwidth
                print preview_doc(os.path.join(path, f)).decode('utf8')
                print '-' * delimwidth
                print "[y/n] DELETE: y to delete, o to open, else to ignore..."
                if raw_input() == 'y':
                    print 'delete'

                
if __name__ == '__main__':
    walk(ur"C:/test")

