#coding:utf-8
from tkinter import *
import webbrowser
import requests
import re

url='http://www.qmaile.com/'
response=requests.get(url)
response.encoding=response.apparent_encoding
resp=response.text

rege=re.compile('<option value="(.*?)" selected')
reg=re.findall(rege,resp)
one=reg[0]
two=reg[1]
three=reg[2]
four=reg[3]
five=reg[4]
#图形界面
tk=Tk()
tk.title('vip视频播放')
#设置窗口大小 位置
tk.geometry('500x250+200+200')
#标签
label1=Label(tk,text='播放接口',font=('微软雅黑',12))
label2=Label(tk,text='视频链接',font=('微软雅黑',12))
label1.grid()
label2.grid(row=5,column=0)
text1=Entry(tk,text='',width=50)
text1.grid(row=5,column=1)
var=StringVar()
radiobutton1=Radiobutton(tk,text='播放接口1',variable=var,value=one)
radiobutton2=Radiobutton(tk,text='播放接口2',variable=var,value=two)
radiobutton3=Radiobutton(tk,text='播放接口3',variable=var,value=three)
radiobutton4=Radiobutton(tk,text='播放接口4',variable=var,value=four)
# radiobutton5=Radiobutton(tk,text='播放接口5',variable=var,value=five)
radiobutton1.grid(row=0,column=1)
radiobutton2.grid(row=1,column=1)
radiobutton3.grid(row=2,column=1)
radiobutton4.grid(row=3,column=1)
# radiobutton5.grid(row=4,column=1)
def mac():
	webbrowser.open(var.get()+text1.get())
	
def del_text():
	text1.delete(0,'end')
button1=Button(tk,text='播放',font=('微软雅黑',12),width=8,height=1,command=mac) 
button2=Button(tk,text='清除',font=('微软雅黑',12),width=8,height=1,command=del_text)
button1.grid(row=6,column=1)
button2.grid(row=7,column=1)

#消息循环
tk.mainloop()