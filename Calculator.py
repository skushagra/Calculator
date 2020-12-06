	# btn1      -----------------------------   7

# btn2      -----------------------------   8

# btn3      -----------------------------   9

# btn4      -----------------------------   +

# btn5      -----------------------------   4

# btn6      -----------------------------   5

# btn7      -----------------------------   6

# btn8      -----------------------------   -

# btn9      -----------------------------   1

# btn10     -----------------------------   2

# btn11     -----------------------------   3 

# btn12     -----------------------------   X

# btn13     -----------------------------   C

# btn14     -----------------------------   0

# btn15     -----------------------------   =

# btn16     -----------------------------   /

# btn17     -----------------------------   √

# btn18     -----------------------------   x²

# btn19     -----------------------------   . 

# btn20     -----------------------------   ⌫

# btn21     -----------------------------   ^
import tkinter
from tkinter import *
from tkinter import messagebox
val = ""
A = 0
operator = ""
pi = 3.141592653589  
root = tkinter.Tk()
root.title("Calculator")
root.geometry("300x410+300+300")
#root.resizable(0,0)
#root.iconbitmap('/home/kali/SoftwareCode/Python/Complete/forcalc.ico')
# img = PhotoImage(file='forcalc.png')
# root.tk.call('wm', 'iconphoto', root._w, img)
#photo = PhotoImage(file = "forcalc.png")
#root.iconphoto(False, photo)
#messagebox.showinfo(title = "Welcome to Calculator",message="Welcome to Calculator. Before you start using it remember that all the trigonometric functions give value in radians and there is now way  provided to change it into degrees in this application. ",)                                                         


#  Adding menu
def about():
   messagebox.showinfo(title = "About" ,
                      message = """Made with ❤ by © KushagraS ™
               Contact ↓ business.kushagras@gmail.com """)
def othapp():
   othapplication = Toplevel()
   othapplication.title("Other Applications")
   othapplication.geometry("600x600+300+300")
   frmapp1=Frame(othapplication).pack(expand=True,fill="both")
   frmapp2=Frame(othapplication).pack(expand=True,fill="both")
   frmapp3=Frame(othapplication).pack(expand=True,fill="both")
   lbloth1= Label(frmapp1,font=("Fira Code Light",22) ,text="Other Applications by KushagraS ™").pack(side =LEFT,expand=True,fill="both")
   lbloth2= Label(frmapp2,font=("Fira Code Light",20) , text="""1. Calculator\n2. Text Editor\n3. Music Player\n4. Image Viewer\n5. Web Browser""").pack(side = BOTTOM,expand=True,fill="both")
   lbloth3= Label(frmapp3,font=("Fira Code Light",15) , text="Check out any up date on www.kushagras.com").pack(side = BOTTOM,expand=True,fill="both")
   othapplication.mainloop()



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)




