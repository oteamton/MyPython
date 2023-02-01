import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import threading
import time

window = tk.Tk()
window.title("serial read")
window.geometry("1200x720")
window.config(bg="light blue")

voltage1 = []
voltage2 = []
voltage3 = []
voltage4 = []

time1 = []
time2 = []
time3 = []
time4 = []

status = False

def plot():
    global status
    t1.start()
    status = True

def plot_data():
    #global voltage1,voltage2,voltage3,voltage4,time1,time2,time3,time4,status
    if(status==True):
        try:
            lines1.set_xdata(time1)
            lines1.set_ydata(voltage1)

            lines2.set_xdata(time2)
            lines2.set_ydata(voltage2)
            
            lines3.set_xdata(time3)
            lines3.set_ydata(voltage3)
            
            lines4.set_xdata(time4)
            lines4.set_ydata(voltage4)
            
            canvas1.draw()
        
        except: 
            print("plot error")

    window.after(10,plot_data)    

def stopThread():
    global status
    status = False
    #btn1.config(text= "disable",bg="yellow",state = tk.DISABLED)
    try:
        t1.join()
    except:
        print("error!!!!!!!!!")


def threadTask():
    df = pd.read_excel('Python\Data\Book1.xlsx','Sheet1')
    count = 0
    Xdata = 0
    while(status == True):
        if(Xdata < 100):
            try:

                voltage1.append(df['data2'][count])
                time1.append(Xdata)
                #print(df['test'][count])

                voltage2.append(df['random'][count])
                time2.append(Xdata)
                
                voltage3.append(df['data'][count])
                time3.append(Xdata)
                
                voltage4.append(df['data'][count])
                time4.append(Xdata)

                Xdata = Xdata +1
                count = count +1
                
            

            except:
                 print("can't read data")
        
        else: 
            voltage1.clear()
            voltage2.clear()
            voltage3.clear()
            voltage4.clear()

            time1.clear()
            time2.clear()
            time3.clear()
            time4.clear()

            Xdata = 0

        if(count == 948): 
            count = 0

        time.sleep(0.000001)
          
    
    
    canvas1.draw()

#---------------------------------------Button------------------------------------------------
btn1 = tk.Button(text="plot",command= plot).place(x=900,y=650)
btn2 = tk.Button(text="stop thread",command= stopThread).place(x=1000,y=650)

data = [1,2,3,4,5]
x = [10,20,30,40,50]
#-------------------------------------set graph------------------------------------------------------
fig = Figure()
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

ax1.set_title('serial data')
ax1.set_ylabel('voltage')
ax1.set_xlim(0,100)
ax1.set_ylim(-100,100)
lines1 = ax1.plot([],[])[0]

ax2.set_ylabel('Voltage')
ax2.set_xlim(0,100)
ax2.set_ylim(-100,100)
lines2 = ax2.plot([],[])[0]

#ax3.set_title('Serial Data')
#ax3.set_xlabel('Sample')
ax3.set_ylabel('Voltage')
ax3.set_xlim(0,100)
ax3.set_ylim(-500,600)
lines3 = ax3.plot([],[])[0]

#ax4.set_title('Serial Data')
ax4.set_xlabel('Sample')
ax4.set_ylabel('Voltage')
ax4.set_xlim(0,100)
ax4.set_ylim(-500,600)
lines4 = ax4.plot([],[])[0]

#-----------------------------------------# A tk.DrawingArea.----------------------------------------
canvas1 = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
canvas1.get_tk_widget().place(x = 10, y = 10, width = 800,height = 600)
canvas1.draw()

#------------------------------------------#threding-----------------------------
t1 = threading.Thread(target=threadTask)
window.after(10,plot_data)
window.mainloop()

