__author__ = 'zhangxinzheng'
# -*- coding: utf-8 -*-
import sys
import re
import os
def f(filename):
    if filename.find("html") == -1:
        return
    targetName = filename.replace("html","md")
    fd = open(filename, "r+")
    str = ''.join(fd.readlines())
    while str.find("<pre") != -1:
        tempString="\n```\n"
        isContent = False
        startIndex = str.find("<pre")
        endIndex = len(str)
        realEnd = startIndex
        leftCount = 1
        rightCount = 0
        for j in xrange(startIndex, endIndex):
            if str[j] == '<':
                isContent = False
                leftCount +=1
            if isContent:
                tempString+=str[j]
            if str[j] == '>':
                isContent = True
                rightCount +=1
                realEnd = j
            if leftCount == rightCount:
                break
        str+="\n```\n"
        str=str.replace(str[startIndex:realEnd], tempString)
    fd.close()

    fd = open(targetName, "w+")
    fd.write(str)
    fd.close()
    os.remove(filename)

if __name__ == "__main__":
    for i in sys.argv:
        f(i)