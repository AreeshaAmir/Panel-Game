import sys
from tkinter import *
from tkinter import messagebox

TotalScore = 0


# ****************************** Scoring and Validation ************************************

def initialize(window):
    window.title("panel game")
    window.resizable(0, 0)

    w = int(window.winfo_screenwidth() / 2)
    h = int(window.winfo_screenheight() / 1.5)  # height for the Tk root

    # get screen width and height
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.configure(background="#993366")

    frame = Frame(window)
    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.40, relheight=0.15, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="WELCOME TO PANEL GAME")
    wel_note.configure(justify="center")
    wel_note.configure(font="Algerian 22")
    wel_note.configure(width=800)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(command=lambda: Category1_RD1(frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


def Total(AnswerDict):
    key = list(AnswerDict.keys())[0]
    KeyList = AnswerDict[list(AnswerDict.keys())[0]]

    global TotalScore

    # ************* Category 1 ****************
    # Round 1
    if key == 'C1R1':
        if KeyList[0] == 2:
            TotalScore += 1
        if KeyList[1] == 1:
            TotalScore += 1
        if KeyList[2] == 1:
            TotalScore += 1

    # Round 2
    elif key == 'C1R2':
        if KeyList[0] == 2:
            TotalScore += 1
        if KeyList[1] == 1:
            TotalScore += 1
        if KeyList[2] == 2:
            TotalScore += 1

    # Round 3
    elif key == 'C1R3':
        if KeyList[0] == 1:
            TotalScore += 1
        if KeyList[1] == 1:
            TotalScore += 1
        if KeyList[2] == 3:
            TotalScore += 1
        if KeyList[3] == 1:
            TotalScore += 1

    # ************* Category 2 ****************
    # Round 1
    if key == 'C2R1':
        if KeyList[0] == 2:
            TotalScore += 1
        if KeyList[1] == 2:
            TotalScore += 1
        if KeyList[2] == 2:
            TotalScore += 1

    # Round 2
    elif key == 'C2R2':
        if KeyList[0] == 1:
            TotalScore += 1
        if KeyList[1] == 1:
            TotalScore += 1
        if KeyList[2] == 1:
            TotalScore += 1

    # Round 3
    elif key == 'C2R3':
        if KeyList[0] == 3:
            TotalScore += 1
        if KeyList[1] == 1:
            TotalScore += 1
        if KeyList[2] == 1:
            TotalScore += 1
        if KeyList[3] == 1:
            TotalScore += 1

    # ************* Category 3 ****************
    # Round 1
    if key == 'C3R1':
        if KeyList[0] == 3:
            TotalScore += 1
        if KeyList[1] == 1:
            TotalScore += 1
        if KeyList[2] == 2:
            TotalScore += 1

    # Round 2
    elif key == 'C3R2':
        if KeyList[0] == 2:
            TotalScore += 1
        if KeyList[1] == 2:
            TotalScore += 1
        if KeyList[2] == 2:
            TotalScore += 1

    # Round 3
    elif key == 'C3R3':
        if KeyList[0] == 3:
            TotalScore += 1
        if KeyList[1] == 1:
            TotalScore += 1
        if KeyList[2] == 2:
            TotalScore += 1
        if KeyList[3] == 1:
            TotalScore += 1

    # ************* Category 4 ****************
    # Round 1
    if key == 'C4R1':
        if KeyList[0] == 3:
            TotalScore += 1
        if KeyList[1] == 2:
            TotalScore += 1
        if KeyList[2] == 1:
            TotalScore += 1

    # Round 2
    elif key == 'C4R2':
        if KeyList[0] == 1:
            TotalScore += 1
        if KeyList[1] == 2:
            TotalScore += 1
        if KeyList[2] == 2:
            TotalScore += 1

    # Round 3
    elif key == 'C4R3':
        if KeyList[0] == 3:
            TotalScore += 1
        if KeyList[1] == 2:
            TotalScore += 1
        if KeyList[2] == 3:
            TotalScore += 1
        if KeyList[3] == 1:
            TotalScore += 1


def Validation(AnswerDict, Funct, frame, window):
    AnswerList = AnswerDict[list(AnswerDict.keys())[0]]

    if AnswerList.count(0) > 0:
        messagebox.showerror("Error", "Please Select an Option")
    else:
        Total(AnswerDict)
        if Funct is not None:
            Funct(frame, window)
        else:
            global TotalScore
            Percentage = round(100 * TotalScore / 40, 2)
            if Percentage > 50:
                Result_Msg = 'Total Score: ' + str(TotalScore) + '\n' + \
                             'Percentage: ' + str(Percentage) + '%' + \
                             '\nCongratulations! You Passed'
            else:
                Result_Msg = 'Total Score: ' + str(TotalScore) + '\n' + \
                             'Percentage: ' + str(Percentage) + '%' + \
                             '\nSorry! You Failed'

            messagebox.showinfo('Result', Result_Msg,
                                icon='info')
            window.destroy()


# ******************************************************************************************
# ************************************* Category 1 *****************************************
# ******************************************************************************************

# Round 1
def Category1_RD1(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.06, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 1 
     HAZRAT MUHAMMAD (S.A.W.W)
    (Round 1)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.05, rely=0.23, height=35, width=400)
    q1_msg.configure(width=400)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.On which animal Hazrat Muhammad (S.A.W.W) migrated to madina?")

    q1_ans1 = Radiobutton(frame, text="Hourse", font="Times 10", background="#E7C4C4", value=1, variable=q1Var)
    q1_ans1.place(relx=0, rely=0.28, height=25, width=200)
    q1_ans2 = Radiobutton(frame, text="Camel", font="Times 10", background="#E7C4C4", value=2, variable=q1Var)
    q1_ans2.place(relx=0.06, rely=0.32, height=25, width=115)
    q1_ans3 = Radiobutton(frame, text="Elephant", font="Times 10", background="#E7C4C4", value=3, variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.36, height=25, width=140)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.05, rely=0.43, height=25, width=170)
    q2_msg.configure(width=400)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.The meaning of Rasool is?")

    q2_ans1 = Radiobutton(frame, text="messenger", font="Times 10", background="#E7C4C4", value=1, variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.49, height=25, width=150)
    q2_ans2 = Radiobutton(frame, text="Guard", font="Times 10", background="#E7C4C4", value=2, variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.53, height=25, width=125)
    q2_ans3 = Radiobutton(frame, text="Distributor", font="Times 10", background="#E7C4C4", value=3, variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.57, height=25, width=150)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.05, rely=0.62, height=35, width=250)
    q3_msg.configure(width=700)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.Hazrat Muhammad (S.A.W.W) born in ?")

    q3_ans1 = Radiobutton(frame, text="Makkah", font="Times 10", background="#E7C4C4", value=1,
                          variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.68, height=30, width=130)
    q3_ans2 = Radiobutton(frame, text="Madina", font="Times 10", background="#E7C4C4", value=2,
                          variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.72, height=30, width=130)
    q3_ans3 = Radiobutton(frame, text="Taif", font="Times 10", background="#E7C4C4", value=3,
                          variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.76, height=30, width=110)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C1R1': [q1Var.get(), q2Var.get(), q3Var.get()]}, Category1_RD2, frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# Round 2
