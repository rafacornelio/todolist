#importing packages 
from  tkinter import * 
import tkinter.messagebox
#function to enter the task in the Listbox
def entertask():
    #A new window to pop up to take input
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    def delete():
        entry_task.delete(1.0, "end-1c")
                
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command=add)
    button_temp.pack()
    button_temp=Button(root1,text="Delete task",command=delete)
    button_temp.pack()
    root1.mainloop()
    

#function to facilitate the delete task from the Listbox
def deletetask():
    if listbox_task.curselection():
        #selects the slected item and then deletes it 
        selected=listbox_task.curselection()
        listbox_task.delete(selected[0])
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="Select a text")  

#Executes this to mark completed 
def markcompleted():
    if listbox_task.curselection():
        marked=listbox_task.curselection()
        temp=marked[0]
        #store the text of selected item in a string
        temp_marked=listbox_task.get(marked)
        #update it 
        temp_marked=temp_marked+" ✔"
        #delete it then insert it 
        listbox_task.delete(temp)
        listbox_task.insert(temp,temp_marked)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="Select a text")  

#Executes this to delete mark completed
def delmarkcompleted():
    if listbox_task.curselection():
        marked=listbox_task.curselection()
        temp=marked[0]
        #store the text of selected item in a string   
        temp_marked=listbox_task.get(marked)
        #update it
        if " ✔" in temp_marked: 
            temp_marked=temp_marked.replace(" ✔","")
            #delete it then insert it 
            listbox_task.delete(temp)
            listbox_task.insert(temp,temp_marked)
        else:
            tkinter.messagebox.showwarning(title="Warning!",message="This text not a marked")    
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="Select a text")  

#creating the initial window
window=Tk()
#giving a title
window.title("DataFlair To_Do_APP")
#Frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()

#to hold items in a listbox
listbox_task=Listbox(frame_task,bg="black",fg="white",height=15,width=50,font = "Helvetica")
scrollbarH_task=Scrollbar(frame_task)
scrollbarH_task.pack(side=tkinter.BOTTOM,fill=tkinter.X)
scrollbarH_task.config(command=listbox_task.xview)
listbox_task.pack(side=tkinter.LEFT)

#Scrolldown in case the total list exceeds the size of the given window 
scrollbarV_task=Scrollbar(frame_task)
scrollbarV_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(xscrollcommand=scrollbarH_task.set, yscrollcommand=scrollbarV_task.set)
scrollbarV_task.config(command=listbox_task.yview)


#Button widget 
entry_button=Button(window,text="Add task",width=50,command=entertask)
entry_button.pack(pady=3)

delete_button=Button(window,text="Delete selected task",width=50,command=deletetask)
delete_button.pack(pady=3)

mark_button=Button(window,text="Mark as completed ",width=50,command=markcompleted)
mark_button.pack(pady=3)

delmark_button=Button(window,text="Delete as marked ",width=50,command=delmarkcompleted)
delmark_button.pack(pady=3)

window.mainloop()


