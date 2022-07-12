from pygtrans import Translate
import numpy as np
import argparse 
import os

parser = argparse.ArgumentParser()
parser.add_argument('mytxt', help='your word list')
parser.add_argument('-n',type=int, help='word number')
parser.add_argument('-s',type=int, help='start from')
parser.add_argument('-l',type=int, help='line length')
parser.add_argument('--r', help='random or not',action="store_true")
args = parser.parse_args()

#store words and translation as dictionaries
dict={}
filehandler = open(args.mytxt,"r")
list = np.array(filehandler.readlines())

#根据start和length切片
if(args.s==None):
    args.s=0
if(args.l==None):
    args.l=len(list)
list_needed = list[args.s: args.s+args.l]

#根据number抽取单词
if(args.n==None):
    args.n=len(list)
vocab = np.random.choice(list_needed,args.n)

#决定是否随机打乱
if(args.r):
    np.random.shuffle(vocab)

for line in vocab:
    if(line!='\n'):
        word=line[0:len(line)-1]
        tran = Translate()
        text = tran.translate(word)
        dict[word]=text.translatedText

#quoted from csdn: Python解决创建新文件时避免覆盖已有的同名文件问题
def check_filename_available(filename):
    n=[0]
    def check_meta(file_name):
        file_name_new=file_name
        if os.path.isfile(file_name):
            file_name_new=file_name[:file_name.rfind('.')]+'_'+str(n[0])+file_name[file_name.rfind('.'):]
            n[0]+=1
        if os.path.isfile(file_name_new):
            file_name_new=check_meta(file_name)
        return file_name_new
    return_name=check_meta(filename)
    return return_name

file = open(check_filename_available("./vocabulary/with_trans.txt"),"w")
for item in dict:
    file.write(item)
    file.write(": ")
    file.write(dict[item])
    file.write("\n")
file.close()

file = open(check_filename_available("./vocabulary/no_trans.txt"),"w")
for item in dict:
    file.write(item)
    file.write("\n")
file.close()

filehandler.close