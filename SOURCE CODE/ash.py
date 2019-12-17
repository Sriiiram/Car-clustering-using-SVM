import Tkinter as tk  
from functools import partial  
import class_cars
print"start1"
import luxury_cars
print"start2"
import perf_cars
print"start3"
import lux_perf_cars
print"start4"
print"start"

   
def call_result1(label_result, n1, n2,n3):  
    num1 = (n1.get())  
    num2 = (n2.get())
    num3 = (n3.get())
##    result = int(num1)+int(num2)  
##    label_result.config(text="Result = %d" % result)  
##    return
    result=class_cars.get_detail(num1, num2,num3)
    label_result.config(text=result)
def call_result2(label_result, n1, n2,n3):
    num1 = (n1.get())  
    num2 = (n2.get())
    num3 = (n3.get())
##    num1 = (n1.get())  
##    num2 = (n2.get())  
##    result = int(num1)+int(num2)  
##    label_result.config(text="Result = %d" % result)  
##    return
    result= luxury_cars.get_detail(num1, num2,num3)
    label_result.config(text=result)
def call_result3(label_result, n1, n2,n3):
    num1 = (n1.get())  
    num2 = (n2.get())
    num3 = (n3.get())
##    num1 = (n1.get())  
##    num2 = (n2.get())  
##    result = int(num1)+int(num2)  
##    label_result.config(text="Result = %d" % result)  
##    return
    result= perf_cars.get_detail(num1, num2,num3)
    label_result.config(text=result)

def call_result4(label_result,n1,n2,n3,n4,n5):
    num1 = (n1.get())  
    num2 = (n2.get())
    num3 = (n3.get())
    num4 = (n4.get())
    num5 = (n5.get())
##    num1 = (n1.get())  
##    num2 = (n2.get())  
##    result = int(num1)+int(num2)  
##    label_result.config(text="Result = %d" % result)  
##    return
    result= lux_perf_cars.get_detail(num1, num2,num3,num4,num5)
    label_result.config(text=result)
root = tk.Tk()  
root.geometry('1024x720')  
  
root.title('Car')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
number3 = tk.StringVar()  
number4 = tk.StringVar()
number5 = tk.StringVar()  
number6 = tk.StringVar()
number7 = tk.StringVar()  
number8 = tk.StringVar()
number9 = tk.StringVar()
number10 = tk.StringVar()  
number11 = tk.StringVar()
number12 = tk.StringVar()  
number13 = tk.StringVar()
number14 = tk.StringVar()

labelNum1 = tk.Label(root, text="MSRP").grid(row=1, column=0)  
labelNum2 = tk.Label(root, text="MPG_City").grid(row=1, column=2)
labelNum3 = tk.Label(root, text="MPG_Highway").grid(row=1, column=4)

labelNum4 = tk.Label(root, text="MSRP").grid(row=3, column=0)  
labelNum5 = tk.Label(root, text="MPG_Weight").grid(row=3, column=2)
labelNum6 = tk.Label(root, text="MPG_Lenngth").grid(row=3, column=4)

labelNum7 = tk.Label(root, text="MSRP").grid(row=5, column=0)  
labelNum8 = tk.Label(root, text="MPG_Cylinders").grid(row=5, column=2)
labelNum9 = tk.Label(root, text="MPG_Horsepower").grid(row=5, column=4)

labelNum10 = tk.Label(root, text="MSRP").grid(row=7, column=0)  
labelNum11 = tk.Label(root, text="MPG_Cylinders").grid(row=7, column=2)
labelNum12 = tk.Label(root, text="MPG_Horsepower").grid(row=7, column=4)
labelNum13 = tk.Label(root, text="MPG_Weight").grid(row=7, column=6)
labelNum14 = tk.Label(root, text="MPG_Lenngth").grid(row=7, column=8)
labelResult = tk.Label(root)  
  
labelResult.grid(row=10, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=1)  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=1, column=3)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=1, column=5)
entryNum4 = tk.Entry(root, textvariable=number4).grid(row=3, column=1)  
entryNum5 = tk.Entry(root, textvariable=number5).grid(row=3, column=3)
entryNum6 = tk.Entry(root, textvariable=number6).grid(row=3, column=5)
entryNum7 = tk.Entry(root, textvariable=number7).grid(row=5, column=1)  
entryNum8 = tk.Entry(root, textvariable=number8).grid(row=5, column=3)
entryNum9 = tk.Entry(root, textvariable=number9).grid(row=5, column=5)
entryNum10 = tk.Entry(root, textvariable=number10).grid(row=7, column=1)
entryNum11 = tk.Entry(root, textvariable=number11).grid(row=7, column=3)
entryNum12 = tk.Entry(root, textvariable=number12).grid(row=7, column=5)
entryNum13 = tk.Entry(root, textvariable=number13).grid(row=7, column=7)
entryNum14 = tk.Entry(root, textvariable=number14).grid(row=7, column=9)


  
call_result1 = partial(call_result1, labelResult, number1, number2, number3)  
call_result2 = partial(call_result2, labelResult, number4, number5, number6)
call_result3 = partial(call_result3, labelResult, number7, number8, number9)
call_result4 = partial(call_result4, labelResult, number10, number11, number12,number13,number14)


buttonCal = tk.Button(root, text="Class", command=call_result1).grid(row=2, column=0)  
buttonCal1 = tk.Button(root, text="Luxury", command=call_result2).grid(row=4, column=0)
buttonCal2 = tk.Button(root, text="Perf", command=call_result3).grid(row=6, column=0)
buttonCal3 = tk.Button(root, text="Lux+Perf", command=call_result4).grid(row=8, column=0) 


root.mainloop()  


