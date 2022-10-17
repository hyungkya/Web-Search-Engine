from tkinter import *
from tkinter import messagebox
import search

wd = Tk()
wd.title('TEAM KAKAO')
wd.geometry("500x400")

origin = StringVar()  # Holds a string; default value ""


def calculate():
    ret = []


    query = origin.get()
    if query.strip() == "":
        messagebox.showwarning(title="Invalid Query", message="Please input valid queries")
        return

    se = search.SearchEngine() 
    se.loadIndexingData()

    se.processQuery(query)

    for docID in se.champion[:10]:
       ret.append(se.urlMap[docID])
       print(se.urlMap[docID])

    result_str = ''
    for i, url in enumerate(ret):
        result_str += (f'{i+1}.' + url + '\n')
        
    if result_str != '':
        messagebox.showinfo('RESULT', result_str)
    else:
        messagebox.showwarning(title="No match", message="No matches found for your query.")
        return

def exit(event):
    wd.destroy()


if __name__ == "__main__":
    # create widget
    lb0 = Label(wd, text='Team KAKAO')
    lbx = Label(wd, text='MILESTONE 3')
    lb1 = Label(wd, text=" INPUT_QUERY      : ")

    text1 = Entry(wd, textvariable=origin, width=50)
    btn = Button(wd, text="Show the result",
                 command=calculate)  # binding mouse click to the function

    # grid-type widget specification
    lb0.grid(row=0, column=1)
    lbx.grid(row=1, column=1)
    lb1.grid(row=2, column=0)
    text1.grid(row=2, column=1)
    btn.grid(row=3, column=1)
    wd.bind('<Escape>', exit)  # binding 'esc' button to exit method
    
    wd.mainloop()