menubar.add_cascade(label="Mode", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_separator()
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Exit", command=root.quit)
helpmenu.add_command(label="Other Applications", command=othapp,)
root.config(menu=menubar)

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
data = StringVar()
#----------------Label--------------------
lab = Label(root, text = "Lable", anchor = SE, font = ("Verdena", 22), textvariable = data, background = "#ffffff", fg = "#000000", )
lab.pack(expand = True, fill ="both")
#----------------Frame 1--------------------
frm1 = Frame(root)
frm1.pack(expand = True, fill = "both",)
#----------------Frame 2--------------------
frm2 = Frame(root)
frm2.pack(expand = True, fill = "both",)
#----------------Frame 3--------------------
frm3 = Frame(root)
frm3.pack(expand = True , fill = "both")
#----------------Frame 4--------------------
frm4 = Frame(root)
frm4.pack(expand = True, fill = "both",)
#----------------Frame 5---------------------
frm5 = Frame(root)
frm5.pack(expand = True, fill = "both",)
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#*******************************************************fun for starts*********************************************
#-----------------fun for button 1----------------
def buttonFor_1_isClicked():
    global val 
    val += "1"
    data.set(val)
#-----------------fun for button 2----------------
def buttonFor_2_isClicked():
    global val 
    val += "2"
    data.set(val)
#-----------------fun for button 3----------------
def buttonFor_3_isClicked():
    global val 
    val += "3"
    data.set(val)
#-----------------fun for button 4----------------
def buttonFor_4_isClicked():
    global val 
    val += "4"
    data.set(val)
#-----------------fun for button 5----------------
def buttonFor_5_isClicked():
    global val 
    val += "5"
    data.set(val)
#-----------------fun for button 6----------------
def buttonFor_6_isClicked():
    global val 
    val = val + "6"
    data.set(val)
#-----------------fun for button 7----------------
def buttonFor_7_isClicked():
    global val 
    val = val + "7"
    data.set(val)
#-----------------fun for button 8----------------
def buttonFor_8_isClicked():
    global val 
    val = val + "8"
    data.set(val)
#-----------------fun for button 9----------------
def buttonFor_9_isClicked():
    global val 
    val = val + "9"
    data.set(val)
#-----------------fun for button 0----------------
def buttonFor_0_isClicked():
    global val 
    val = val + "0"
    data.set(val)
#-----------------fun for button .----------------
def buttonFor_dot_isClicked():
    global val 
    val = val + "."
    data.set(val)

#%^%^%^%^^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^ fun for af buttons %^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%
#-------- fun for ! ----------
def buttonFor_factorial_isClicked():
     global val
     global operator
     operator = "!"
     val = val + "!"
     data.set(val)
#-------- fun for sin ----------
def buttonFor_sin_isClicked():
     global val
     global operator
     operator = "sin"
     val = val + "sin("
     data.set(val)
#-------- fun for cos ----------
def buttonFor_cos_isClicked():
     global val
     global operator
     operator = "tan("
     val = val + "cos("
     data.set(val)
#-------- fun for tan ----------
def buttonFor_tan_isClicked():
     global val
     global operator
     operator = "tan("
     val = val + "tan("
     data.set(val)
#-------- fun for pi ----------
def buttonFor_pi_isClicked():
     global val
     global operator
     operator = "π"
     val = val + "π"
     data.set(val)
#-------- fun for power ----------
def buttonFor_power_isClicked():
     global val
     global operator
     operator = "^"
     val = val + "^"
     data.set(val)
#-------- fun for sin inv ----------
def buttonFor_sininv_isClicked():
     global val
     global operator
     operator = "sin-1("
     val = val + "sin-1("
     data.set(val)
#-------- fun for cos inv ----------
def buttonFor_cosinv_isClicked():
     global val
     global operator
     operator = "cos-1("
     val = val + "cos-1("
     data.set(val)
#-------- fun for tan inv ----------
def buttonFor_taninv_isClicked():
     global val
     global operator
     operator = "tan-1("
     val = val + "tan-1("
     data.set(val)
#-------- fun for ysqrtx ----------
def buttonFor_ysqrtx_isClicked():
     global val
     global operator
     operator = "y√x"
     val = val + "√"
     data.set(val)
#-------- fun for xsqrtx ----------
def buttonFor_xsqrtx_isClicked():
     global val
     global operator
     operator = "x√x"
     val = val + "x√"
     data.set(val)
#-------- fun for xsqrtx ----------
def buttonFor_ce_isClicked():
     global val
     global operator
     op = operator 
     newval = val.split(op)[0]
     val = newval + op
     data.set(val)




#%^%^%^%^^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^ fun for af buttons %^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

#*******************************************************fun for buttons ends**********************************************
#@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ fun for operators  starts@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @
def buttonFor_plus_isClicked():
    global A
    global operator
    global val
    A = list(map(float, val.split("+")))
    operator = "+"
    val = val + "+"
    A= str(A)
    data.set(val)

def buttonFor_sub_isClicked():
    global A
    global operator
    global val
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def buttonFor_multiply_isClicked():
    global A
    global operator
    global val
    A = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def buttonFor_divide_isClicked():
    global A
    global operator
    global val
    A = float(val)
    operator = "÷"
    val = val + "÷"
    data.set(val)

def buttonFor_sqroot_isClicked():
    global A
    global operator
    global val
    operator = "√"
    val = val + "√"
    data.set(val)

def buttonFor_sq_isClicked():
    global A
    global operator
    global val
    A = float(val)
    operator = "x²"
    val = val + "²"
    data.set(val)

def buttonFor_si_isClicked():
        si = Toplevel()
        si.title("Calculate Simple Interest")
        si.geometry("600x600+300+300")
        lbl01 = Label(si, text = "This is a label", anchor = SE, font = ("Verdena", 22), textvariable = sata, background = "#ffffff", fg = "#000000", ).pack(expand = True, fill = "both")
        

        frm01 = Frame(si).pack(expand = True, fill = "both")
        bttn = Button(si, text="Calculate",bg = "#05ACF5", fg = "#ffffff").pack(expand = True, fill = "both")
#@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @fun for operators ends@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& fun for C & ⌫ starts&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def buttonFor_c_isClicked():
    global A
    global operator
    global val
    A = 0 
    val = "" 
    operator = ""
    data.set(val)
def buttonFro_del_isClickled():
    global val
    ind = (len(val)-1)
    char = val[:ind]
    val = char
    data.set(val)
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& fun for C ends&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def buttonFor_saf_isClicked():
    global blue
    global white
    global grey
    btn1.config(text = "INV",font = ("Verdena", 15), bg = "#05ACF5", fg = "#ffffff", command = buttonFor_sinverse_isClicked )
    btn2.config(text = "sin", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_sin_isClicked )
    btn3.config(text = "cos", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_cos_isClicked)
    btn4.config(text = "tan", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_tan_isClicked)
    btn5.config(text = "^", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_power_isClicked)
    btn6.config(text = "!", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_factorial_isClicked)
    btn7.config(text = "y√x",font = ("Verdena",15), bg = "#05ACF5", fg = "#ffffff", command = buttonFor_ysqrtx_isClicked)
    btn8.config(text = "x√x",font = ("Verdena",15), bg = "#05ACF5", fg = "#ffffff", command = buttonFor_xsqrtx_isClicked)
    btn18.config(text = "CE", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_ce_isClicked)
    btn17.config(text = "SI", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_si_isClicked)
    #btn11.config(text = "ln", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_natlog_isClicked)
    #btn17.config(text = "π", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_pi_isClicked)    
    btn21.config(text = "⌄", bg = "#033950", fg = "#ffffff", command = buttonFor_eaf_isClicked,)
def buttonFor_eaf_isClicked():
    global blue
    global white
    global grey
    btn1.config(text = "7",font = ("Verdena", 22), bg = "#696969", fg = "#ffffff", command = buttonFor_7_isClicked )
    btn2.config(text = "8",font = ("Veedena", 22), bg = "#696969", fg = "#ffffff", command = buttonFor_8_isClicked )
    btn3.config(text = "9",font = ("Veedena", 22), bg = "#696969", fg = "#ffffff", command = buttonFor_9_isClicked)
    btn4.config(text = "+",font = ("Veedena", 22), bg = "#696969", fg = "#00FFFF", command = buttonFor_plus_isClicked)
    btn5.config(text = "4", bg = "#696969", fg = "#ffffff", command = buttonFor_4_isClicked)
    btn6.config(text = "5", bg = "#696969", fg = "#ffffff", command = buttonFor_5_isClicked)
    btn7.config(text = "6",font = ("Verdena",22), bg = "#696969", fg = "#ffffff", command = buttonFor_6_isClicked)
    btn8.config(text = "-", font = ("Verdena",22), bg = "#696969", fg = "#00ffff", command = buttonFor_sub_isClicked)
    #btn10.config(text = "2", bg = "#696969", fg = "#ffffff", command = buttonFor_2_isClicked)
    btn18.config(text = "x²",font = ("Verdena",22), bg = "#696969", fg = "#00ffff", command = buttonFor_sq_isClicked)
    btn17.config(text = "√", bg = "#696969", fg = "#00FFFF", command = buttonFor_sqroot_isClicked)  
    btn21.config(text = "^", bg = "#05ACF5", fg = "#ffffff", command = buttonFor_saf_isClicked)
def buttonFor_sinverse_isClicked():
        btn1.config(text = "INV",font = ("Verdena", 15), bg = "#033950", fg = "#ffffff", command = buttonFor_einverse_isClicked)
        btn2.config(text = "sin-1",font = ("Verdena", 15), bg = "#05ACF5", fg = "#ffffff", command = buttonFor_sininv_isClicked )
        btn3.config(text = "cos-1",font = ("Verdena", 15), bg = "#05ACF5", fg = "#ffffff", command = buttonFor_cosinv_isClicked)
        btn4.config(text = "tan-1",font = ("Verdena", 15), bg = "#05ACF5", fg = "#ffffff", command = buttonFor_taninv_isClicked)
def buttonFor_einverse_isClicked():
        btn1.config(text = "INV",font = ("Verdena", 15), bg = "#05ACF5", fg = "#ffffff", command = buttonFor_sinverse_isClicked)
        btn2.config(text = "sin",font = ("Veedena", 22), bg = "#05ACF5", fg = "#ffffff", command = buttonFor_sin_isClicked )
        btn3.config(text = "cos", font = ("Veedena", 22),bg = "#05ACF5", fg = "#ffffff", command = buttonFor_cos_isClicked)
        btn4.config(text = "tan", font = ("Veedena", 22),bg = "#05ACF5", fg = "#ffffff", command = buttonFor_tan_isClicked)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ fun for = starts $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def buttonFor_result_isClicked():
    global A
    global operator
    global val
    global pi
    val2 = val
    while True:
        if '÷' in val2:
            i = val2.index('÷')
            res = int(val2[i-1]) / int(val2[i-1])
            val2 = val2.split('÷') + str(res)
            if '*' in val2:
                i = val2.index('*')
                res = int(val2[i-1]) * int(val2[i-1])
                val2 = val2.split('*') + str(res)
                if '+' in val2:
                    i = val2.index('+')
                    res = int(val2[i-1]) + int(val2[i-1])
                    val2 = val2.split('+') + str(res)
                    if '-' in val2:
                        i = val2.index('-')
                        res = int(val2[i-1]) - int(val2[i-1])
                        val2 = val2.split('-') + str(res)
        elif '*' in val2:
            i = val2.index('*')
            res = int(val2[i-1]) * int(val2[i-1])
            val2 = val2.split('*') + str(res)
            if '+' in val2:
                i = val2.index('+')
                res = int(val2[i-1]) + int(val2[i-1])
                val2 = val2.split('+') + str(res)
                if '-' in val2:
                    i = val2.index('-')
                    res = int(val2[i-1]) - int(val2[i-1])
                    val2 = val2.split('-') + str(res)   
        elif '+' in val2:
            i = val2.index('+')
            res = int(val2[i-1]) + int(val2[i-1])
            val2 = val2.split('+') + str(res)
            print(val2)
            if '-' in val2:
                i = val2.index('-')
                res = int(val2[i-1]) - int(val2[i-1])
                val2 = val2.split('-') + str(res)
        elif '-' in val2:
            i = val2.index('-')
            res = float(val2[i-1]) - int(val2[i-1])
            val2 = val2.split('-') + str(res)
        if not('+') in val2 and not('-') in val2 and not('*') in val2 and not('÷') in val2:
            break
# def buttonFor_result_isClicked():
#     global A
#     global operator
#     global val
#     global pi
#     val2 = val 
#     if operator == "+":
#        B = float((val2.split("+")[1]))
#        C = A + B
#        data.set(C)
#        val = str(C)
#     elif operator == "-":
#        B = float((val2.split("-")[1]))
#        C  = A - B
#        data.set(C)
#        val = str(C)
#     elif operator == "*":
#        B = float((val2.split("*")[1]))
#        C  = A * B
#        data.set(C)
#        val = str(C)
#     elif operator == "÷":
#        B = float((val2.split("÷")[1]))
#        if B == 0:
#            messagebox.showerror("Error","Division by 0 yeilds an undefined result")
#            A = 0
#            val = ""
#            operator = ""
#            data.set(val)
#        else:
#            C  = A / B
#            data.set(C)
#            val = str(C)
#     elif operator == "√":
#           B =  (val2.split("√")[1])
#           b = float(B)
#           C =  math.sqrt(b)
#           data.set(C)
#           val = str(C)
#     elif operator == "x²":
#           B = float((val2.split("²")[0]))
#           C = B * B
#           data.set(C)
#           val = str(C)
#     elif operator == "!":
#          B=float(val.split("!")[0])
#          C=math.factorial(B)
#          data.set(C)
#          val=str(C) 
#     elif operator == "sin":
#          B=float(val.split("sin(")[1]) 
#          C=math.sin(B)
#          data.set(C)
#          val=str(C) 
#     elif operator == "cos(":
#          B=float(val.split("cos(")[1])
#          C=math.cos(B)
#          data.set(B)
#          val=str(C)
#     elif operator == "tan(":
#          B=float(val.split("tan(")[1])
#          C=math.tan(B)
#          data.set(C)
#          val=str(C)  
#     elif operator == "π":
#          B=float(val.split("π")[0])
#          #B2=float(val.split("π")[1])
#          C=B*math.pi
#          data.set(C)
#          val=str(C)  
#     elif operator == "^":
#          B=float(val.split("^")[0])
#          b=float(val.split("^")[1])
#          C=B**b 
#          data.set(C)
#          val=str(C)  
#     elif operator == "sin-1(":
#          B=float(val.split("sin-1(")[1])
#          C=math.asin(B)
#          data.set(C)
#          val=str(C)  
#     elif operator == "cos-1(":
#          B=float(val.split("cos-1(")[1])
#          C=math.acos(B)
#          data.set(C)
#          val=str(C)  
#     elif operator == "tan-1(":
#          B=float(val.split("tan-1(")[1])
#          C=math.atan(B)
#          data.set(C)
#          val=str(C) 
#     elif operator == "y√x":
#          B = float(val.split("√")[0])
#          b = float(val.split("√")[1])
#          c = (1/float(B))
#          C = b**c
#          data.set(C)
#          val = str(C)
#     elif operator == "x√x":
#          B = float(val.split("√")[1])
#          c = (1/float(B))
#          C = B**c
#          data.set(C)
#          val = str(C)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ fun for = ends $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#88888888888888888888888888888888888888888888fun for hover starts888888888888888888888888888888888888888888888888
#def enteredbtn1(event):
    #btn1.config(
       #         bg = "#0AA6E5",
      #          fg = "#ffffff",
     #          )
#def leftbtn1(event):
 #  btn1.config(
  #          bg = "#696969",
   #         fg = "#0AA6E5"
    #        )
#88888888888888888888888888888888888888888888fun for hover ends88888888888888888888888888888888888888888888888888
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#----------------button 1--------------------
btn1 = Button(frm1,
              text="7" ,
              font = ("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_7_isClicked,
              )
btn1.config( height = 1, width = 1 )
btn1.pack(side = LEFT,expand=True , fill="both")
#btn1.bind("<Enter>", enteredbtn1)
#btn1.bind("<Leave>", leftbtn1)
#----------------button 2--------------------
btn2 = Button(frm1,
              text="8",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_8_isClicked,
              )
btn2.config( height = 1, width = 1 )
btn2.pack(side = LEFT,expand=True , fill="both")
#----------------button 3--------------------
btn3 = Button(frm1,
              text="9",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_9_isClicked,
              )
btn3.config( height = 1, width = 1 )
btn3.pack(side = LEFT,expand=True , fill="both")
#----------------button 4--------------------
btn4 = Button(frm1,
              text="+",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#00FFFF",
              highlightthickness=0,
              command = buttonFor_plus_isClicked,
              )
btn4.config( height = 1, width = 1 )
btn4.pack(side = LEFT,expand=True , fill="both")
#----------------button 5--------------------
btn5 = Button(frm2,
              text="4" ,
              font = ("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_4_isClicked,
              )
btn5.config( height = 1, width = 1 )
btn5.pack(side = LEFT,expand=True , fill="both")
#----------------button 6--------------------
btn6 = Button(frm2,
              text="5",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_5_isClicked,
              )
btn6.config( height = 1, width = 1 )
btn6.pack(side = LEFT,expand=True , fill="both")
#----------------button 7--------------------
btn7 = Button(frm2,
              text="6",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_6_isClicked,
              )
btn7.config( height = 1, width = 1 )
btn7.pack(side = LEFT,expand=True , fill="both")
#----------------button 8--------------------
btn8 = Button(frm2,
              text="-",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#00FFFF",
              highlightthickness=0,
              command = buttonFor_sub_isClicked,
              )
btn8.config( height = 2, width = 1 )
btn8.pack(side = LEFT,expand=True , fill="both")
#----------------button 9--------------------
btn9 = Button(frm3,
              text="1" ,
              font = ("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_1_isClicked
              )
btn9.config( height = 1, width = 1 )
btn9.pack(side = LEFT,expand=True , fill="both")
#----------------button 10--------------------
btn10 = Button(frm3,
              text="2",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_2_isClicked
              )
btn10.config( height = 1, width = 1 )
btn10.pack(side = LEFT,expand=True , fill="both")
#----------------button 11--------------------
btn11 = Button(frm3,
              text="3",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_3_isClicked
              )
btn11.config( height = 1, width = 1 )
btn11.pack(side = LEFT,expand=True , fill="both")
#----------------button 12--------------------
btn12 = Button(frm3,
              text="*",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#00FFFF",
              highlightthickness=0,
              command = buttonFor_multiply_isClicked,
              )
btn12.config( height = 2, width = 1 )
btn12.pack(side = LEFT,expand=True , fill="both")
#----------------button 13-------------------
btn13 = Button(frm4,
              text="C" ,
              font = ("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_c_isClicked,
              )
btn13.pack(side = LEFT,expand=True , fill="both")
btn13.config( height = 1, width = 1 )
#----------------button 14--------------------
btn14 = Button(frm4,
              text="0",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#ffffff",
              highlightthickness=0,
              command = buttonFor_0_isClicked
              )
btn14.config( height = 1, width = 1 )
btn14.pack(side = LEFT,expand=True , fill="both")
#----------------button 15--------------------
btn15 = Button(frm4,
              text="=",
              font=("Verdena ", 22),
              relief = GROOVE,
              background = "#ffa500",
              fg = "#ffffff",
	      border = 0,
              highlightthickness=0,
              command  = buttonFor_result_isClicked,
              )
btn15.config( height = 1, width = 1 )
btn15.pack(side = LEFT,expand=True , fill="both")
#----------------button 16--------------------
btn16 = Button(frm4,
              text="÷",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#00FFFF",
              highlightthickness=0,
              command = buttonFor_divide_isClicked,
              )
btn16.config( height = 1, width = 1 )
btn16.pack(side = LEFT,expand=True , fill="both")
#----------------button 17--------------------
btn17 = Button(frm1,
              text="√",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#00FFFF",
              highlightthickness=0,
              command = buttonFor_sqroot_isClicked,
              )
btn17.config( height = 2, width = 1 )
btn17.pack(side = LEFT,expand=True , fill="both")
#----------------button 18--------------------
btn18 = Button(frm2,
              text="x²",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#00FFFF",
              highlightthickness=0,
              command = buttonFor_sq_isClicked,
              )
btn18.config( height = 1, width = 1 )
btn18.pack(side = LEFT,expand=True , fill="both")
#----------------button 19--------------------
btn19 = Button(frm3,
              text=".",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#00FFFF",
              highlightthickness=0,
              command = buttonFor_dot_isClicked,
              )
btn19.config( height = 1, width = 1 )
btn19.pack(side = LEFT,expand=True , fill="both")
#----------------button 20--------------------
btn20 = Button(frm4,
              text="⌫",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#696969",
              fg = "#00FFFF",
              highlightthickness=0,
              command = buttonFro_del_isClickled,
              )
btn20.config( height = 2, width = 1 )
btn20.pack(side = LEFT,expand=True , fill="both")
#----------------button 21------------------------
btn21 = Button(frm5,
              text = "^",
              font=("Verdena ", 22),
              relief = GROOVE,
	      border = 0,
              bg = "#000000",
              fg = "#00FFFF",
              highlightthickness=0,
              command = buttonFor_saf_isClicked
)
btn21.config( height = 1, width = 1, bg = "#05ACF5", fg = "#ffffff" )
btn21.pack(side = BOTTOM, expand=True, fill="both")
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
root.mainloop()