def Category1_RD2(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.09, rely=0.09, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 1 
    HAZRAT MUHAMMAD (S.A.W.W)
    (Round 2)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.08, rely=0.23, height=35, width=300)
    q1_msg.configure(width=500)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.Hazrat Muhammad (S.A.W.W )died at the age of?")

    q1_ans1 = Radiobutton(frame, text="65 years", font="Times 10", background="#E7C4C4", value=1, variable=q1Var)
    q1_ans1.place(relx=0, rely=0.28, height=25, width=285)
    q1_ans2 = Radiobutton(frame, text="63 years", font="Times 10", background="#E7C4C4", value=2, variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.32, height=25, width=220)
    q1_ans3 = Radiobutton(frame, text="61 years", font="Times 10", background="#E7C4C4", value=3, variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.36, height=25, width=220)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.09, rely=0.42, height=25, width=450)
    q2_msg.configure(width=500)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.To whom the Holy Prophet (S.A.W.W) went after the revelation of the first wahi? ")

    q2_ans1 = Radiobutton(frame, text="Hazrat Khadija (R.A)", font="Times 10", background="#E7C4C4", value=1,
                          variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.47, height=25, width=280)
    q2_ans2 = Radiobutton(frame, text="Hazrat Abu Bakar Siddique(R.A) ", font="Times 10", background="#E7C4C4", value=2,
                          variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.51, height=25, width=345)
    q2_ans3 = Radiobutton(frame, text="Hazrat Bin Abu Talib (R.A)", font="Times 10", background="#E7C4C4", value=3,
                          variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.55, height=25, width=312)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.001, rely=0.61, height=25, width=490)
    q3_msg.configure(width=500)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.When did Hazrat Muhmmad (S.A.W.W) perform 'Hajjat-ul-Wada?' ")

    q3_ans1 = Radiobutton(frame, text="630 A.D", font="Times 10", background="#E7C4C4", value=1, variable=q3Var)
    q3_ans1.place(relx=0.06, rely=0.66, height=25, width=200)
    q3_ans2 = Radiobutton(frame, text="632 A.D", font="Times 10", background="#E7C4C4", value=2, variable=q3Var)
    q3_ans2.place(relx=0.07, rely=0.70, height=25, width=185)
    q3_ans3 = Radiobutton(frame, text="627 A.D", font="Times 10", background="#E7C4C4", value=3, variable=q3Var)
    q3_ans3.place(relx=0.07, rely=0.74, height=25, width=185)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C1R2': [q1Var.get(), q2Var.get(), q3Var.get()]}, Category1_RD3, frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# Round 3
