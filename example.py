import tkinter as tk

root= tk.Tk()

root.geometry("600x400")

id_var=tk.StringVar()
length_var=tk.StringVar()

def submit():
 
    id=id_var.get()
    length=length_var.get()
     
    print("The ID is : " + id)
    print("The Word length is : " + length)
     
    id_var.set("")
    length_var.set("")


id_label = tk.Label(root, text = 'ID', font=('calibre',10, 'bold'))
id_entry = tk.Entry(root,textvariable = id_var, font=('calibre',10,'normal'))
length_label = tk.Label(root, text = 'size', font = ('calibre',10,'bold'))
length_entry=tk.Entry(root, textvariable = length_var, font = ('calibre',10,'normal'), show = '*')
sub_btn=tk.Button(root,text = 'Submit', command = submit)

id_label.grid(row=0,column=0)
id_entry.grid(row=0,column=1)
length_label.grid(row=1,column=0)
length_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()