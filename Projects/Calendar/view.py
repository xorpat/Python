import tkinter as tk
import datetime
from tkinter import ttk
from enum import Enum
from calendar import monthrange
from turtle import width

class Weekday(Enum):
    MONDAY = "Mo"
    TUESDAY = "Tu" 
    WEDNESDAY = "We"
    THURSDAY = "Th"
    FRIDAY = "Fr"
    SATURDAY = "Sa"
    SUNDAY = "Su"


class MyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("1800x500")
        for i in range(3):  # Grid configuration
            master.rowconfigure(i)
        for k in range(4):
            master.columnconfigure(k)
        self.frame = master
        self.buttonDict = {}
        self.monthLabelDict = {}
        self.weekDayLabelDict = {}
        self.weekDayButtonList = []
        self.frameDict = {}
        
        self.Month = {
            0:"January",
            1:"February",
            2:"March",
            3:"April",
            4:"May",
            5:"June",
            6:"July",
            7:"August",
            8:"September",
            9:"October",
            10:"November",
            11:"December"
        }
        
        self.createWidgets()
        
    def createMonthFrameGrid(self, frame): # Creates a 3x4 grid with all months from January to December 
        column = 0
        row = 0
        for k in self.Month.keys(): # Creates the 3x4 split
            if k % 4 == 0:
                row += 1
                column = 0   
            self.frameDict[k] = ttk.Frame(frame, borderwidth=5, relief="ridge", width=100,height=100)
            self.frameDict[k].grid(column=column, row=row,sticky=("N","E","W","S"))
            column += 1
       
        
    def createMonthFrameGridLabels(self, frameDict): # Creates month labels from Jan - Dec
        for k in self.Month.keys():
            self.monthLabelDict[k] = ttk.Label(self.frameDict[k], text=self.Month[k])
            self.monthLabelDict[k].grid(row=1,columnspan=7)
            
    
    def createMonthFrameGridWeekDaysLabels(self, frameDict): # Creates Weekday labels from Mo - Su
        for i in range(len(self.Month)):
            k = 0
            for day in Weekday:
                    self.weekDayLabelDict[k] = ttk.Label(frameDict[i], text="{}".format(day.value))
                    self.weekDayLabelDict[k].grid(row=2, column=k, padx=5)
                    k += 1
    
    def createMonthFrameDaysButtonGrid(self,frameDict): # Creates Buttons for month
        for i in range(len(self.Month)): # 12 Month
            self.weekDayButtonList.append([])
            beginDay, endDay  = monthrange(datetime.datetime.now().year,i+1)
            m_today, d_today = tuple(map(int,datetime.date.today().strftime('%m-%d').split('-')))
            dayctr = 1
            for j in range(5): # 5 rows
                for k in range(len(Weekday)): # each day one Button
                    self.weekDayButtonList[i].append(tk.Button(self.frameDict[i],
                                                                width=4, 
                                                                text="{var}".format(var=dayctr if dayctr >= beginDay and dayctr <= endDay else ""),
                                                                bg="{bg_color}".format(bg_color="blue" if dayctr == d_today and i+1 == m_today else "#F0F0F0")
                                                                ))
                    
                    self.weekDayButtonList[i][-1].grid(row=3+j,column=k) # button positioning
                    dayctr += 1
        
    def createMonthFrameDaysLabels(self,frameDict):
        #for i in range(len(self.Month)):
        #self.weekDayButtonList[i][]
        #beginDay, endDay  = monthrange(datetime.datetime.now().year,i+1)
        #sublistDaysOfMonth = self.weekDayButtonList[i][beginDay-1:endDay]
        #for elem in sublistDaysOfMonth:
        pass   
        
       
            
    
    def createWidgets(self):
        self.createMonthFrameGrid(self.frame)
        self.createMonthFrameGridLabels(self.frameDict)
        self.createMonthFrameGridWeekDaysLabels(self.frameDict)
        self.createMonthFrameDaysButtonGrid(self.frameDict)
        self.createMonthFrameDaysLabels(self.frameDict)
        #self.button = ttk.Button(self.frame, text='Okay')
        #self.button.grid(row=1, column=0, padx=10, pady=10)
        #self.a_button = ttk.Button(self.frame, text="A Button") 
        #self.a_button.grid(row=1, column=2, padx=10, pady=10)
        #self.createCalendarLabels()
        #self.createButtons(10)
                
root = tk.Tk()
app = MyApp(root)
app.mainloop()