def Category1_RD3(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()
    q4Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 1 
    HAZRAT MUHAMMAD (S.A.W.W)
    (Round 3)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.01, rely=0.23, height=25, width=300)
    q1_msg.configure(width=500)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.Which was the fisrt battle fought against Makkah?")

    q1_ans1 = Radiobutton(frame, text="Badar", font="Times 10", background="#E7C4C4", value=1,
                          variable=q1Var)
    q1_ans1.place(relx=0, rely=0.28, height=25, width=160)
    q1_ans2 = Radiobutton(frame, text="Tabook", font="Times 10", background="#E7C4C4", value=2,
                          variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.32, height=25, width=103)
    q1_ans3 = Radiobutton(frame, text="Khandaq", font="Times 10", background="#E7C4C4", value=3,
                          variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.36, height=25, width=111)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.01, rely=0.45, height=25, width=390)
    q2_msg.configure(width=500)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.Holy Prophet (S.A.W.W)  delivered his farewell sermon at Arafat on?")

    q2_ans1 = Radiobutton(frame, text="10th of Dhul Hijjah", font="Times 10", background="#E7C4C4",
                          value=1, variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.49, height=25, width=160)
    q2_ans2 = Radiobutton(frame, text="11th of Dhul Hijjah", font="Times 10", background="#E7C4C4",
                          value=2, variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.53, height=25, width=160)
    q2_ans3 = Radiobutton(frame, text="9th of Dhul Hijjah", font="Times 10", background="#E7C4C4",
                          value=3, variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.57, height=25, width=155)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.019, rely=0.62, height=35, width=400)
    q3_msg.configure(width=500)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.The attributive name of the Holy Prophet (S.A.W.W), 'AHMAD' means??")

    q3_ans1 = Radiobutton(frame, text="The Commander", font="Times 10", background="#E7C4C4", value=1,
                          variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.68, height=30, width=145)
    q3_ans2 = Radiobutton(frame, text="The Chaste", font="Times 10", background="#E7C4C4",
                          value=2, variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.72, height=30, width=119)
    q3_ans3 = Radiobutton(frame, text="The Most Commandable", font="Times 10", background="#E7C4C4",
                          value=3, variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.76, height=30, width=188)

    q4_msg = Message(frame)
    q4_msg.place(relx=0.46, rely=0.23, height=30, width=350)
    q4_msg.configure(width=500)
    q4_msg.configure(background="#E7C4C4")
    q4_msg.configure(text="4..Hazrat Muhammad (S.A.W.W) tribe is? ")

    q4_ans1 = Radiobutton(frame, text="Quraish", font="Times 10", background="#E7C4C4",
                          value=1, variable=q4Var)
    q4_ans1.place(relx=0.45, rely=0.28, height=25, width=240)
    q4_ans2 = Radiobutton(frame, text="Banu Ummayan", font="Times 10", background="#E7C4C4",
                          value=2, variable=q4Var)
    q4_ans2.place(relx=0.50, rely=0.32, height=25, width=217)
    q4_ans3 = Radiobutton(frame, text="Bano Nuzair", font="Times 10", background="#E7C4C4",
                          value=3, variable=q4Var)
    q4_ans3.place(relx=0.50, rely=0.36, height=25, width=196)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C1R3': [q1Var.get(), q2Var.get(), q3Var.get(), q4Var.get()]}, Category2_RD1, frame,
                                   window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# ******************************************************************************************
# ************************************* Category 2 *****************************************
# ******************************************************************************************

