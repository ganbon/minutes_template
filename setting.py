import tkinter as tk
import tkinter.ttk as ttk
from text import Text
from tkinter import messagebox
from datetime import datetime
import subprocess
import os

def create(writer,member,func,plan):
    minutes=Text(writer,member,func,plan)
    minutes.create_minutes()
    messagebox.showinfo('作成','議事録を作成しました')
    now_path=os.getcwd()
    file_path=f"{now_path}\\minutes_text\\{minutes.file_name}"
    subprocess.Popen(file_path,shell=True)
    

def box(frame,text,row,width):
    label = tk.Label(frame, text=text)
    label.grid(row=row,column=1)
    data = tk.Entry(frame, width=width, bd=1)
    data.grid(row=row,column=2)
    return data
    
def name_box(frame,text,row,column,width):
    label = tk.Label(frame, text=text)
    label.grid(row=row,column=column)
    name = tk.Entry(frame, width=width, bd=1)
    name.grid(row=row,column=column+1)
    return name
    
def function_box(frame,text,row):
    label = tk.Label(frame, text=text)
    label.grid(row=row,column=0)
    module_hour = [x for x in range(12,24)]
    module_time = [x for x in range(0,60,5)]
    start_hour = ttk.Combobox(frame, width=2,
                         values=module_hour, state="readonly")
    start_time = ttk.Combobox(frame, width=2,
                         values=module_time, state="readonly")
    start_hour.grid(row=row,column=1)
    label_start_hour = tk.Label(frame, text="時")
    label_start_hour.grid(row=row,column=2)
    start_time.grid(row=row,column=3)
    label_start_time = tk.Label(frame, text="分")
    label_start_time.grid(row=row,column=4)
    label_from = tk.Label(frame, text="~")
    label_from.grid(row=row,column=5)
    end_hour = ttk.Combobox(frame, width=2,
                         values=module_hour, state="readonly")
    end_time = ttk.Combobox(frame, width=2,
                         values=module_time, state="readonly")
    end_hour.grid(row=row,column=6)
    label_end_hour = tk.Label(frame, text="時")
    label_end_hour.grid(row=row,column=7)
    end_time.grid(row=row,column=8)
    label_end_time = tk.Label(frame, text="分")
    label_end_time.grid(row=row,column=9)
    label_end_time = tk.Label(frame, text="活動内容")
    label_end_time.grid(row=row,column=10)
    function_context = tk.Entry(frame, width=70, bd=1)
    function_context.grid(row=row,column=11)
    return [start_hour,start_time,end_hour,end_time,function_context]
    
def plan_box(frame,text,row):
    now_date = datetime.now()
    now_month = int(now_date.month)
    label = tk.Label(frame, text=text)
    label.grid(row=row,column=0)
    module_month = [x for x in range(1,13)]
    module_day = [x for x in range(1,32)]   
    module_hour = [x for x in range(12,24)]
    module_time = [x for x in range(0,60,5)]
    month = ttk.Combobox(frame, width=5,height=5,
                         values=module_month, state="readonly")
    month.set(str(now_month))
    day = ttk.Combobox(frame, width=5,height=5,
                         values=module_day, state="readonly")
    start_hour = ttk.Combobox(frame, width=5,
                         values=module_hour, state="readonly")
    start_hour.set("19")
    start_time = ttk.Combobox(frame, width=5,height=5,
                         values=module_time, state="readonly")
    start_time.set("0")
    end_hour = ttk.Combobox(frame, width=5,height=5,
                         values=module_hour, state="readonly")
    end_hour.set("21")
    end_time = ttk.Combobox(frame, width=5,height=5,
                         values=module_time, state="readonly")
    end_time.set("0")
    month.grid(row=row,column=1)
    label_month = tk.Label(frame, text="月")
    label_month.grid(row=row,column=2)
    day.grid(row=row,column=3)
    label_month = tk.Label(frame, text="日")
    label_month.grid(row=row,column=4)
    start_hour.grid(row=row,column=5)
    label_start_hour = tk.Label(frame, text="時")
    label_start_hour.grid(row=row,column=6)
    start_time.grid(row=row,column=7)
    label_start_time = tk.Label(frame, text="分")
    label_start_time.grid(row=row,column=8)
    label_from = tk.Label(frame, text="~")
    label_from.grid(row=row,column=9)
    end_hour.grid(row=row,column=10)
    label_end_hour = tk.Label(frame, text="時")
    label_end_hour.grid(row=row,column=11)
    end_time.grid(row=row,column=12)
    label_end_time = tk.Label(frame, text="分")
    label_end_time.grid(row=row,column=13)
    label_end_time = tk.Label(frame, text="活動内容")
    label_end_time.grid(row=row,column=14)  
    function_context = tk.Entry(frame, width=50, bd=1)
    function_context.insert(tk.END,"定例活動")
    function_context.grid(row=row,column=15)
    return [month,day,start_hour,start_time,end_hour,end_time,function_context]
    
    
    