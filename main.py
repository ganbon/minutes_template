import tkinter as tk
import tkinter.ttk as ttk
from setting import box,name_box,function_box,plan_box,create
    
app=tk.Tk()
app.geometry(
    "1000x1000"
)   
app.title(
    "議事録作成ツール"
)
frame1=tk.Frame(app)
frame2=tk.Frame(app)
frame3=tk.Frame(app)
frame4=tk.Frame(app)
frame5=tk.Frame(app)
frame6=tk.Frame(app)
frame7=tk.Frame(app)
frame1.pack(pady=5)
frame2.pack(pady=5)
frame3.pack(pady=5)
frame4.pack(pady=5)
frame5.pack(pady=5)
frame6.pack(pady=5)
frame7.pack(pady=5)

title_label = tk.Label(frame1, text="議事録テンプレート\n",font=("MSゴシック", "20", "bold"))
title_label.pack(side=tk.TOP)

writer_label1 = tk.Label(frame2, text="議事 ",font=("MSゴシック", "15", "bold"))
writer_label1.grid(row=0,column=0)
writer_name1=name_box(frame2,"名字",0,1,20)
writer_name1.insert(tk.END,"岩本")
writer_name2=name_box(frame2,"名前",0,3,20)
writer_name2.insert(tk.END,"和真")
writer_number=name_box(frame2,"学籍番号",0,5,30)
writer_number.insert(tk.END,"20T301")


next_writer_label1 = tk.Label(frame2, text="次回議事  ",font=("MSゴシック", "15", "bold"))
next_writer_label1.grid(row=1,column=0)
next_writer_name1 = name_box(frame2,"名字",1,1,20)
writer=[writer_name1,writer_name2,writer_number,next_writer_name1]


attend_label = tk.Label(frame3, text="出席　",font=("MSゴシック", "15", "bold"))
attend_label.grid(row=0,column=0)
d1=box(frame3,"D1",0,80)
m2=box(frame3,"M2",1,80)
m1=box(frame3,"M1",2,80)
b4=box(frame3,"B4",3,80)
b3=box(frame3,"B3",4,80)
b2=box(frame3,"B2",5,80)
b1=box(frame3,"B1",6,80)
member=[d1,m2,m1,b4,b3,b2,b1]
function_label = tk.Label(frame4, text="活動内容　",font=("MSゴシック", "15", "bold"))
function_label.grid(row=0,column=0)
func_1=function_box(frame4,"活動1",1)
func_2=function_box(frame4,"活動2",2)
func_3=function_box(frame4,"活動3",3)
func_list=[func_1,func_2,func_3]
plan_label = tk.Label(frame5, text="次回予定　",font=("MSゴシック", "15", "bold"))
plan_label.grid(row=0,column=0)
plan_1=plan_box(frame5,"予定1",1)
plan_2=plan_box(frame5,"予定2",2)
plan_3=plan_box(frame5,"予定3",3)
plan=[plan_1,plan_2,plan_3]
create_btn = tk.Button(frame7, text='生成',height=2,width=10,font=10,command=lambda : create(writer,member,func_list,plan))
create_btn.pack()



app.mainloop()

