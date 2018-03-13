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
    deuni = docText.decode('utf8')
    return deuni[0: min(200, len(docText))].encode('utf8')

def walk(path, direct = False):
    # for ele in os.listdir(path) # for direct
    for path, dirs, files in os.walk(path):
        # path = dirs + files
        # All dirs will become path so as to be visited iteratively
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

