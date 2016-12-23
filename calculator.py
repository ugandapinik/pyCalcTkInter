from tkinter import *

calculator = Tk()
calculator.title("Calculator")
# calculator.resizable(0,0)

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        #create widgets
        self.createWidgets()


    def calculateExpression(self):
        
        self.expression = self.display.get()
        self.expression = self.expression.replace("%", "/100")
        
        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            self.replaceText("Invalid")


    
    #replace text 
    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    #append value to display
    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if(self.entryText == "0"):
            self.replaceText(text)
        
        else:
            self.display.insert(self.textLength, text)
    

    def clearText(self):
        self.replaceText("0")

    '''
    sticky
    ------------------
    NW = north west
    NE = north east
    SW = south west
    SE = south east
    '''

    #create all the widgets
    def createWidgets(self):
        #calculator display
        self.display = Entry(self, font = ("Helvetica", 16), relief="raised", justify="right", borderwidth=0)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)


        #----------------------1st ROW------------------------------#
        #insert seven Button
        self.sevenButton = Button(self, font=("Helvetica", 11), text="7", borderwidth=0, command=lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE")

        #insert eight = 8 Button
        self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=0, command=lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=1, column=1, sticky="NWNESWSE")

        #insert nine = 9 Button
        self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=0, command=lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=1, column=2, sticky="NWNESWSE")

        #insert seven = + Button
        self.multiplyButton = Button(self, font=("Helvetica", 11), text="*", borderwidth=0, command=lambda: self.appendToDisplay("*"))
        self.multiplyButton.grid(row=1, column=3, sticky="NWNESWSE")

        #insert seven Button
        self.clearButton = Button(self, font=("Helvetica", 11), text="C", borderwidth=0, command=lambda: self.clearText())
        self.clearButton.grid(row=1, column=4, sticky="NWNESWSE")
        #----------------------1st ROW------------------------------#


        #----------------------2ND ROW------------------------------#
        #insert four = 4 Button
        self.fourButton = Button(self, font=("Helvetica", 11), text="4", borderwidth=0, command=lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=2, column=0, sticky="NWNESWSE")

        #insert five = 5 Button
        self.fiveButton = Button(self, font=("Helvetica", 11), text="5", borderwidth=0, command=lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=2, column=1, sticky="NWNESWSE")

        #insert six = 6 Button
        self.sixButton = Button(self, font=("Helvetica", 11), text="6", borderwidth=0, command=lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=2, column=2, sticky="NWNESWSE")

        #insert divideButton = / Button
        self.divideButton = Button(self, font=("Helvetica", 11), text="/", borderwidth=0, command=lambda: self.appendToDisplay("/"))
        self.divideButton.grid(row=2, column=3, sticky="NWNESWSE")

        #insert percentage Button
        self.percentageButton = Button(self, font=("Helvetica", 11), text="%", borderwidth=0, command=lambda: self.appendToDisplay("%"))
        self.percentageButton.grid(row=2, column=4, sticky="NWNESWSE")
        #----------------------2ND ROW------------------------------#


        
        #----------------------3RD ROW------------------------------#
        #insert one = 1 Button
        self.oneButton = Button(self, font=("Helvetica", 11), text="1", borderwidth=0, command=lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=3, column=0, sticky="NWNESWSE")

        #insert two = 2 Button
        self.twoButton = Button(self, font=("Helvetica", 11), text="2", borderwidth=0, command=lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=3, column=1, sticky="NWNESWSE")

        #insert three = 3 Button
        self.threeButton = Button(self, font=("Helvetica", 11), text="3", borderwidth=0, command=lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=3, column=2, sticky="NWNESWSE")

        #insert seven = + Button
        self.minusButton = Button(self, font=("Helvetica", 11), text="-", borderwidth=0, command=lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=3, column=3, sticky="NWNESWSE")

        #insert seven Button
        self.equalButton = Button(self, font=("Helvetica", 11), text="=", borderwidth=0, command=lambda: self.calculateExpression())
        self.equalButton.grid(row=3, column=4, sticky="NWNESWSE", rowspan=2)
        #----------------------3RD ROW------------------------------#

        
        #----------------------4TH ROW------------------------------#
        #insert zero = 0 Button
        self.zeroButton = Button(self, font=("Helvetica", 11), text="0", borderwidth=0, command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4, column=0, sticky="NWNESWSE", columnspan=2)

        #insert point = . Button
        self.pointButton = Button(self, font=("Helvetica", 11), text=".", borderwidth=0, command=lambda: self.appendToDisplay("."))
        self.pointButton.grid(row=4, column=2, sticky="NWNESWSE")

        #insert plusButton = + Button
        self.plusButton = Button(self, font=("Helvetica", 11), text="+", borderwidth=0, command=lambda: self.appendToDisplay("+"))
        self.plusButton.grid(row=4, column=3, sticky="NWNESWSE")

        #----------------------4TH ROW------------------------------#

app = Application(calculator).grid()

#display calculator
calculator.mainloop()