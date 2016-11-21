from tkinter import *

class MyDialog:
    def __init__(self, parent):
        top = self.top = parent
        Label(top, text=" Enter your real mail Password ").pack(pady=25)
        self.e = Entry(top,show="*")
        self.e.pack(padx=5)
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=25)
    def ok(self):
        self.passw=self.e.get()
        self.top.destroy()
       
root = Tk()
root.geometry('200x200+300+300')
root.title('Enter real password')
inputDialog = MyDialog(root)
root.wait_window(inputDialog.top)
entryPassword=inputDialog.passw
root.mainloop()