# Round 1
def Category2_RD1(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 2 
    HOLY QURAN
    (Round 1)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.01, rely=0.23, height=25, width=280)
    q1_msg.configure(width=300)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.How many surahs are there in Quran?")

    q1_ans1 = Radiobutton(frame, text="115", font="Times 10", background="#E7C4C4", value=1,
                          variable=q1Var)
    q1_ans1.place(relx=0, rely=0.28, height=25, width=200)
    q1_ans2 = Radiobutton(frame, text="114", font="Times 10", background="#E7C4C4", value=2,
                          variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.32, height=25, width=133)
    q1_ans3 = Radiobutton(frame, text="111", font="Times 10", background="#E7C4C4", value=3,
                          variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.36, height=25, width=130)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.060, rely=0.45, height=25, width=280)
    q2_msg.configure(width=300)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.What is the name of shortest surah of the Quran?")

    q2_ans1 = Radiobutton(frame, text="Surah An Naas", font="Times 10", background="#E7C4C4",
                          value=1, variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.49, height=25, width=190)
    q2_ans2 = Radiobutton(frame, text="Surah Kausar", font="Times 10", background="#E7C4C4",
                          value=2, variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.53, height=25, width=179)
    q2_ans3 = Radiobutton(frame, text="Surah Ikhlas", font="Times 10", background="#E7C4C4",
                          value=3, variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.57, height=25, width=171)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.066, rely=0.62, height=35, width=295)
    q3_msg.configure(width=300)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.What is the name of the longest surah of the Quran?")

    q3_ans1 = Radiobutton(frame, text="Surah Yusuf", font="Times 10", background="#E7C4C4",
                          value=1, variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.68, height=30, width=170)
    q3_ans2 = Radiobutton(frame, text="Surah-Al-Baqarah", font="Times 10", background="#E7C4C4",
                          value=2, variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.72, height=30, width=200)
    q3_ans3 = Radiobutton(frame, text="Surah-Al-Imran", font="Times 10", background="#E7C4C4",
                          value=3, variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.76, height=30, width=185)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C2R1': [q1Var.get(), q2Var.get(), q3Var.get()]}, Category2_RD2, frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# Round 2
def Category2_RD2(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 2 
    HOLY QURAN
    (Round 2)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.006, rely=0.23, height=35, width=390)
    q1_msg.configure(width=300)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.How many Ayat and Ruku are there in Quran?")

    q1_ans1 = Radiobutton(frame, text="558 and 6666", font="Times 10", background="#E7C4C4", value=1,
                          variable=q1Var)
    q1_ans1.place(relx=0, rely=0.28, height=25, width=290)
    q1_ans2 = Radiobutton(frame, text="556 and 6664", font="Times 10", background="#E7C4C4", value=2,
                          variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.32, height=25, width=225)
    q1_ans3 = Radiobutton(frame, text="554 and 6665", font="Times 10", background="#E7C4C4", value=3,
                          variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.36, height=25, width=225)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.070, rely=0.44, height=25, width=400)
    q2_msg.configure(width=500)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2. What are the numbers of Madni Surahs Makki Surahs in Quran?")

    q2_ans1 = Radiobutton(frame, text="28 and 86", font="Times 10", background="#E7C4C4", value=1,
                          variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.49, height=25, width=200)
    q2_ans2 = Radiobutton(frame, text="26 and 88", font="Times 10", background="#E7C4C4", value=2,
                          variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.53, height=25, width=200)
    q2_ans3 = Radiobutton(frame, text="24 and 83", font="Times 10", background="#E7C4C4", value=3,
                          variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.57, height=25, width=200)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.095, rely=0.62, height=35, width=500)
    q3_msg.configure(width=500)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(
        text="3.How many virtues are found in the recitation of each letter of the each letter of the Quran?")

    q3_ans1 = Radiobutton(frame, text="10", font="Times 10", background="#E7C4C4", value=1,
                          variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.68, height=30, width=165)
    q3_ans2 = Radiobutton(frame, text="15", font="Times 10", background="#E7C4C4", value=2,
                          variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.72, height=30, width=160)
    q3_ans3 = Radiobutton(frame, text="20", font="Times 10", background="#E7C4C4", value=3,
                          variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.76, height=30, width=160)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C2R2': [q1Var.get(), q2Var.get(), q3Var.get()]}, Category2_RD3, frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# Round 3
