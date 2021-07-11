
from tkinter import *
from time import time
import random as r

questions = [
    # Bheem
    "What is this character's name? ",
    "Where does he live? ",
    "Which animal is his best friend? ",
    "Which is his favorite sweet?",
    # Doraemon
    "From which timeline did this character come from? ",
    "Who is the creator of this character? ",
    "What is this character scared of?",
    "What is  this character's specialty",
    # Tom and Jerry
    "Who created this series? ",
    "What is the cat's full name? ",
    "Who is the first owner of the cat? ",
    "What is Spike in this cartoon series?",
    # Shinchan
    "Which cartoon is this? ",
    "Which language was this originally made in?",
    "How many friends does he have?",
    "How many pets does this character have?",

]

answers_choice = [
    # Chota Bheem
    ["Raju", "Jaggu", "Chota Bheem", "Dhoni"],
    ["Bheemnagar", "Pehalwanpur", "Rampur", "Dholakpur"],
    ["Cat", "Monkey", "Buffalo", "Donkey"],
    ["Gulab Jamun", "Laddoo", "Rasgulla", "Jalebi"],
    # Doraemon
    ["Past", "Future", "Present", "A timeline which doesn't exist"],
    ["Fujiki Fujiho", "Yoshito Usui", "Masashi Kishimoto", "None of the above"],
    ["Assignments", "Rats", "Flies", "Cakes"],
    ["Creating fire from his bare hands ", "blow off mountains with a single blow", "Take out anything which is usable but has a drawback", "Nothing..."],
    # Tom and Jerry
    ["Walt Disney", "Hanna and Barbera", "Warner Bros", "Universal"],
    ["Tom cat", "Thomas cat", "Tommy cat", "Tom Riddle"],
    ["Mammy Two-Shoes", "Mammy Apron", "Aunt Rose", "Guille"],
    ["A Cat", "A Mouse", "A Dog", "A Bird"],
    # Shinchan
    ["Shinchan", "Horrid Henry", "Dexter", "Naruto"],
    ["English", "Hindi", "Japanese", "Korean"],
    ["1", "6", "3", "4"],
    ["2", "1", "4", "3"],

]

answers = [3,4,2,2, # Chota Bheem
           2,1,2,3, # Doraemon
           2,2,1,3, # Tom and Jerry
           1,3,4,2, # Shinchan
           ]
user_answer = []

indexes = []

def gen():
    global indexes
    i = 0
    while i <= 15:
        x = r.randint(0, 15)
        if x in indexes:
            continue
        else:
            indexes.append(x)
            i+=1


def showresult(score):
    lblQuestion.destroy()
    lblimage.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "white",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "white",
    )
    labelresulttext.pack()
    end_time = time()
    global start_time
    elapsed_time = str((end_time - start_time))[:4]

    s = str(score)
    if score >= 80:
        img = PhotoImage(file="Images/great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You scored "+s+"\n You Are Excellent !!"+"\nTime Taken :"+elapsed_time+" secs")
    elif (score >= 40 and score < 80):
        img = PhotoImage(file="Images/ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You scored "+s+"\n You Can Be Better !!"+"\n Time Taken :"+elapsed_time+" secs")
    else:
        img = PhotoImage(file="Images/bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You scored "+s+"\n You Should Work Hard !!"+"\n Time Taken :"+elapsed_time+" secs")

def calc():
    global indexes,user_answer,answers
    t = 0
    score = 0
    for i in indexes:
        #user_answer.pop(0)
        if user_answer[t]+1 == answers[i]:
            score += 5
        t += 1
    showresult(score)

def loadImage(d):
    global lblimage
    if (d <= 3):
        img = PhotoImage(file="Images/bheem.png")
        lblimage.config(image=img)
        lblimage.image = img
        lblimage.pack(before=lblQuestion)

    elif (d <= 7) and (d > 3):
        img = PhotoImage(file="Images/doraemon.png")
        lblimage.config(image=img)
        lblimage.image = img
        lblimage.pack(before=lblQuestion)

    elif (d <= 11) and (d > 7):
        img = PhotoImage(file="Images/tom_and_jerry.png")
        lblimage.config(image=img)
        lblimage.image = img
        lblimage.pack(before=lblQuestion)

    elif (d <= 15) and (d > 11):
        img = PhotoImage(file="Images/shinchan.png")
        lblimage.config(image=img)
        lblimage.image = img
        lblimage.pack(before=lblQuestion)

ques = 0
lblimage = None

def selected():
    global radiovar,user_answer
    x = radiovar.get()
    user_answer.append(x)
    global lblQuestion,r1,r2,r3,r4
    global ques
    if ques < 15:
        ques += 1
        loadImage(indexes[ques])
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
    else:
        calc()
    radiovar.set(-1)

start_time = 0

def startquiz():
    global start_time
    start_time = time()
    global lblQuestion,r1,r2,r3,r4

    lblQuestion = Label(root, text = questions[indexes[0]], font = ("Gabriola", 14), width = 480, justify = "center",
                        wraplength = 380, )
    lblQuestion.pack()
    global lblimage

    lblimage = Label(root, bg="white")
    print(indexes)
    global radiovar
    radiovar = IntVar(root)
    radiovar.set(-1)

    r1 = Radiobutton(root,
                     text = answers_choice[indexes[0]][0],
                     font = ("Times",13),
                     value = 0,
                     command = selected,
                     variable = radiovar,
                     )
    r1.pack()
    r2 = Radiobutton(root,
                     text = answers_choice[indexes[0]][1],
                     font=("Times", 13),
                     value=1,
                     command = selected,
                     variable=radiovar,
                     )
    r2.pack()
    r3 = Radiobutton(root,
                     text = answers_choice[indexes[0]][2],
                     font=("Times", 13),
                     value=2,
                     command = selected,
                     variable=radiovar,
                     )
    r3.pack()
    r4 = Radiobutton(root,
                     text = answers_choice[indexes[0]][3],
                     font=("Times", 13),
                     value=3,
                     command = selected,
                     variable=radiovar,
                     )
    r4.pack()
    loadImage(indexes[0])

def startIspressed():
    labeltext.destroy()
    lblinstrct.destroy()
    lblrules.destroy()
    buttonstart.destroy()
    gen()
    startquiz()

root = Tk()
root.title('Cartoon Quiz')
root.config(bg="white")

labeltext = Label(root,
                  text = 'Cartoon Quiz',
                  font = ("Gabriola", 44, "bold"),
                  bg = "white"
                  )

buttonstart = Button(root,
                     text ="Start",
                     bg = "green",
                     fg = "white",
                     font = ("Gabriola", 22, "bold"),
                     width = 8,
                     command = startIspressed
                     )
lblinstrct = Label(root,
                   text = "Read the rules\n Click Start once you are ready",
                   bg = "white",
                   font = ("Gabriola", 22, "bold"),
                   justify = "center"
                   )

lblrules = Label(root,
                 bg = "black",
                 fg = "Blue",
                 text = "RULES:\nThis quiz contains 5 images\nEach image will have 4 questions based on itself\n"
                        "Once you select a radio button that will be your final choice\nEach question carries 5 marks"
                        "\nHence think carefully before you answer",
                 font=("Times",16 ),
                 width = 480
                 )

labeltext.pack(pady = (0,48))
buttonstart.pack()
lblinstrct.pack()
lblrules.pack(side = "bottom")
root.mainloop()