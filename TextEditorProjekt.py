from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox


#main window
root = Tk(className=' My Text Editor')

#text rutan man kan skriva i
textArea=scrolledtext.ScrolledText(root, width=100,height=80)

#funktioner som vi binder till command i menu parenteserna.



#newFile - frågar om användaren vill spara det som är skrivet i text editorn och raderar sedan all text för att skapa en "ny" blank sida.
def newFile():
    if len(textArea.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno("save?","do you wish to save?"):
            saveFile()
        else:
            textArea.delete('1.0',END)
    root.title("TEXT EDITOR")


#openFile - tar filedialog modulen och frågar användaren vilken fil den vill öppna.
def openFile():
    textArea.delete('1.0', END)
    file =filedialog.askopenfile(parent=root,mode='rb',title='select a text file',)

    if file != None:
        contents =file.read()
        textArea.insert('1.0', contents)
        file.close()

#saveFile - samma som ovan, tar filedialog och asksaveasfile i w mode för att fråga användaren vad den vill döpa filen till och var filen ska sparas.
def saveFile():
    file = filedialog.asksaveasfile(mode='w')

    if file != None:
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()
#enkel messagebox funktion.
def about():
    label = messagebox.showinfo('About','A simple text editor made with Python by Tobias Grönberg, student at Nackademin.')


#en exit funktion
def exit():
    if messagebox.askyesno("Quit","are you sure you want to quit?"):
        root.destroy()

#meny rader
menu=Menu(root)
root.config(menu=menu)

#första menyn och de under-menyer.
fileMenu=Menu(menu)
menu.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='New',command=newFile)
fileMenu.add_command(label='Open',command=openFile)
fileMenu.add_command(label='Save',command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=exit)


#andra menyn
helpMenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpMenu)
helpMenu.add_command(label='Help')
helpMenu.add_command(label='About',command=about)


textArea.pack()
root.mainloop()