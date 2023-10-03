from tkinter import *
import subprocess
import os
import shutil
def file_manage(): #ye file_manage function hai
    f=open("path.txt","r+") #PATH KO OPEN KIA READ WRITE MODE ME (r+)
    get_path=f.read().rstrip() #read kia path rigth space hta die or get path me dal dia
    f.close() #file close kr di, qki path le chuke hai get path me
    pdf_files=[] #empty list bnai pdf, text, images ke lie
    text_files=[]
    images=[]
    miscs=[]
    others=[]
    managing_path=get_path #managing path me b copy kr lia get path
    f=open("output.txt","a+") #output file open ki ye ek log file hai jisme program ka flow milega poora kon si file move hui khi problem to ni aai.
    #(a+ ka mtlb ye file append+read mode me open hogi age esi koi file ni hogi to apne aap ban jaygi)
    
    for files in os.listdir(managing_path): #listdir method in python is used to get all files and directories in the specified folder
        if not(os.path.isdir(managing_path+"\\"+files)): #os module ka method hai path.isdir() ye check krne ke lie ki specified path directory hai ya ni hai
                                                          # humko files chaie directory ni chaie islie ye false hina chaie, islie upr if not() likha hai
            if files.endswith('.pdf'):
                pdf_files.append(files) #loop ke andar aa gye, ye to pkka hai ki file hai, ab agr pdf file hai to pdf wali list me append kar denge
                                
            elif files.endswith('.jpg') or files.endswith('.png'):
                images.append(files) # jpg hai mtlb pics hai to jpg me append kar denge
            elif files.endswith('.txt') or files.endswith('.html') or files.endswith('.c') or files.endswith('.py') or files.endswith('.docx'):
                text_files.append(files) # txt hai to txt me append kar denge
            elif files.endswith('.mp4') or files.endswith('.mkv') or files.endswith('.mp3'):
                miscs.append(files) # mp4, mkv ,mp3 hai to isme
            else:
                others.append(files) # koi ni to others me append kr denge
    path_folders=[os.path.join(managing_path,"pdf_files"),os.path.join(managing_path,"text_files"),os.path.join(managing_path,"images"),os.path.join(managing_path,"miscs"),os.path.join(managing_path,"others")]
    #os.path.join() method in Python join one or more path components intelligently. This method concatenates various path components with exactly one directory separator
    #sare components jud kr path_folders me aagye
    for i in path_folders:
        os.makedirs(i) # har ek ko ek seperate directory/folder bna dia
    current_location=managing_path #managing_path ko current_location me dal lia
    for i in pdf_files:
        source=current_location+'\\'+i #source path select kia
        destination=os.path.join(managing_path,"pdf_files") #destination ko select kia
        shutil.move(source,destination) #shutil module ke move function ki help se source files ko destination me move kr dia, 
        t="MOVED- "+i+"\n" #ye display ke lie use kia h, jb move hogi files to output hoga display
        f.write(t) #f(log file hai ye) isme write kr dia ki move ho gai file
    for i in text_files: #same iske lie bhi
        source=current_location+'\\'+i
        destination=os.path.join(managing_path,"text_files")
        shutil.move(source,destination)
        t="MOVED- "+i+"\n"
        f.write(t)
    for i in images: #same
        source=current_location+'\\'+i
        destination=os.path.join(managing_path,"images")
        shutil.move(source,destination)
        t="MOVED- "+i+"\n"
        f.write(t)
    for i in miscs: #same
        source=current_location+'\\'+i
        destination=os.path.join(managing_path,"miscs")
        shutil.move(source,destination)
        t="MOVED- "+i+"\n"
        f.write(t)
    for i in others: #same
        source=current_location+'\\'+i
        destination=os.path.join(managing_path,"others")
        shutil.move(source,destination)
        t="MOVED- "+i+"\n"
        f.write(t)
    f.write("Process Completed") #sari file move ho gai, log file me entry kr di "Successfuly Completed"
    f.close()  #log file closed
def read_data():  #ye 2nd function hai read_data
    w=open("output.txt","r+")  #agr read krna hai log file to open kro read write mode mai
    data=w.read() #read kro
    w.close() #band kro
    return(data) #data return kr do.....
def menu(): #ye 3rd function hai 
    def hello(): #nested function hello
        messagebox.showinfo("MENU", "Do nothing!") #Isse user ko dika Menu, but uspr click krne se kch hoga ni (Jb run kroge dek left left me upr dikega)
    def kill():
        exit()   #isse exit ho jayga cross pr click krne se
    def en_data():
        f=open("path.txt","w+") #file opened in w+ means both write and read agr koi file hogi phle se to override bhi kr dega use, ni hogi to bna dega new file
        inp=e1.get() 
        f.write(inp)
        f.close()
    top = Tk() #creates object of tkinter
    top.geometry("1500x1500") #set dimension of window
    var = StringVar() #Stringvar is a function of tkinter used to hold string
    label = Message(top, textvariable=var, relief=RAISED)
    var.set("DESTINII")  #UI bnai hai ab ye sb neche
    label.configure(width='500',justify=CENTER,bg='lightblue',font='Algerian 18 bold',bd='8px',padx='10',pady='20',fg='black')
    label.pack()
    labelframe = LabelFrame(top, text="MENU")
    labelframe.configure(bg='light blue',font='Arial 15 bold',fg='green',bd='5px')
    file_ent = Label(labelframe, text="Enter the path where File management will be Active:-")
    file_ent.configure(bg='white',font='Arial 14 bold',bd='4px',padx='3',pady='3',fg='black')
    file_ent.place(x=30,y=120)
    e1 = Entry(top,width=60)
    e1.place(x=560,y=243)
    B1 = Button(top, text = "Instructions", command = hello)
    B1.configure(bg='brown',fg='white',font='Arial 15 bold')
    B1.place(x = 35,y = 180)
    B2 = Button(top, text = "Manage", command = file_manage)
    B2.configure(bg='white',fg='black',font='Arial 10 bold')
    B2.place(x = 500,y = 300)
    
    text1 = Label(text="OUTPUT")
    text1.place(x=60, y=330)
    output = Text(top)
    dat=read_data()
    output.insert(INSERT,dat)
    output.place(x=50,y=350)
    B3 = Button(top, text = "Confirm", command =lambda: en_data())
    B3.configure(bg='white',fg='black',font='Arial 10 bold')
    B3.place(x = 900,y = 240)
    labelframe.pack(fill="both", expand="yes")
    top.mainloop()
menu() #function call to menu