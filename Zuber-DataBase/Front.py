import tkinter as tk
import UsersBackend as UB
import CarsBackend as CB
import MatchesBackend as MB

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand="True")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Matches, Cars, Users):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        menu = tk.Menu(self.master)
        self.config(menu=menu)
        file = tk.Menu(menu)
        file.add_command(label='Exit', command=self.exi)
        menu.add_cascade(label='File', menu=file, command=self.exi)

        run = tk.Menu(menu)
        run.add_command(label='Users', command=lambda: self.show_frame(Users))
        run.add_command(label='Cars', command=lambda: self.show_frame(Cars))
        run.add_command(label='MATCHES', command=lambda: self.show_frame(Matches))
        menu.add_cascade(label='RUN', menu=run)

    def exi(self):
        exit()

    def show_frame(self, PageName):
        frame = self.frames[PageName]
        frame.tkraise()


class Matches(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def get_selected_row(event):
            global selected_Tuple
            index = list1.curselection()
            selected_Tuple = list1.get(index)

        def view_command():
            list1.delete(0,tk.END)
            for row in MB.view():
                list1.insert(tk.END, row)

        def search_command():
            list1.delete(0, tk.END)
            for row in MB.search(CID.get(), UID.get()):
                list1.insert(tk.END, row)
        def add_command():
            MB.insert(CID.get(),UID.get(),Payment.get())

        def delete_command():
            MB.delete(selected_Tuple[0])

        lbl_ID = tk.Label(self, text="CarID:")
        lbl_ID.grid(row=0, column=0)

        CID = tk.StringVar()
        e1 = tk.Entry(self, textvariable=CID)
        e1.grid(row=0, column=1)

        lbl_ID2= tk.Label(self, text="UserID:")
        lbl_ID2.grid(row=0, column=2)

        UID = tk.StringVar()
        e2 = tk.Entry(self, textvariable=UID)
        e2.grid(row=0, column=3)

        lbl_payment = tk.Label(self, text="Payment:")
        lbl_payment.grid(row=0, column=4)

        Payment = tk.StringVar()
        e3= tk.Entry(self, textvariable=Payment)
        e3.grid(row=0, column=5)

        list1=tk.Listbox(self,width=35,height=6)
        list1.grid(row=2, column=4, rowspan=6, columnspan=2)

        sb1=tk.Scrollbar(self)
        sb1.grid(row=2,column=6,rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview())
        list1.bind('<<ListboxSelect>>', get_selected_row)

        btn1 = tk.Button(self, text="View ALL", width=12, command=view_command)
        btn1.grid(row=2, column=2)

        btn2 = tk.Button(self, text="Search Entry", width=12, command=search_command)
        btn2.grid(row=2, column=3)

        btn3 = tk.Button(self, text="Add Entry", width=12, command=add_command)
        btn3.grid(row=3, column=2)

        btn4 = tk.Button(self, text="Selected Delete", width=12,command=delete_command)
        btn4.grid(row=3, column=3)
class Cars(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def get_selected_row(event):
            global selected_Tuple
            index = list1.curselection()
            selected_Tuple = list1.get(index
                                       )
        def view_command():
            list1.delete(0, tk.END)
            for row in CB.view():
                list1.insert(tk.END, row)

        def search_command():
            list1.delete(0, tk.END)
            for row in CB.search(ID.get(), DriverName.get(), DriverSurname.get(), CarModel.get()):
                list1.insert(tk.END, row)

        def add_command():
            CB.insert(ID.get(),DriverName.get(),DriverSurname.get(),CarModel.get())

        def delete_command():
            CB.delete(selected_Tuple[0])

        def update_command():
            print(selected_Tuple)
            CB.update(selected_Tuple[0],DriverName.get(),DriverSurname.get(),CarModel.get())

        lbl_ID = tk.Label(self, text="CarID:")
        lbl_ID.grid(row=0, column=0)

        ID = tk.StringVar()
        e1 = tk.Entry(self, textvariable=ID)
        e1.grid(row=0, column=1)

        lbl_Name = tk.Label(self, text="DriverName:")
        lbl_Name.grid(row=0, column=3)

        DriverName = tk.StringVar()
        e2 = tk.Entry(self, textvariable=DriverName)
        e2.grid(row=0, column=4)

        lbl_Surname = tk.Label(self, text='Driver SName:')
        lbl_Surname.grid(row=1, column=0)

        DriverSurname = tk.StringVar()
        e3 = tk.Entry(self, textvariable=DriverSurname)
        e3.grid(row=1, column=1)

        lbl_Car=tk.Label(self,text='Car model:')
        lbl_Car.grid(row=1,column=3)

        CarModel=tk.StringVar()
        e4=tk.Entry(self,textvariable=CarModel)
        e4.grid(row=1,column=4)

        list1 = tk.Listbox(self, width=35, height=6)
        list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb1 = tk.Scrollbar(self)
        sb1.grid(row=2, column=2, rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview())
        list1.bind('<<ListboxSelect>>', get_selected_row)

        btn1 = tk.Button(self, text="View ALL", width=12,command=view_command)
        btn1.grid(row=2, column=3)

        btn2 = tk.Button(self, text="Search Entry", width=12,command=search_command)
        btn2.grid(row=3, column=3)

        btn3 = tk.Button(self, text="Add Entry", width=12, command=add_command)
        btn3.grid(row=2, column=4)

        btn4 = tk.Button(self, text="Selected Delete", width=12, command=delete_command)
        btn4.grid(row=3, column=4)

        btn4 = tk.Button(self, text="Selected Update", width=12, command=update_command)
        btn4.grid(row=4, column=3)

class Users(tk.Frame):

    def __init__(self, parent, controller):
        def get_selected_row(event):
            global selected_Tuple
            index = list1.curselection()
            # Direk kayıdı listeden alıyoruz
            selected_Tuple = list1.get(index)

        def view_command():
            list1.delete(0, tk.END)
            for row in UB.view():
                list1.insert(tk.END, row)

        def search_command():
            list1.delete(0, tk.END)
            for row in UB.search(ID.get(), Name.get(), Surname.get(), age.get()):
                list1.insert(tk.END, row)

        def delete_command():
            UB.delete(selected_Tuple[0])

        def add_command():
            UB.insert(ID.get(), Name.get(), Surname.get(), age.get())

        def update_command():
            print(selected_Tuple)
            UB.update(selected_Tuple[0], Name.get(), Surname.get(), age.get())

        tk.Frame.__init__(self, parent)

        lbl_ID = tk.Label(self, text="CustomerID:")
        lbl_ID.grid(row=0, column=0)

        ID = tk.StringVar()
        e1 = tk.Entry(self, textvariable=ID)
        e1.grid(row=0, column=1)

        lbl_Name = tk.Label(self, text="UserName")
        lbl_Name.grid(row=0, column=3)

        Name = tk.StringVar()
        e2 = tk.Entry(self, textvariable=Name)
        e2.grid(row=0, column=4)


        lbl_Surname=tk.Label(self,text='SurName:')
        lbl_Surname.grid(row=1,column=0)

        Surname=tk.StringVar()
        e3=tk.Entry(self,textvariable=Surname)
        e3.grid(row=1,column=1)

        lbl_age=tk.Label(self,text='Age:')
        lbl_age.grid(row=1,column=3)

        age=tk.StringVar()
        e4=tk.Entry(self,textvariable=age)
        e4.grid(row=1,column=4)


        list1=tk.Listbox(self,width=35,height=6)
        list1.grid(row=2,column=0,rowspan=6,columnspan=2)


        sb1=tk.Scrollbar(self)
        sb1.grid(row=2,column=2,rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview())
        list1.bind('<<ListboxSelect>>', get_selected_row)

        btn1 = tk.Button(self, text="View ALL", width=12,command=view_command)
        btn1.grid(row=2, column=5)

        btn2 = tk.Button(self, text="Search Entry", width=12,command=search_command)
        btn2.grid(row=3, column=5)

        btn3 = tk.Button(self, text="Add Entry", width=12, command=add_command)
        btn3.grid(row=2, column=4)

        btn4 = tk.Button(self, text="Selected Delete", width=12, command=delete_command)
        btn4.grid(row=3, column=4)

        btn5=tk.Button(self,text="Selected Update",width=12,command=update_command)
        btn5.grid(row=4,column=4)

root = Window()
root.mainloop()
