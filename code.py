from tkinter import *
from tkinter import messagebox
import requests

tk = Tk()
tk.title('Headlines')
tk.geometry('500x500')

def getcountrycode():
    cname = countryname.get().lower()
    response = requests.get('https://api.printful.com/countries')
    data = response.json()
    results = data['result']
    countrycode = ''
    for f in results:
        if(f['name'].lower() == cname):
            countrycode = f['code'].lower()
    if(countrycode == ''):
        messagebox.showerror(
            'error', 'The country does not exist {}'.format(cname))
    else:
        getheadlines(countrycode)

countryname = StringVar()
countryenter = Entry(tk, textvariable=countryname,
                     font=('bold', 15)).place(x=200, y=40)
enterlabel = Label(tk, text='Enter country name',
                   font=('bold', 15)).place(x=200, y=10)
searchbutton = Button(tk, text='search', width=12,
                      command=getcountrycode).place(x=200, y=70)
title = Label(tk, text='', font=('bold', 15))
title.place(x=100,y=100)




def getheadlines(c):
    
    link = 'https://newsapi.org/v2/top-headlines?country='+c+'&apiKey=3ed8c02dfc00453fa5ec3d4960e8dfeb'
    response = requests.get(link)
    data = response.json()
    results = data['articles']
    print(results)
    titles = ''
    count = 1
    if(len(results) == 0):
        titles = 'No new news to display'
    else:
        for f in results:
            titles = titles+str(count)+'. '+f['title']+'\n'
            count = count+1
        
    title.config(text = titles)

tk.mainloop()
