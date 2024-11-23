#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as py
import plotly.offline
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


df = pd.read_csv("rainfall in india 1901-2015.csv")
df.head()


# In[8]:


df = df.rename(columns = {'SUBDIVISION':'STATE'})


# In[9]:


plt.figure(figsize=(15,10))
sns.lineplot(x = 'YEAR', y= 'ANNUAL', hue = 'STATE', data = df)
plt.title('Annual Rainfall received',fontsize=20)


# In[10]:


plt.figure(figsize=(15,8))
df.groupby(['STATE','YEAR'])['ANNUAL'].sum().sort_values(ascending=False).plot()

plt.grid()
plt.xlabel("State,Year",fontsize=15)
plt.ylabel("Annual Rainfall received",fontsize=15)
plt.title('Highest Rainfall year Data of States',fontsize=20)


# In[11]:


plt.figure(figsize=(15,10))
df.groupby(['STATE'])['ANNUAL'].sum().sort_values(ascending=False).head(15).plot(kind='bar', color = 'black')
plt.ylabel('Total Rainfall')
plt.title('Total Rainfall Data',fontsize=20)
plt.grid()


# In[12]:


plt.figure(figsize=(10,7))
df[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG',
       'SEP', 'OCT', 'NOV', 'DEC']].mean().plot(kind= 'bar', color='red')
plt.xlabel('Months',fontsize=15)
plt.ylabel('Avg. Rainfall',fontsize=15)
plt.title('Avg. Monthly Rainfall Data',fontsize=25)
plt.grid()
plt.show()


# In[13]:


plt.figure(figsize=(10,2))
df[['STATE', 'Jan-Feb', 'Mar-May',
       'Jun-Sep', 'Oct-Dec']].groupby("STATE").mean().sort_values('Jun-Sep').plot.bar(width=0.5,edgecolor='k',align='center',stacked=True,figsize=(16,8))
plt.xlabel('STATE',fontsize=15)
plt.ylabel('Rainfall (in mm)',fontsize=15)
plt.title('Rainfall in States of India',fontsize=25)
plt.grid()


# In[18]:


plt.rcParams['figure.figsize']=(18,8)
ax = sns.boxplot(x="STATE", y="ANNUAL", data=df, width=0.8,linewidth=3)
ax.set_xlabel('State',fontsize=20)
ax.set_ylabel('Annual Rainfall (in mm)',fontsize=20)
plt.title('Annual Rainfall in States of India',fontsize=30)
ax.tick_params(axis='x',labelsize=10,rotation=90)
ax.tick_params(axis='y',labelsize=10,rotation=0)
plt.grid()


# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

window=Tk()
window.title(' ')
window.geometry("1000x7000+500+200")
window.configure(bg="#FFFFFF")



def resize_func():
    image = Image.open("C:/Users/User/Desktop/ak.jpg")
    w = int(width.get())
    h = int(height.get())
    resize_img = image.resize((w, h))
    img = ImageTk.PhotoImage(resize_img)
    disp_img.config(image=img)
    disp_img.image = img


frame = Frame(window)
frame.pack()

Label(
    frame,
    text='Width'
    ).pack(side=LEFT)
width = Entry(frame, width=30)
width.insert(END, 1550)
width.pack(side=LEFT)

Label(
    frame,
    text='Height'
    ).pack(side=LEFT)

height = Entry(frame, width=50)
height.insert(END, 800)
height.pack(side=LEFT)

resize_btn = Button(
    frame,
    text='Resize',
    command=resize_func
)
resize_btn.pack(side=LEFT)

disp_img = Label()
disp_img.place(x=0,y=50)

h1 = Label(text = "RAINFALL ANALYSIS ",font=('Arial',18,'bold'),bg="#E0FFFF",fg="black")
h1.place(x=550,y=50)



print("\n");

def func():#function of the button
    tkinter.messagebox.showinfo("message","data is loadded")

data = pd.read_csv("rainfall in india 1901-2015.csv")



def function():

    label = data
    top = Toplevel()
    top.title("DATA")
    msg = Label(top,text=label)
    msg.pack()
    but = Button(top,width=20,height=3,bg="blue",text="Exit",command=top.destroy,font=("comic sans",10))
    but.pack()



data = pd.read_csv("rainfall in india 1901-2015.csv")
run = data.info()


def datatype():

    label = data.head(6)
    top = Toplevel()
    top.title("READING THE DATA")
    msg= Label(top,text=label)
    msg.pack()
    but = Button(top,width=20,height=3,bg="red",text="Exit",command=top.destroy,font=("comic sans",10))
    but.pack()



