from datetime import datetime
import datetime as dt
class Text:
    def __init__(self,writer,member,func,plan):
        self.name1,self.name2,self.student_number,self.next_writer = writer
        now_date = datetime.now()
        self.now_year = int(now_date.year)
        self.now_month = int(now_date.month)
        self.now_day = int(now_date.day)
        self.member=member
        self.function_context=func
        self.plan_context=plan
        self.week_list = ["月","火","水","木","金","土","日"]
    
    def create_minutes(self):
        minutes_text=self.text()
        self.file_name=f"{self.now_year}_{self.now_month:02}{self.now_day:02}.txt"
        with open(f'minutes_text\\{self.file_name}','w',encoding='utf-8') as f:
            f.write(minutes_text)
    
        
    def text(self):
        minutes_text=self.title()
        minutes_text+="★ 次第\n\n"
        minutes_text+=self.active_member()
        minutes_text+=self.writer_memo()
        minutes_text+=self.next_writer_memo()
        minutes_text+= self.today_progress()
        minutes_text+=self.active_context()
        minutes_text+=self.plan()
        minutes_text+=self.free()
        return minutes_text
    

    def title(self):
        name1=self.name1.get()
        name2=self.name2.get()
        number=self.student_number.get()
        return f"□ SLP 定例活動 {self.now_year}.{self.now_month:02}.{self.now_day:02} s{number} {name1} {name2}\n\n"
    
    def active_member(self):
        out=""
        class_str = ["○ D1 ","○ M2 ","○ M1 ","○ B4 ","○ B3 ","○ B2 ","○ B1 "]
        for c,m in zip(class_str,self.member): 
            member=m.get().split('　')
            if member!=[""]:
                out+=c
                for s in member:
                    out+=f"{s}、"
                out+='\n'
        out+='\n'
        return out
    
    def writer_memo(self):
        name=self.name1.get()
        return f"議事 {name}\n\n"
    
    def next_writer_memo(self):
        next_writer=self.next_writer.get()
        return f"次回議事 {next_writer}\n\n\n"
    
    def today_progress(self):
        out="● 進行\n\n"
        for _f in range(3):
            function_list=self.value_get(self.function_context[_f])
            print(function_list)
            if function_list==[]:
                continue
            function_list[:4] = [int(x) for x in function_list[:4]]
            start_hour,start_minute,end_hour,end_minute,context = function_list
            out+=f"○ {start_hour:02}:{start_minute:02}-{end_hour:02}:{end_minute:02} {context}\n"
        out+="\n\n"
        return out
    
    def active_context(self):
        out="★ 活動\n\n"
        for _f in range(len(self.function_context)):
            function_list = self.value_get(self.function_context[_f])
            if function_list==[]:
                continue
            function_list[:4] = [int(x) for x in function_list[:4]]
            start_hour,start_minute,end_hour,end_minute,context = function_list
            out+=f"● {context}\n\n"
            out+="ここに活動内容を記入\n\n"
        out+="\n"
        return out
        
    def plan(self):
        out="■ 予定\n\n"
        for p in self.plan_context:
            plan_list = self.value_get(p)
            plan_list[:len(plan_list)-1] = [int(x) for x in plan_list[:len(plan_list)-1]]
            plan_month,plan_day,start_hour,start_minute,end_hour,end_minute,context = plan_list
            d_key = dt.date(self.now_year,plan_month,plan_day)
            plan_year = self.now_year
            week_key = d_key.weekday()
            plan_week = self.week_list[week_key]
            out+=f"○ {plan_year}.{plan_month:02}.{plan_day:02}({plan_week}) {start_hour:02}:{start_minute:02}-{end_hour:02}:{end_minute:02} {context}\n"
        out+="\n\n"
        return out
    
    def free(self):
        out="■ 備考\n\n"
        out+="ここに好きなことを書こう！\n"
        return out
    
    def value_get(self,box_list):
        value_list=[]
        for b in box_list:
            com=b.get()
            if com=='':
                continue
            value_list.append(b.get())
        return value_list