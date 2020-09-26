# Import Modules
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import pyttsx3, time

root =Tk()
root.config(background="Black")
root.title("Quiz")


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    time.sleep(0.000000000000000000000000000000000000000000000000000001)

# Entering image
img = Image.open("Title.png")
img = ImageTk.PhotoImage(img)

def correct_answer_q1():
    messagebox.showinfo("Correct answer",
                        "You have selected the correct answer!! ")
    q1_scr.destroy()

def wrong_answer_q1():
    messagebox.showerror("Wrong answer",
                        "You have selected a wrong answer. \nPlease reattempt the question")

def question_1():
    global q1_scr

    q1_scr = Toplevel(root)
    q1_scr.config(background="Black")
    q1_scr.title("Question 1")
    
    # Labels
    Label(q1_scr, text="Question 1", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=0, sticky=N, pady=5)
    Label(q1_scr, text="Add Question Here", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=1, sticky=N, pady=5)
    Label(q1_scr, text="Option A", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=2, sticky=W, pady=5)
    Label(q1_scr, text="Option B", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=3, sticky=W, pady=5)
    Label(q1_scr, text="Option C", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=4, sticky=W, pady=5)
    Label(q1_scr, text="Option D", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=5, sticky=W, pady=5)

    # Buttons
    Button(q1_scr, text="A", fg="Blue", bg="red", font=("Times new roman", 15), command=Correct_answer_q1.speaker, Correct_answer_q1.messenger).grid(row=2, sticky=W, pady=5, padx=250)
    Button(q1_scr, text="B", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q1).grid(row=3, sticky=W, pady=5, padx=250)
    Button(q1_scr, text="C", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q1).grid(row=4, sticky=W, pady=5, padx=250)
    Button(q1_scr, text="D", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q1).grid(row=5, sticky=W, pady=5, padx=250)

def correct_answer_q2():
    messagebox.showinfo("Correct answer",
                        "You have selected the correct answer!! ")
    q2_scr.destroy()

def wrong_answer_q2():
    messagebox.showerror("Wrong answer",
                        "You have selected a wrong answer. \nPlease reattempt the question")

def question_2():
    global q2_scr

    q2_scr = Toplevel(root)
    q2_scr.config(background="Black")
    q2_scr.title("Question 2")
    
    # Labels
    Label(q2_scr, text="Question 1", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=0, sticky=N, pady=5)
    Label(q2_scr, text="Add Question Here", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=1, sticky=N, pady=5)
    Label(q2_scr, text="Option A", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=2, sticky=W, pady=5)
    Label(q2_scr, text="Option B", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=3, sticky=W, pady=5)
    Label(q2_scr, text="Option C", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=4, sticky=W, pady=5)
    Label(q2_scr, text="Option D", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=5, sticky=W, pady=5)

    # Buttons
    Button(q2_scr, text="A", fg="Blue", bg="red", font=("Times new roman", 15), command=correct_answer_q2).grid(row=2, sticky=W, pady=5, padx=250)
    Button(q2_scr, text="B", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q2).grid(row=3, sticky=W, pady=5, padx=250)
    Button(q2_scr, text="C", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q2).grid(row=4, sticky=W, pady=5, padx=250)
    Button(q2_scr, text="D", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q2).grid(row=5, sticky=W, pady=5, padx=250)

# Labels
Label(root, text="Quiz", fg="Red", bg="Black", font=("Algerian", 20)).grid(row=0, column=2, sticky=N, pady=5)
Label(root, text="Questions", fg="green", bg="Black", font=("Times new Roman", 18)).grid(row=1, column=2, sticky=N, pady=5)
Label(root, image=img).grid(row=2, column=2, sticky=N, pady=5)

# Buttons
Button(root, text="Question 1", fg="red", bg="Orange", font=("calibri", 15), command=question_1).grid(row=4, sticky=W, column=1, pady=5, padx=10)
Button(root, text="Question 2", fg="red", bg="Orange", font=("calibri", 15), command=question_2).grid(row=4, sticky=W, column=3, pady=5, padx=10)

root.mainloop()