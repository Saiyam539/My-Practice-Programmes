import PyPDF2
import pyttsx3
from tkinter import *

def read_text():
    page_num = int(page_number.get())
    path_name = path.get()
    pyttsx3.speak("Welcome to PDF Reader")

    file = open(path_name,"rb")

    fileReader = PyPDF2.PdfFileReader(file)
    page = fileReader.getPage(page_num-1)
    page_content = page.extractText()
    pyttsx3.speak(page_content)

window = Tk()
window.geometry("500x600")
window.minsize(600,500)
window.maxsize(600,500)
window.title("PDF Reader")
window.configure(background="light grey")

heading = Label(window, text="PDF Reader", font=("Arial Bold", 40), fg="white", bg="black")
heading.pack(fill=X)

label1 = Label(window, text="Enter the path of the PDF file below", font=("Arial Bold", 30),background="light grey")
label1.pack(fill=X, pady=20)
path = Entry(window, width=50, font=("Arial Bold", 25),bg="grey")
path.pack(fill=X, pady=5)

label2 = Label(window, text="Enter the page number you want to read below", font=("Arial Bold", 25),background="light grey")
label2.pack(fill=X, pady=20)
page_number = Entry(window, width=30, font=("Arial Bold", 25),bg="grey")
page_number.pack(fill=X, pady=5)

button = Button(window, text="Read", font=("Arial Bold", 25), command=lambda:read_text(), bg="grey")
button.pack(pady=20)

window.mainloop()