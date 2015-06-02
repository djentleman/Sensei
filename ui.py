# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *
import sensei
import romkan


class Example(Frame):
  
    def __init__(self, parent, lbound, ubound, count):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.count = count # number of flashcards
        self.lbound = lbound # lower bound on word length
        self.ubound = ubound # upper bound on word length
        self.score = 0
        self.word = ""
        self.curr = 0
        self.initUI()

    def callback(self, event):
        self.submit()
        
    def initUI(self):
      
        self.parent.title("せんせい")

        self.pack(fill=BOTH, expand=1)

        submit = Button(self, text="Submit",
            command=self.submit)
        submit.place(x=420, y=260)

        self.kana = StringVar()
        Label(self, font=("Helvetica", 40), textvariable=self.kana).place(x=30, y=50)

        self.e = StringVar()
        Label(self, font=("Helvetica", 20), textvariable=self.e).place(x=50, y=130)
        self.e.set("Romanji:")

        self.response = StringVar()
        self.lblres = Label(self, font=("Helvetica", 20), textvariable=self.response)
        self.lblres.place(x=50, y=200)

        self.input = StringVar()
        entry = Entry(self, font=("Helvetica", 20), textvariable=self.input)
        entry.place(x=170, y=130)
        entry.bind("<Return>", self.callback)

        self.round = StringVar()
        Label(self, font=("Helvetica", 16), textvariable=self.round).place(x=400, y=10)

        
        
        
        self.init()

    

    def init(self):
        self.word = sensei.generateWord(self.lbound, self.ubound)
        self.kana.set(romkan.to_hiragana(self.word))
        self.round.set(str(self.score)+"/"+str(self.count)+" ("+str(self.curr)+")")

    def submit(self):

        
        uromanji = self.input.get()
        if (uromanji == self.word):
            self.score += 1
            self.response.set("Correct!  ["+romkan.to_hiragana(self.word)+"] "+self.word)
            self.lblres.config(background="green")
        else:
            self.response.set("Incorrect!  ["+romkan.to_hiragana(self.word)+"] "+self.word)
            self.lblres.config(background="red")
        sensei.tts(romkan.to_hiragana(self.word))
        self.input.set("")
        self.word = sensei.generateWord(self.lbound, self.ubound)
        self.kana.set(romkan.to_hiragana(self.word))
        self.curr += 1
        self.round.set(str(self.score)+"/"+str(self.count)+" ("+str(self.curr)+")")

        if self.curr >= self.count:
            print str(self.score)+"/"+str(self.count)+" ("+str(self.curr)+")"
            self.parent.destroy()
        
            
        


def main():
  
    root = Tk()
    root.geometry("500x300+300+300")
    app = Example(root, 1, 1, 50)
    root.mainloop()  


if __name__ == '__main__':
    main()  