def chart():
    global image
    top = Toplevel()
    top.title("'Annual Rainfall received")
    image = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop"))
    msg = Label(top,image=image)
    msg.pack()
    but = Button(top,width=10,height=3,bg="red",text="Exit",command=top.destroy,font=("comic sans",10))
    but.pack()


def chart1():
    global image
    top = Toplevel()
    top.title("Highest Rainfall year Data of States")
    image = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop"))
    msg = Label(top,image=image)
    msg.pack()
    but = Button(top,width=10,height=3,bg="red",text="Exit",command=top.destroy,font=("comic sans",10))
    but.pack()


def chart2():
    global image
    top = Toplevel()
    top.title(" Total Rainfall Data")
    image = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/BP.jpg"))
    msg = Label(top,image=image)
    msg.pack()
    but = Button(top,width=10,height=3,bg="red",text="Exit",command=top.destroy,font=("comic sans",10))
    but.pack()


def chart3():
    global image
    top = Toplevel()
    top.title("DISTRIBUSTION OF CHEST PAIN")
    image = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/chestpain.jpg"))
    msg = Label(top,image=image)
    msg.pack()
    but = Button(top,width=10,height=3,bg="red",text="Exit",command=top.destroy,font=("comic sans",10))
    but.pack()


def chart4():
    global image
    top = Toplevel()
    top.title("DISTRIBUSTION OF ONE FEATURE HUE")
    image = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/hear rate.jpg"))
    msg = Label(top,image=image)
    msg.pack()
    but = Button(top,width=10,height=3,bg="red",text="Exit",command=top.destroy,font=("comic sans",10))
    but.pack()


def chart5():
    global image
    top = Toplevel()
    top.title("HEART ATTACK AND HEART RATE")
    image = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/heart rate.jpg"))
    msg = Label(top,image=image)
    msg.pack()
    but = Button(top,width=10,height=3,bg="red",text="Exit",command=top.destroy,font=("comic sans",10))
    but.pack()

def chart6():
    global image
    top = Toplevel()
    top.title("BLOOD SUGAR")
    image = ImageTk.PhotoImage(Image.open("blood_sugar.jpg"))
    msg = Label(top,image=image)
    msg.pack()
    but = Button(top,width=10,height=3,bg="red",text="Exit",command=top.destroy,font=("comic sans",10))
    but.pack()

    
btn1=Button(text="LOAD THE DATA", width=30,height=3,bg="red",fg="black",command=func,font=('Arial',10,'bold'))
btn1.place(x=30,y=50)
print("\n");

btn2=Button(text="READING THE DATA", width=30,height=3,bg="yellow",fg="black",command=function,font=('Arial',10,'bold'))
btn2.place(x=30,y=120)

btn3=Button(text="PRINT THE DATA", width=30,height=3,bg="#FF0000",fg="black",command=datatype,font=('Arial',10,'bold'))
btn3.place(x=30,y=190)

btn4=Button(text="Annual Rainfall received", width=30,height=3,bg="yellow",fg="black",command=chart,font=('Arial',10,'bold'))
btn4.place(x=30,y=260)

btn5=Button(text="DISTRIBUTION OF GENDER", width=30,height=3,bg="#FF0000",fg="black",command=chart1,font=('Arial',10,'bold'))
btn5.place(x=30,y=330)

btn6=Button(text=" BLOOD PRESSURE", width=30,height=3,bg="yellow",fg="black",command=chart2,font=('Arial',10,'bold'))
btn6.place(x=30,y=400)

btn6=Button(text="DISTRIBUTION OF CHEST PAIN", width=30,height=3,bg="#FF0000",fg="black",command=chart3,font=('Arial',10,'bold'))
btn6.place(x=30,y=470)

btn7=Button(text="DISTRIBUTION OF ONE FEATURE HUE", width=30,height=3,bg="yellow",fg="black",command=chart4,font=('Arial',10,'bold'))
btn7.place(x=30,y=540)

btn8=Button(text="HEART ATTACK AND HEART RATE", width=30,height=3,bg="#FF0000",fg="black",command=chart5,font=('Arial',10,'bold'))
btn8.place(x=30,y=610)

btn9=Button(text="BLOOD SUGAR ", width=30,height=3,bg="yellow",fg="black",command=chart6,font=('Arial',10,'bold'))
btn9.place(x=30,y=680)



window.mainloop()


# In[ ]:




