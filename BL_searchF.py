#Negin Parsa
from tkinter import *
import os
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import re
            
                           
            
def open_file(lbox_folder):
    os.startfile(lbox_folder.get(lbox_folder.curselection()[0]))

def alltype(file_name,link_of_folder,lbox_folder,subfolderget,nameoptionget,type_get):
    #MATCH CASE -->  (nameoption==2)
            if nameoptionget==2:
                if subfolderget==1:   
                    lbox_folder.delete(0, END)
                    filelist = []
                    for r, d, f in os.walk(link_of_folder):
                        for file in f:
                            if file_name in file:
                                filelist.append(r + "\\" + file)
                    if not filelist:
                        messagebox.showerror("ERROR!!","file Not found")       
                    for f in filelist:
                        lbox_folder.insert(0, f)
                elif subfolderget==0:
                    lbox_folder.delete(0, END)
                    filelist = []
                    for file in os.listdir(link_of_folder):
                        if file_name in file:
                            path = os.path.join(link_of_folder, file)
                            if os.path.isdir(path):
                                filelist.append(path)
                    if not filelist:
                        messagebox.showerror("ERROR!!","file Not found")       
                    for d in filelist:
                        lbox_folder.insert(0, d)
                #MACH WHOLE WORD -->  (nameoption==3)
            if nameoptionget==3:
                if subfolderget==1:   
                    lbox_folder.delete(0, END)
                    filelist = []
                    for r, d, f in os.walk(link_of_folder):
                        for file in f:
                            list_file = file.rsplit(".")
                            if file_name== list_file[0]:
                                filelist.append(r + "\\" + file)
                    if not filelist:
                        messagebox.showerror("ERROR!!","file Not found")       
                    for f in filelist:
                        lbox_folder.insert(0, f)
                elif subfolderget==0:
                    lbox_folder.delete(0, END)
                    filelist = []
                    for file in os.listdir(link_of_folder):
                        if file_name==file:
                            path = os.path.join(link_of_folder, file)
                            if os.path.isdir(path):
                                filelist.append(path)
                    if not filelist:
                        messagebox.showerror("ERROR!!","file Not found")       
                    for d in filelist:
                        lbox_folder.insert(0, d)
            
def anothertype (file_name,link_of_folder,lbox_folder,subfolderget,nameoptionget,type_get):

    
    #MATCH CASE -->  (nameoption==2)
            if nameoptionget==2:
                if subfolderget==1:   
                    lbox_folder.delete(0, END)
                    filelist = []
                    for r, d, f in os.walk(link_of_folder):
                        for file in f:
                            if file_name in file and  file.endswith(type_get) :
                                filelist.append(r + "\\" + file)
                    if not filelist:
                        messagebox.showerror("ERROR!!","file Not found")       
                    for f in filelist:
                        lbox_folder.insert(0, f)
                elif subfolderget==0:
                    lbox_folder.delete(0, END)
                    filelist = []
                    for file in os.listdir(link_of_folder):
                        if file_name in file and  file.endswith(type_get) :
                            path = os.path.join(link_of_folder, file)
                            if os.path.isdir(path):
                                filelist.append(path)
                    if not filelist:
                        messagebox.showerror("ERROR!!","file Not found")       
                    for d in filelist:
                        lbox_folder.insert(0, d)
    #MACH WHOLE WORD -->  (nameoption==3)
            if nameoptionget==3:
                if subfolderget==1:   
                    lbox_folder.delete(0, END)
                    filelist = []
                    for r, d, f in os.walk(link_of_folder):
                        for file in f  :
                            list_file = file.rsplit(".")
                            if file_name== list_file[0] and file.endswith(type_get) :
                                filelist.append(r + "\\" + file)
                    if not filelist:
                        messagebox.showerror("ERROR!!","file Not found")       
                    for f in filelist:
                        lbox_folder.insert(0, f)
                elif subfolderget==0:
                    lbox_folder.delete(0, END)
                    filelist = []
                    for file in os.listdir(link_of_folder):
                        if file_name==file and  file.endswith(type_get) :
                            path = os.path.join(link_of_folder, file)
                            if os.path.isdir(path):
                                filelist.append(path)
                    if not filelist:
                        messagebox.showerror("ERROR!!","file Not found")       
                    for d in filelist:
                        lbox_folder.insert(0, d)

