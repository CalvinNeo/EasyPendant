#coding:utf8
import os
from os.path import getsize, join

cmd1 = u"ffmpeg -i concat:\"{}\" -acodec copy -vcodec copy -f mp4 {}OTTTTT.mp4"
# cmd2 = u"ffmpeg -f concat -i {}list.temp -bsf:a aac_adtstoasc -acodec copy -vcodec copy -f mp4 {}OTTTTT.mp4"
cmd2 = u"ffmpeg -f concat -i {}list.temp -bsf:a aac_adtstoasc -acodec copy -vcodec copy -f mp4 {}OTTTTT.mp4"
p = u"F:\\TTT\\"
lst = u""
# flag = False
# for ele in os.listdir(p):
# 	sz = getsize(p + ele)
# 	if sz > 1000:
# 		if flag:
# 			lst += '|'
# 		else:
# 			flag = True
# 		lst += (p + ele)


for ele in os.listdir(p):
	sz = getsize(p + ele)
	if sz > 1000:
		lst += u"file '{}{}'\n".format(p, ele)
f = open(p + u"list.temp", "w")
f.write(lst.encode("utf8"))
f.close()
ccmd = cmd2.format(p, p)
print ccmd
# os.popen(ccmd)
# print "OK"