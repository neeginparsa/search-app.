#Negin Parsa
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from BL_searchF import *
import os




def browseFiles():
    lbox_folder.delete(0, END)
    global file_adreesvar
    global file_namevar
    file_namevar.set("")
    link = filedialog.askdirectory()
    file_adreesvar.set(link)
    print(link)

def searchfiles(file_name,link_of_folder,lbox_folder,subfolderget,nameoptionget,type_get):
    err_list=[]
    if not file_name:
        err_list.append("invalid file name!!!")    
    if not link_of_folder:
        err_list.append("invalid link!!!") 
    if err_list:
        messagebox.showerror("ERROR!!", "\n".join(err_list))
    if not err_list:
        b_save["state"] = "normal"
        b_save.config(bg='#FCAA53',fg="black")
        if type_get== "All type":
            alltype(file_name,link_of_folder,lbox_folder,subfolderget,nameoptionget,type_get)
        else:
            anothertype(file_name,link_of_folder,lbox_folder,subfolderget,nameoptionget,type_get)
  
def save():
    selected = lbox_folder.curselection() 
    if not selected:
        messagebox.showinfo("Select!!","Select the desired links to save")
    if selected:
        try:
            file = asksaveasfile(defaultextension=".txt")
            for idx in selected:
                file.write("\n")
                file.write(lbox_folder.get(idx))
        except:
            return "error"
            

#region hover button
#CHOOSE
def on_enter_choose(e):
    b_choose['background'] = '#CE6A51'
def on_leave_choose(e):
    b_choose['background'] = '#FCAA53'
    
#SEARCH
def on_enter_search(e):
    b_search['background'] = '#CE6A51'
def on_leave_search(e):
    b_search['background'] = '#FCAA53'
#endregion


root = Tk()
root.title("search")
root.geometry("605x600")
root.resizable(width=0 , height=0)
root.configure(bg ="#524034")

#region BUTTON
b_choose = Button(root, text="choose",bg="#FCAA53", activebackground= "#FBE5A0",command= browseFiles )
b_choose.place(height=20, width=100, x=485,y=98)
b_choose.bind("<Enter>", on_enter_choose)
b_choose.bind("<Leave>", on_leave_choose)
b_search = Button(
                root, text="search" ,
                bg="#FCAA53",
                activebackground= "#FBE5A0" ,
                width=20,
                command= lambda : searchfiles(
                                                file_name= file_namevar.get(),
                                                link_of_folder= file_adreesvar.get(),
                                                lbox_folder= lbox_folder,
                                                subfolderget= var1.get(),
                                                nameoptionget = nameoption.get(),
                                                type_get = type_.get()
                                            )
                )
b_search.place(height=30, width=106, x=478,y=430)
b_search.bind("<Enter>", on_enter_search)
b_search.bind("<Leave>", on_leave_search)
b_save = Button(root, text = 'Save',bg="#FBE5A0",activebackground= "#FBE5A0", command = lambda : save())
b_save["state"] = "disabled"
b_save.place(height=30, width=106, x=478,y=470)
#endregion

#region ENTRY
file_adreesvar = StringVar()
ent_adress = Entry(root, textvariable= file_adreesvar,state=DISABLED,disabledbackground="white")
ent_adress.place(height=19, width=390, x=83,y=98)

file_namevar= StringVar()
ent_name = Entry(root, textvariable= file_namevar)
ent_name.place(height=19, width=501, x=83,y=130)

#endregion

