from tkinter import Tk, ttk
from tkinter import *

from PIL import Image, ImageTk

import requests
import json

cor0 = "#FFFFFF"
cor1 = "#333333"
cor2 = "#5192eb"

window = Tk()
window.geometry('320x390')
window.title('Currency Converter')
window.configure(bg=cor0)
window.resizable(height=False, width=False)

top = Frame(window, width=400, height=80, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=400, height=300, bg=cor0)
main.grid(row=1, column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    if currency_2 == 'INR':
        symbol = 'Rs.'
    elif currency_2 == 'USD':  
        symbol = '$'
    elif currency_2 == 'EUR':  
        symbol = 'CE'
    elif currency_2 == 'BRL':  
        symbol = 'R$'
    elif currency_2 == 'CAD':  
        symbol = 'CA $'            


    headers = {
        "X-RapidAPI-Key": "d94574bd04msh62a7e6c5ec691b8p10dd15jsnba6c91dfe50b",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol  + "{:,.2f}".format(converted_amount)
    
    result['text'] = formatted

    print(formatted)


icon = Image.open('images/icon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image = icon, compound=LEFT, text = "Currency converter", height=5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_name.place(x=0, y=0)

result = Label(main, text = " ", width=16, height=3, pady=7,relief="solid", anchor=CENTER, font=('Ivy 16 bold'), bg=cor0, fg=cor1)
result.place(x=50, y=10)

currency = ['INR', 'CAD', 'BRL', 'EUR', 'USD']

from_label = Label(main, text = "From ", width=8, height=1, padx=0, pady=7,relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
from_label.place(x=48, y=110)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=50, y=145)

to_label = Label(main, text = "To ", width=8, height=1, padx=0, pady=7,relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
to_label.place(x=170, y=110)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=170, y=145)

value = Entry(main, width=23, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=51,y=200)

button = Button(main, text="Convert", width=19, padx=5, height=1, bg=cor2, fg=cor0, font=("Ivy 12 bold"), command=convert)
button.place(x=50, y=260)



window.mainloop()