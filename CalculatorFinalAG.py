from tkinter import *
import math
import requests
import json
import datetime


def myCalculator():

    root = Tk()
    root.title("My Calculator")

    root.configure(bg='gray21')


    # define global variables
    global firstNum
    global operator

    # create a text box for calculator inputs and API/number fact display
    e = Entry(root, width=35, borderwidth=10)
    e.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

    f = Entry(root, width=70, borderwidth=8)
    f.grid(row=7, column=0, columnspan=4, padx=10, pady=15)

    p = Entry(root, width=70, borderwidth=8)
    p.grid(row=9, column=0, columnspan=4, padx=10, pady=15)

    factLabel = Label(root, text="Number Fact: ", bg='gray21')
    factLabel.grid(row=6, column=0)
    factLabel.config(font=("Courier", 12))

    primeLabel = Label(root, text="Is it prime?", bg='gray21')
    primeLabel.grid(row=8, column=0)
    primeLabel.config(font=("Courier", 12))

    # define methods used in other places


    def getFact(result):

        api = f"http://numbersapi.com/{result}/math"
        data = requests.get(api)
        f.insert(0, data.text)


    def checkInt(x):

        test = True
        counter = 0
        for chars in x:
            if chars == '.':
                xmod = x[counter:]
                if xmod[1:4] == '000' or xmod[1:4] == '0' or xmod[1:4] == '00':
                    intx = x[:counter]
                    e.delete(0, END)
                    e.insert(0, intx)
                else:
                    test = False
            else:
                counter += 1
        return test


    def checkPrime(num):

        currentdate = datetime.date.today()
        currentdateStr = str(currentdate)
        fileextension = ".txt"
        filename = currentdateStr + fileextension

        num = int(num)

        test = True
        for i in range(2, num):
            if (num % i) == 0:
                test = False
                break

        notPrime = f"{num} is not a prime number."
        prime = f"{num} is a prime number."

        if test:
            p.insert(0, prime)
            return True

        else:
            p.insert(0, notPrime)
            return False

    # define methods/commands for the buttons


    def clearButton():
        e.delete(0, END)
        f.delete(0, END)
        p.delete(0, END)
        global firstNum
        firstNum = None


    def clickButton(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))


    def decimalButton():
        current = e.get()
        if current.find(".") == -1:
            e.delete(0, END)
            e.insert(0, current + ".")


    def addButton():
        first = e.get()
        global firstNum
        global operator
        operator = "add"
        if checkInt(first):
            firstNum = int(first)
        else:
            firstNum = float(first)
        e.delete(0, END)


    def subButton():
        first = e.get()
        global firstNum
        global operator
        operator = "sub"
        if checkInt(first):
            firstNum = int(first)
        else:
            firstNum = float(first)
        e.delete(0, END)


    def mulButton():
        first = e.get()
        global firstNum
        global operator
        operator = "mult"
        if checkInt(first):
            firstNum = int(first)
        else:
            firstNum = float(first)
        e.delete(0, END)


    def divButton():
        first = e.get()
        global firstNum
        global operator
        operator = "div"
        if checkInt(first):
            firstNum = int(first)
        else:
            firstNum = float(first)
        e.delete(0, END)


    def expButton():
        first = e.get()
        global firstNum
        global operator
        operator = "exp"
        if checkInt(first):
            firstNum = int(first)
        else:
            firstNum = float(first)
        e.delete(0, END)


    def sqrtButton():
        first = e.get()
        global firstNum
        global operator
        operator = "sqrt"
        if checkInt(first):
            firstNum = int(first)
        else:
            firstNum = float(first)


    def equalButton():

        f.delete(0, END)
        p.delete(0, END)
        dec = "We cannot provide facts or primes for decimals, sorry."

        currentdate = datetime.date.today()
        currentdateStr = str(currentdate)
        fileextension = ".txt"
        filename = currentdateStr + fileextension

        if operator != "sqrt":

            secondNum = e.get()
            e.delete(0, END)

            if operator == "add":
                if checkInt(secondNum):
                    e.insert(0, firstNum + int(secondNum))
                else:
                    e.insert(0, firstNum + float(secondNum))
                result = e.get()
                file = open(filename, 'a')
                file.write(f"{firstNum} + {secondNum} = {e.get()} \t")
                if checkInt(result):
                    result = e.get()
                    getFact(result)
                    if checkPrime(result):
                        file = open(filename, 'a')
                        file.write(f"Is Prime \n")
                    else:
                        file = open(filename, 'a')
                        file.write(f"Is Not Prime \n")

                else:
                    f.insert(0, dec)
                    file = open(filename, 'a')
                    file.write(f"Can't Find Prime \n")

            if operator == "sub":
                if checkInt(secondNum):
                    e.insert(0, firstNum - int(secondNum))
                else:
                    e.insert(0, firstNum - float(secondNum))
                result = e.get()
                file = open(filename, 'a')
                file.write(f"{firstNum} - {secondNum} = {e.get()} \t")
                if checkInt(result):
                    result = e.get()
                    getFact(result)
                    if checkPrime(result):
                        file = open(filename, 'a')
                        file.write(f"Is Prime \n")
                    else:
                        file = open(filename, 'a')
                        file.write(f"Is Not Prime \n")

                else:
                    f.insert(0, dec)
                    file = open(filename, 'a')
                    file.write(f"Can't Find Prime \n")

            if operator == "mult":
                if checkInt(secondNum):
                    e.insert(0, firstNum * int(secondNum))
                else:
                    e.insert(0, firstNum * float(secondNum))
                result = e.get()
                file = open(filename, 'a')
                file.write(f"{firstNum} * {secondNum} = {e.get()} \t")
                if checkInt(result):
                    result = e.get()
                    getFact(result)
                    if checkPrime(result):
                        file = open(filename, 'a')
                        file.write(f"Is Prime \n")
                    else:
                        file = open(filename, 'a')
                        file.write(f"Is Not Prime \n")

                else:
                    f.insert(0, dec)
                    file = open(filename, 'a')
                    file.write(f"Can't Find Prime \n")

            if operator == "div":
                if checkInt(secondNum):
                    e.insert(0, firstNum / int(secondNum))
                else:
                    e.insert(0, firstNum / float(secondNum))
                result = e.get()
                file = open(filename, 'a')
                file.write(f"{firstNum} / {secondNum} = {e.get()} \t")
                if checkInt(result):
                    result = e.get()
                    getFact(result)
                    if checkPrime(result):
                        file = open(filename, 'a')
                        file.write(f"Is Prime \n")
                    else:
                        file = open(filename, 'a')
                        file.write(f"Is Not Prime \n")

                else:
                    f.insert(0, dec)
                    file = open(filename, 'a')
                    file.write(f"Can't Find Prime \n")

            if operator == "exp":
                if checkInt(secondNum):
                    e.insert(0, firstNum ** int(secondNum))
                else:
                    e.insert(0, firstNum ** float(secondNum))
                result = e.get()
                file = open(filename, 'a')
                file.write(f"{firstNum}^{secondNum} = {e.get()} \t")
                if checkInt(result):
                    result = e.get()
                    getFact(result)
                    if checkPrime(result):
                        file = open(filename, 'a')
                        file.write(f"Is Prime \n")
                    else:
                        file = open(filename, 'a')
                        file.write(f"Is Not Prime \n")

                else:
                    f.insert(0, dec)
                    file = open(filename, 'a')
                    file.write(f"Can't Find Prime \n")
        else:
            e.delete(0, END)
            e.insert(0, math.sqrt(firstNum))
            result = e.get()
            file = open(filename, 'a')
            file.write(f"Squareroot({firstNum}) = {e.get()} \t")
            if checkInt(result):
                result = e.get()
                getFact(result)
                if checkPrime(result):
                    file = open(filename, 'a')
                    file.write(f"Is Prime \n")
                else:
                    file = open(filename, 'a')
                    file.write(f"Is Not Prime \n")

            else:
                f.insert(0, dec)
                file = open(filename, 'a')
                file.write(f"Can't Find Prime \n")

    # Define each button's text and commands


    button1 = Button(root, text="1", bg="grey", padx=65,
                    pady=20, command=lambda: clickButton(1))
    button2 = Button(root, text="2", bg="grey", padx=70,
                    pady=20, command=lambda: clickButton(2))
    button3 = Button(root, text="3", bg="grey", padx=50,
                    pady=20, command=lambda: clickButton(3))
    button4 = Button(root, text="4", bg="grey", padx=65,
                    pady=20, command=lambda: clickButton(4))
    button5 = Button(root, text="5", bg="grey", padx=70,
                    pady=20, command=lambda: clickButton(5))
    button6 = Button(root, text="6", bg="grey", padx=50,
                    pady=20, command=lambda: clickButton(6))
    button7 = Button(root, text="7", bg="grey", padx=65,
                    pady=20, command=lambda: clickButton(7))
    button8 = Button(root, text="8", bg="grey", padx=70,
                    pady=20, command=lambda: clickButton(8))
    button9 = Button(root, text="9", bg="grey", padx=50,
                    pady=20, command=lambda: clickButton(9))
    button0 = Button(root, text="0", bg="grey", padx=70,
                    pady=20, command=lambda: clickButton(0))
    buttonClr = Button(root, text="C", bg="grey", padx=65,
                    pady=20, command=lambda: clearButton())
    buttonAdd = Button(root, text="+", bg="grey", padx=50,
                    pady=20, command=lambda: addButton())
    buttonSub = Button(root, text="-", bg="grey", padx=50,
                    pady=20, command=lambda: subButton())
    buttonMul = Button(root, text="x", bg="grey", padx=50,
                    pady=20, command=lambda: mulButton())
    buttonDiv = Button(root, text="/", bg="grey", padx=50,
                    pady=20, command=lambda: divButton())
    buttonEq = Button(root, text="=", bg="grey", padx=50,
                    pady=20, command=lambda: equalButton())
    buttonExp = Button(root, text="x^", bg="grey", padx=46,
                    pady=20, command=lambda: expButton())
    buttonSqrt = Button(root, text="√x", bg="grey", padx=65,
                        pady=20, command=lambda: sqrtButton())
    buttonDec = Button(root, text=".", bg="grey", padx=52,
                    pady=20, command=lambda: decimalButton())

    # Placing buttons on Screen, organized by rows
    buttonSqrt.grid(row=1, column=1)
    buttonExp.grid(row=1, column=2)
    buttonAdd.grid(row=1, column=3)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    buttonSub.grid(row=2, column=3)

    button4.grid(row=3, column=0)
    button5.grid(row=3, column=1)
    button6.grid(row=3, column=2)
    buttonMul.grid(row=3, column=3)

    button1.grid(row=4, column=0)
    button2.grid(row=4, column=1)
    button3.grid(row=4, column=2)
    buttonDiv.grid(row=4, column=3)

    buttonClr.grid(row=5, column=0)
    button0.grid(row=5, column=1)
    buttonDec.grid(row=5, column=2)
    buttonEq.grid(row=5, column=3)

    root.mainloop()

myCalculator()