#region LABLE
lbl_file_searchapp = Label(root, text="searching" )
lbl_file_searchapp.config(font=("Papyrus", 29))
lbl_file_searchapp.place(height=47, width=260, x=165,y=23)
lbl_file_searchapp.configure(bg= "#524034", fg="#FCAA53")
lbl_file_adress = Label(root, text="Look in :" )
lbl_file_adress.place(height=23, width=80, x=4,y=94)
lbl_file_adress.configure(bg= "#524034", fg="#FCAA53")
lbl_file_name = Label(root, text="Find what :" )
lbl_file_name.place(height=25, width=68, x=10,y=126)
lbl_file_name.configure(bg= "#524034", fg="#FCAA53")
lbl_name_option = Label(root, text="option :" )
lbl_name_option.place(height=80, width=40, x=25,y=170)
lbl_name_option.configure(bg= "#524034", fg="#FCAA53")
lbl_type = Label(root, text="Type :" )
lbl_type.place(height=80, width=40, x=22,y=270)
lbl_type.configure(bg= "#524034", fg="#FCAA53")
#endregion

#region checkbox
var1 = tk.IntVar()
chksub = tk.Checkbutton(root, text='include sub-folder',onvalue=1, offvalue=0, variable=var1) 
chksub.configure(bg= "#524034",fg="#FCAA53",selectcolor="#524034")
chksub.place(height=35, width=130, x=77,y=150)
#endregion

#region Radiobutton
nameoption =tk.IntVar(root,2)
tk.Radiobutton(root, 
               text="Match case",
               padx = 20, 
               variable=nameoption, 
               value=2,background='#524034',fg="#FCAA53",selectcolor="#524034").place(x=75,y=215)

tk.Radiobutton(root, 
               text="Match whole word",
               padx = 20, 
               variable=nameoption, 
               value=3,background='#524034',fg="#FCAA53",selectcolor="#524034").place(x=75,y=245)
#endregion

#region Combobox
type_ = tk.StringVar()
type_.set("All type")
typechoosen = ttk.Combobox(root, width = 27,textvariable =type_)
typechoosen['values'] = ('All type',
                          '.txt', 
                          '.png',
                          '.jpg',
                          '.pdf',
                          '.mp3',
                           '.mp4')
  
typechoosen.place(height=20, width=500, x=80,y=300)
#endregion

#region LISTBOX
scr = Scrollbar(root)
scr.place(height=200, width=18, x=440,y=377)
lbox_folder = Listbox(root,selectmode=MULTIPLE,yscrollcommand= scr.set)
lbox_folder.place(height=200, width=415, x=27,y=377)
lbox_folder.bind("<Double-Button>", lambda x: open_file(lbox_folder=lbox_folder))
scr.config(command=lbox_folder.yview)
scr.configure(bg= "#F0F4F8")
lbox_folder.configure(bg= "#FBE5A0")
#endregion

#region MENU
def show_rule_frame():
    show_rule = Tk()
    show_rule.geometry("440x440")
    show_rule.config(bg="#FBE5A0")
    show_rule.title("About")
    text = Label(show_rule,text=" About")
    text.config(font =("Papyrus", 15),bg="#FBE5A0")
    text.place(x=180,y=6)
    text_rule = Label(show_rule,text="""Before searching, the save button is disabled,
         and after the first search by clicking on
          an unlimited number of desired links,
        it can be saved on your computer.
    """ )
    tnx_lbl = Label(show_rule,text="""    thank you for your attention 
    Negin Parsa""")
    tnx_lbl.place(x=110,y=300,width=200,height=50)
    tnx_lbl.config(bg="#FBE5A0")
    text_rule.config(font =("Papyrus", 14),bg="#FBE5A0")
    text_rule.place(x=12,y=35,width=414,height=200)
    bt_ok_g = Button(show_rule, text = "OK", command = show_rule.destroy)
    bt_ok_g.config(bg="#FCAA53")
    bt_ok_g.place(x=190,y=370,width=50,height=35)
    show_rule.mainloop() 
menubar = Menu(root, background="#FBE5A0", foreground='black')
filemenu = Menu(menubar, tearoff=0, background="#FBE5A0",foreground='black')
filemenu.add_command(label="about program", command=show_rule_frame)
menubar.add_cascade(label="About", menu=filemenu)
menubar.add_command(label="Exit", command=root.destroy)  
root.config( menu=menubar)
#endregion

root.mainloop()