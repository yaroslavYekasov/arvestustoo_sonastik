from tkinter import *

def trans():
    wor = ent.get()
    alphabet_eest = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "š", "z", "ž", "t", "u", "v", "w", "õ", "ä", "ö", "ü", "x", "y"]
    ka=bool(set(alphabet_eest).intersection(set(wor.lower())))
    if ka == True:
        for i in range(len(eest_words)):          
            if eest_words[i].lower() == wor.lower():
                result=eng_words[i]
                lbl.config(text = result)
                break
            else:
                lbl.config(text = "see sõna ei ole\nveel sõnastik")

def add():
    def save():
        new_word = ent_ex.get()

        eest_words.append(wor)
        f = open('eest.txt','a',encoding="utf-8-sig") 
        f.write(wor + '\n')
        f.close()

        eng_words.append(new_word)
        f = open('eng.txt','a',encoding="utf-8-sig") 
        f.write(new_word + '\n')
        f.close()

        print(eest_words, eng_words)

        aken.destroy()

    wor = ent.get()

    aken=Tk()
    aken.title('Säilitada')
    aken.iconbitmap("save.ico")
    aken.geometry("300x150")
    aken['bg'] = 'white'
    label_nickname= Label(aken, text=wor,bg="crimson",fg="white",font="Arial 15",height=2,width=40)
    label_nickname.pack()

    ent_ex = Entry(aken, font="Arial 20", fg="crimson", width=10)
    ent_ex.pack()

    btn_ex = Button(aken, text="säilitada", fg="crimson", bg='white', font="Arial 15", relief=GROOVE, width=7, command=save)
    btn_ex.pack()

#####################################################################eng_defs

def trans_eng():
    wor = ent.get()
    alphabet_eng = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ka=bool(set(alphabet_eng).intersection(set(wor.lower())))
    if ka == True:
        for i in range(len(eng_words)):          
            if eng_words[i].lower() == wor.lower():
                result=eest_words[i]
                lbl.config(text = result)
                break
            else:
                lbl.config(text = "this word is not\nin dictionary yet")

def add_eng():
    def save_eng():
        new_word = ent_ex.get()

        eng_words.append(wor)
        f = open('eng.txt','a',encoding="utf-8-sig") 
        f.write(wor + '\n')
        f.close()

        eest_words.append(new_word)
        f = open('eest.txt','a',encoding="utf-8-sig") 
        f.write(new_word + '\n')
        f.close()

        print(eest_words, eng_words)

        aken.destroy()

    wor = ent.get()

    aken=Tk()
    aken.title('Säilitada')
    aken.iconbitmap("save.ico")
    aken.geometry("300x150")
    aken['bg'] = 'white'
    label_nickname= Label(aken, text=wor,bg="crimson",fg="white",font="Arial 15",height=2,width=40)
    label_nickname.pack()

    ent_ex = Entry(aken, font="Arial 20", fg="crimson", width=10)
    ent_ex.pack()

    btn_ex = Button(aken, text="save", fg="crimson", bg='white', font="Arial 15", relief=GROOVE, width=7, command=save_eng)
    btn_ex.pack()

#####################################################################eng_defs

def change_lang():
    selection = int(str(var.get()))
    if selection==1:
        txt.config(text = "tõlkimine")
        btn.config(text = "T")
        btn_add.config(text = "lisada sõna")
        btn.config(command = trans)
        btn_add.config(command = add)      
    elif selection==2:
        txt.config(text = "translation")
        btn.config(text = "T")
        btn_add.config(text = "add word")
        btn.config(command = trans_eng)
        btn_add.config(command = add_eng)  

def black():
    them = int(str(var.get()))
    if them==3:
         
         slate.config(bg = "white")
         rdb.config(bg = "white")
         rdb1.config(bg = "white")
         txt.config(bg= "white")
         txt_inv.config(bg= "white")
         btn_add.config(fg= "white")
         btn.config(bg ="white", fg ="crimson")
         ent.config(fg ="white")
         lbl.config(fg ="white")
    elif them==4:
        
        slate.config(bg = "#2E2E2E")
        rdb.config(bg = "#2E2E2E")
        rdb1.config(bg = "#2E2E2E")
        txt.config(bg= "#2E2E2E")
        txt_inv.config(bg= "#2E2E2E")
        btn_add.config(fg= "#2E2E2E")
        btn.config(bg ="#2E2E2E", fg ="crimson")
        ent.config(fg ="#2E2E2E")
        lbl.config(fg ="#2E2E2E")

f=open('eest.txt','r',encoding="utf-8-sig")
eest_words=[]
for rida in f:
    eest_words.append(rida.strip())
f.close()

f=open('eng.txt','r',encoding="utf-8-sig")
eng_words=[]
for rida in f:
    eng_words.append(rida.strip())
f.close()

print(eest_words, '\n', eng_words)
    
slate = Tk()

var = IntVar()

slate.title('Slate (Alpha)')
slate.iconbitmap("slate.ico")
slate['bg'] = 'white'
slate.geometry('400x600')
slate.resizable(width=False, height=False)

frm = Frame(slate, bg="crimson", height=750, width=50)
frm.pack(side=LEFT)

theme = Radiobutton(frm, text="", fg="crimson",bg="crimson", font="Arial 25",   variable=var, value=3, command = black)
theme.place(x=14,y=0)

theme1 = Radiobutton(frm, text="", fg="#2E2E2E",bg="crimson", font="Arial 25",  variable=var, value=4, command = black)
theme1.place(x=14,y=34)

rdb = Radiobutton(slate, text="Eesti keel",fg="crimson",bg="white", font="Arial 15",   variable=var, value=1, command=change_lang)
rdb.pack(anchor='w')

rdb1 = Radiobutton(slate, text="English language",fg="crimson",bg="white", font="Arial 15",  variable=var, value=2, command=change_lang)
rdb1.pack(anchor='w')

ent = Entry(slate, font="Arial 40", fg="white", bg="crimson", width=10, relief=FLAT, justify=CENTER)
ent.pack()

txt = Label(slate, text="tõlkimine", fg="crimson", bg="white", font="Arial 20")
txt.pack(anchor='w')

lbl = Label(slate, text="", bg="crimson", fg="white", font="Arial 25", height=6, width=15, justify=CENTER)
lbl.pack()

txt_inv = Label(slate, text="", fg="white", bg="white", font="Arial 20")
txt_inv.pack(anchor='w')

btn = Button(frm, text="T", bg="white", fg="crimson", font="Arial 20", relief=GROOVE, width=2, command=trans)
btn.place(x=3,y=520)

btn_add = Button(slate, text="lisada sõna", bg="crimson", fg="white", font="Arial 24", relief=GROOVE, width=8, command=add)
btn_add.pack()

slate.mainloop()






