import pbsc as pbsc
from tkinter import *
import tkinter as tk


class MyWindow:
    def __init__(self, win):
        lbl = Label(window, text="Prediksi Kepribadian dengan Algoritma PbSC",
                    fg='#4f8a8b', font=("Helvetica", 10))
        lbl.place(x=90, y=50)
        self.lbl1 = Label(win, text='Username Twitter')
        self.lbl3 = Label(win, text='Extroversion')
        self.lbl4 = Label(win, text='Agreeableness')
        self.lbl5 = Label(win, text='Conscientiousness')
        self.textSC = tk.StringVar()
        self.textER = tk.StringVar()
        self.textSC.set("")
        self.textER.set("")
        self.notif = tk.Label(win, textvariable=self.textSC, fg='green')
        self.error = tk.Label(win, textvariable=self.textER, fg='red')
        self.t1 = Entry(bd=3)
        self.t3 = Entry()
        self.t4 = Entry()
        self.t5 = Entry()
        self.btn1 = Button(win, text='Predict')
        self.lbl1.place(x=100, y=100)
        self.t1.place(x=220, y=100)
        self.b1 = Button(win, text='Predict', command=self.add)
        self.notif.place(x=100, y=210)
        self.error.place(x=100, y=200)
        self.b1.place(x=100, y=150)
        self.lbl3.place(x=100, y=270)
        self.t3.place(x=220, y=270)
        self.lbl4.place(x=100, y=320)
        self.t4.place(x=220, y=320)
        self.lbl5.place(x=100, y=370)
        self.t5.place(x=220, y=370)

    def add(self):
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')
        self.t5.delete(0, 'end')
        username = str(self.t1.get())
        try:
            result = pbsc.pbsc(username)
            self.t3.insert(END, str(result[1]))
            self.t4.insert(END, str(result[2]))
            self.t5.insert(END, str(result[3]))
            self.textSC.set("Berikut hasil kepribadian mu "+username)
            self.textER.set("")
        except:
            self.textER.set(
                username+" tidak berhasil di crawl \n pastikan username sudah benar dan akun tidak di privete \n atau periksa koneksi internet anda")


window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("420x500+10+10")
window.mainloop()