def Category2_RD3(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()
    q4Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 2 
    HOLY QURAN
    (Round 3)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.009, rely=0.23, height=30, width=330)
    q1_msg.configure(width=320)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.According to the Quran,the standard of honor is on whom?")

    q1_ans1 = Radiobutton(frame, text="Gender", font="Times 10", background="#E7C4C4", value=1,
                          variable=q1Var)
    q1_ans1.place(relx=0, rely=0.29, height=25, width=230)
    q1_ans2 = Radiobutton(frame, text="Taqwah ", font="Times 10", background="#E7C4C4", value=2,
                          variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.33, height=25, width=170)
    q1_ans3 = Radiobutton(frame, text="Worship", font="Times 10", background="#E7C4C4", value=3,
                          variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.37, height=25, width=170)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.001, rely=0.45, height=25, width=340)
    q2_msg.configure(width=300)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.In Quran Imam-Un-Nas is the title of which prophet?")

    q2_ans1 = Radiobutton(frame, text="Hazrat Ibrahim (A.S)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.49, height=25, width=230)
    q2_ans2 = Radiobutton(frame, text="Hazrat Nooh (A.S)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.53, height=25, width=220)
    q2_ans3 = Radiobutton(frame, text="Hazrat Haroon (A.S)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.57, height=25, width=230)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.001, rely=0.62, height=35, width=390)
    q3_msg.configure(width=380)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.At what age was the Holy Quran revealed to the Holy Prophet?")

    q3_ans1 = Radiobutton(frame, text="40", font="Times 10", background="#E7C4C4", value=1,
                          variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.68, height=30, width=130)
    q3_ans2 = Radiobutton(frame, text="45", font="Times 10", background="#E7C4C4", value=2,
                          variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.72, height=30, width=130)
    q3_ans3 = Radiobutton(frame, text="60", font="Times 10", background="#E7C4C4", value=3,
                          variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.76, height=30, width=130)

    q4_msg = Message(frame)
    q4_msg.place(relx=0.45, rely=0.21, height=35, width=400)
    q4_msg.configure(width=400)
    q4_msg.configure(background="#E7C4C4")
    q4_msg.configure(text="4.What are the stages of revelation of the Holy Quran? ")

    q4_ans1 = Radiobutton(frame, text="2", font="Times 10", background="#E7C4C4", value=1,
                          variable=q4Var)
    q4_ans1.place(relx=0.45, rely=0.28, height=25, width=200)
    q4_ans2 = Radiobutton(frame, text="4", font="Times 10", background="#E7C4C4", value=2,
                          variable=q4Var)
    q4_ans2.place(relx=0.50, rely=0.32, height=25, width=130)
    q4_ans3 = Radiobutton(frame, text="6", font="Times 10", background="#E7C4C4", value=3,
                          variable=q4Var)
    q4_ans3.place(relx=0.50, rely=0.36, height=25, width=130)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C2R3': [q1Var.get(), q2Var.get(), q3Var.get(), q4Var.get()]}, Category3_RD1, frame,
                                   window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# ******************************************************************************************
# ************************************* Category 3 *****************************************
# ******************************************************************************************

# Round 1
def Category3_RD1(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 3 
    QASASUL AMBIA 
    (Round 1)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.005, rely=0.23, height=35, width=400)
    q1_msg.configure(width=300)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.What is the name of Hazrat Ibrahim AS's father? ")

    q1_ans1 = Radiobutton(frame, text="Zubair", font="Times 10", background="#E7C4C4", value=1,
                          variable=q1Var)
    q1_ans1.place(relx=0, rely=0.28, height=25, width=235)
    q1_ans2 = Radiobutton(frame, text="Imran", font="Times 10", background="#E7C4C4", value=2,
                          variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.32, height=25, width=165)
    q1_ans3 = Radiobutton(frame, text="Azar", font="Times 10", background="#E7C4C4", value=3,
                          variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.36, height=25, width=160)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.004, rely=0.43, height=25, width=390)
    q2_msg.configure(width=300)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.What is the name of Hazrat Yusuf A.S's father?")

    q2_ans1 = Radiobutton(frame, text="Hazrat Yaqoob (A.S)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.48, height=25, width=232)
    q2_ans2 = Radiobutton(frame, text="Hazrat Ibrahim (A.S)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.52, height=25, width=230)
    q2_ans3 = Radiobutton(frame, text="Hazrat Ishaq (A.S)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.56, height=25, width=220)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.06, rely=0.62, height=35, width=400)
    q3_msg.configure(width=500)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.Which Prohpet had the knowledge of interpretation of dreams?")

    q3_ans1 = Radiobutton(frame, text="Hazrat Yaqoob (A.S)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.68, height=30, width=230)
    q3_ans2 = Radiobutton(frame, text="Hazrat Yusuf (A.S)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.72, height=30, width=220)
    q3_ans3 = Radiobutton(frame, text="Hazrat Ibrahim (A.S)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.76, height=30, width=227)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C3R1': [q1Var.get(), q2Var.get(), q3Var.get()]}, Category3_RD2, frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# Round 2
def Category3_RD2(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 3 
    QASASUL AMBIA
    (Round 2)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.005, rely=0.23, height=35, width=340)
    q1_msg.configure(width=300)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.At which location Hazrat Nuh AS's ship stop?")

    q1_ans1 = Radiobutton(frame, text="River Nile", font="Times 10", background="#E7C4C4",
                          value=1, variable=q1Var)
    q1_ans1.place(relx=0, rely=0.28, height=25, width=260)
    q1_ans2 = Radiobutton(frame, text="Syria", font="Times 10", background="#E7C4C4", value=2,
                          variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.32, height=25, width=170)
    q1_ans3 = Radiobutton(frame, text="Baitul-Muqaddas", font="Times 10", background="#E7C4C4",
                          value=3, variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.36, height=25, width=235)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.005, rely=0.42, height=25, width=350)
    q2_msg.configure(width=300)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.What is the name of Hazrat Ismail A.S's mother?")

    q2_ans1 = Radiobutton(frame, text="Bibi Sara", font="Times 10", background="#E7C4C4",
                          value=1, variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.46, height=25, width=185)
    q2_ans2 = Radiobutton(frame, text="Bibi Hajra", font="Times 10", background="#E7C4C4",
                          value=2, variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.50, height=25, width=190)
    q2_ans3 = Radiobutton(frame, text="Bibi Asia", font="Times 10", background="#E7C4C4",
                          value=3, variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.54, height=25, width=185)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.006, rely=0.60, height=35, width=380)
    q3_msg.configure(width=300)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.Who was the Prophet who was swallowed by the fish?")

    q3_ans1 = Radiobutton(frame, text="Hazrat Salman(R.A)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.66, height=30, width=240)
    q3_ans2 = Radiobutton(frame, text="Hazrat Yunus (A.S)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.70, height=30, width=240)
    q3_ans3 = Radiobutton(frame, text="Hazrat Saleh (A.S)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.74, height=30, width=230)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C3R2': [q1Var.get(), q2Var.get(), q3Var.get()]}, Category3_RD3, frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# Round 3
def Category3_RD3(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()
    q4Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 3 
    QASASUL AMBIA
    (Round 3)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.032, rely=0.23, height=35, width=277)
    q1_msg.configure(width=300)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(
        text="1.What is the name of Hazrat Nuh (A.S)'s disobedient son who climed the mountain at the time of deluge?")

    q1_ans1 = Radiobutton(frame, text="Yaam", font="Times 10", background="#E7C4C4", value=1,
                          variable=q1Var)
    q1_ans1.place(relx=0, rely=0.30, height=25, width=170)
    q1_ans2 = Radiobutton(frame, text="Haam", font="Times 10", background="#E7C4C4", value=2,
                          variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.34, height=25, width=100)
    q1_ans3 = Radiobutton(frame, text="Can'an", font="Times 10", background="#E7C4C4", value=3,
                          variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.38, height=25, width=104)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.001, rely=0.42, height=35, width=280)
    q2_msg.configure(width=300)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.What is the name of Hazrat Lut A.S's nation?")

    q2_ans1 = Radiobutton(frame, text="Aad", font="Times 10", background="#E7C4C4", value=1,
                          variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.47, height=25, width=90)
    q2_ans2 = Radiobutton(frame, text="Hud", font="Times 10", background="#E7C4C4", value=2,
                          variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.51, height=25, width=90)
    q2_ans3 = Radiobutton(frame, text="Thamud", font="Times 10", background="#E7C4C4", value=3,
                          variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.55, height=25, width=109)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.030, rely=0.61, height=43, width=350)
    q3_msg.configure(width=390)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.How many days did Hazrat Ibrahim A.S stay in the fire caused by nimrod?")

    q3_ans1 = Radiobutton(frame, text="30 days", font="Times 10", background="#E7C4C4", value=1,
                          variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.680, height=30, width=100)
    q3_ans2 = Radiobutton(frame, text="40 days", font="Times 10", background="#E7C4C4", value=2,
                          variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.723, height=30, width=100)
    q3_ans3 = Radiobutton(frame, text="60 days", font="Times 10", background="#E7C4C4", value=3,
                          variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.77, height=30, width=100)

    q4_msg = Message(frame)
    q4_msg.place(relx=0.50, rely=0.22, height=35, width=340)
    q4_msg.configure(width=400)
    q4_msg.configure(background="#E7C4C4")
    q4_msg.configure(text="4.What do we call the story of Hazrat Yusuf A.S's in Quran?")

    q4_ans1 = Radiobutton(frame, text="Ahsan-ul-Qasas", font="Times 10", background="#E7C4C4",
                          value=1, variable=q4Var)
    q4_ans1.place(relx=0.45, rely=0.28, height=25, width=300)
    q4_ans2 = Radiobutton(frame, text="Heart of Quran", font="Times 10", background="#E7C4C4",
                          value=2, variable=q4Var)
    q4_ans2.place(relx=0.50, rely=0.32, height=25, width=225)
    q4_ans3 = Radiobutton(frame, text="Ayat-e-shifa", font="Times 10", background="#E7C4C4",
                          value=3, variable=q4Var)
    q4_ans3.place(relx=0.50, rely=0.36, height=25, width=215)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C3R3': [q1Var.get(), q2Var.get(), q3Var.get(), q4Var.get()]}, Category4_RD1, frame,
                                   window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# ******************************************************************************************
# ************************************* Category 4 *****************************************
# ******************************************************************************************

# Round 1
def Category4_RD1(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 4
    KHULFA-E-RASHIDEEN
    (Round 1)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.01, rely=0.23, height=35, width=340)
    q1_msg.configure(width=300)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.What is the name of Hazrat Maryam(R.A) father?")

    q1_ans1 = Radiobutton(frame, text="Hazrat Zikriya(R.A)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q1Var)
    q1_ans1.place(relx=0, rely=0.29, height=25, width=280)
    q1_ans2 = Radiobutton(frame, text="Hazrat Suhaib(R.A)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.33, height=25, width=215)
    q1_ans3 = Radiobutton(frame, text="Imran ibn hattan", font="Times 10", background="#E7C4C4",
                          value=3, variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.37, height=25, width=200)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.01, rely=0.42, height=25, width=400)
    q2_msg.configure(width=400)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.The compilation of Quran was in the time of which caliph?")

    q2_ans1 = Radiobutton(frame, text="Hazrat Umar(R.A)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.49, height=25, width=210)
    q2_ans2 = Radiobutton(frame, text="Hazrat Abu Bakr Siddique(R.A)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q2Var)
    q2_ans2.place(relx=0.03, rely=0.534, height=25, width=310)
    q2_ans3 = Radiobutton(frame, text="Hazrat Zubair(R.A)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.575, height=25, width=215)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.01, rely=0.62, height=35, width=360)
    q3_msg.configure(width=300)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.Hazrat Usman Ghani(R.A) belonged to which tribe?")

    q3_ans1 = Radiobutton(frame, text="Banu Ummaya", font="Times 10", background="#E7C4C4",
                          value=1, variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.68, height=30, width=195)
    q3_ans2 = Radiobutton(frame, text="Banu Hashim", font="Times 10", background="#E7C4C4",
                          value=2, variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.72, height=30, width=190)
    q3_ans3 = Radiobutton(frame, text="Banu Quraish", font="Times 10", background="#E7C4C4",
                          value=3, variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.76, height=30, width=190)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C4R1': [q1Var.get(), q2Var.get(), q3Var.get()]}, Category4_RD2, frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# Round 2
def Category4_RD2(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 4 
    KHULFA-E-RASHIDEEN
    (Round 2)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.05, rely=0.23, height=33, width=400)
    q1_msg.configure(width=400)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(
        text="1.About Which caliph did the Prophet(P.B.U.H) say that no one is more kind to me in terms of life and property?")

    q1_ans1 = Radiobutton(frame, text="Hazrat Abu Bakr siddique(R.A)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q1Var)
    q1_ans1.place(relx=0, rely=0.30, height=25, width=365)
    q1_ans2 = Radiobutton(frame, text="Hazrat Umair(R.A)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.34, height=25, width=230)
    q1_ans3 = Radiobutton(frame, text="Hazrat Zubair(R.A)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.38, height=25, width=234)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.015, rely=0.45, height=25, width=300)
    q2_msg.configure(width=300)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.Which caliph had the title of zulnurain?")

    q2_ans1 = Radiobutton(frame, text="Hazrat Umer(R.A)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.49, height=25, width=220)
    q2_ans2 = Radiobutton(frame, text="Hazrat Usman(R.A)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.53, height=25, width=230)
    q2_ans3 = Radiobutton(frame, text="Hazrat Abu Bakr Siddique(R.A)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.57, height=25, width=295)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.030, rely=0.61, height=62, width=450)
    q3_msg.configure(width=400)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.During the reign of which caliph the most islamic conquests took place?")

    q3_ans1 = Radiobutton(frame, text="Hazrat Usman(R.A)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.689, height=30, width=230)
    q3_ans2 = Radiobutton(frame, text="Hazrat Umer(R.A)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.73, height=30, width=220)
    q3_ans3 = Radiobutton(frame, text="Hazrat Abu Bakr Siddique(R.A)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.77, height=30, width=293)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Next -->")
    next_but.configure(
        command=lambda: Validation({'C4R2': [q1Var.get(), q2Var.get(), q3Var.get()]}, Category4_RD3, frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


# Round 3
def Category4_RD3(frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    q1Var = IntVar()
    q2Var = IntVar()
    q3Var = IntVar()
    q4Var = IntVar()

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(borderwidth="2")
    frame.configure(background="#E7C4C4")

    wel_note = Message(frame)
    wel_note.place(relx=0.05, rely=0.05, relheight=0.17, relwidth=0.90)
    wel_note.configure(background="#E7C4C4")
    wel_note.configure(text="""Category 4 
    KHULFA-E-RASHIDEEN
    (Round 3)""")
    wel_note.configure(justify="center")
    wel_note.configure(font="Times 13")
    wel_note.configure(width=800)

    q1_msg = Message(frame)
    q1_msg.place(relx=0.001, rely=0.24, height=35, width=340)
    q1_msg.configure(width=300)
    q1_msg.configure(background="#E7C4C4")
    q1_msg.configure(text="1.What was the name of the man who martyred Hazrat Umer farooq(R.A)?")

    q1_ans1 = Radiobutton(frame, text="Bilal", font="Times 10", background="#E7C4C4", value=1,
                          variable=q1Var)
    q1_ans1.place(relx=0, rely=0.31, height=25, width=180)
    q1_ans2 = Radiobutton(frame, text="Usman", font="Times 10", background="#E7C4C4", value=2,
                          variable=q1Var)
    q1_ans2.place(relx=0.05, rely=0.345, height=25, width=130)
    q1_ans3 = Radiobutton(frame, text="Abu lulu Feroz", font="Times 10", background="#E7C4C4",
                          value=3, variable=q1Var)
    q1_ans3.place(relx=0.05, rely=0.385, height=25, width=172)

    q2_msg = Message(frame)
    q2_msg.place(relx=0.001, rely=0.445, height=25, width=240)
    q2_msg.configure(width=300)
    q2_msg.configure(background="#E7C4C4")
    q2_msg.configure(text="2.What is the name of firoon's wife?")

    q2_ans1 = Radiobutton(frame, text="Hazrat Sarah(R.A)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q2Var)
    q2_ans1.place(relx=0.05, rely=0.495, height=25, width=185)
    q2_ans2 = Radiobutton(frame, text="Hazrat Asia(R.A)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q2Var)
    q2_ans2.place(relx=0.05, rely=0.535, height=25, width=180)
    q2_ans3 = Radiobutton(frame, text="Hazrat Zulaikha(R.A)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q2Var)
    q2_ans3.place(relx=0.05, rely=0.575, height=25, width=200)

    q3_msg = Message(frame)
    q3_msg.place(relx=0.005, rely=0.61, height=89, width=400)
    q3_msg.configure(width=350)
    q3_msg.configure(background="#E7C4C4")
    q3_msg.configure(text="3.How many years has the total rule of the Rightly Guided Caliphs spanned? ")

    q3_ans1 = Radiobutton(frame, text="60 years", font="Times 10", background="#E7C4C4", value=1,
                          variable=q3Var)
    q3_ans1.place(relx=0.05, rely=0.74, height=30, width=140)
    q3_ans2 = Radiobutton(frame, text="50 years", font="Times 10", background="#E7C4C4", value=2,
                          variable=q3Var)
    q3_ans2.place(relx=0.05, rely=0.78, height=30, width=140)
    q3_ans3 = Radiobutton(frame, text="30 years", font="Times 10", background="#E7C4C4", value=3,
                          variable=q3Var)
    q3_ans3.place(relx=0.05, rely=0.82, height=30, width=140)

    q4_msg = Message(frame)
    q4_msg.place(relx=0.50, rely=0.229, height=35, width=300)
    q4_msg.configure(width=300)
    q4_msg.configure(background="#E7C4C4")
    q4_msg.configure(text="4.Whose title is Lion Of Allah?")

    q4_ans1 = Radiobutton(frame, text="Hazrat Ali(R.A)", font="Times 10", background="#E7C4C4",
                          value=1, variable=q4Var)
    q4_ans1.place(relx=0.45, rely=0.28, height=25, width=360)
    q4_ans2 = Radiobutton(frame, text="Hazrat Usman(R.A)", font="Times 10", background="#E7C4C4",
                          value=2, variable=q4Var)
    q4_ans2.place(relx=0.50, rely=0.32, height=25, width=318)
    q4_ans3 = Radiobutton(frame, text="Hazrat Umer(R.A)", font="Times 10", background="#E7C4C4",
                          value=3, variable=q4Var)
    q4_ans3.place(relx=0.50, rely=0.36, height=25, width=308)

    next_but = Button(frame)
    next_but.place(relx=0.85, rely=0.92, height=35, width=100)
    next_but.configure(background="#E7C4C4")
    next_but.configure(text="Finish")
    next_but.configure(
        command=lambda: Validation({'C4R3': [q1Var.get(), q2Var.get(), q3Var.get(), q4Var.get()]}, None, frame, window))

    exit_but = Button(frame)
    exit_but.place(relx=0.01, rely=0.92, height=35, width=100)
    exit_but.configure(background="#E7C4C4")
    exit_but.configure(text="Exit Now", command=window.destroy)


if __name__ == "__main__":
    root = Tk()
    Window = initialize(root)
    root.mainloop()
