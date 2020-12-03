from tkinter import ttk
import tkinter as Tk



class int_gr(Tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        super().config(background="#000000")

        self.IP=Tk.StringVar() #adresa ip
        self.Network=Tk.StringVar() #retea
        self.CommunicationPort=Tk.DoubleVar() #port de comunicare
        self.MethodCode=Tk.StringVar() #lista metode
        self.MessageType=Tk.StringVar() #mesaj confirmabil sau neconfirmabil

        IP_label=ttk.Label(self, text="IP", foreground="#FFFFFF")
        Network_label=ttk.Label(self,text="Network", foreground="#FFFFFF")
        CommunicationPort_label = ttk.Label(self, text="Communication Port", foreground="#FFFFFF")

        combobox_MethodCode = ttk.Combobox(self,values=["GET","POST","Metoda 3"],textvariable=self.MethodCode, background="#FFFFFF")
        combobox_MessageType = ttk.Combobox(self, values=["Confirmabil", "Neconfirmabil"], textvariable=self.MessageType,background="#FFFFFF")
        spinbox_CommunicationPort = ttk.Spinbox(self, from_=0.0, to=2048, increment=1, textvariable=self.CommunicationPort, background="#FFFFFF")

        combobox_MethodCode.current(0)
        combobox_MessageType.current(0)

        Network_label = ttk.Label(self, text="Network", foreground="#FFFFFF", background="#000000")
        IP_label = ttk.Label(self, text="IP", foreground="#FFFFFF", background="#000000")

        Network_entry = ttk.Entry(self, textvariable=self.Network)
        IP_entry = ttk.Entry(self, textvariable=self.IP)

        Network_label.grid(row=1, column=14, sticky=Tk.SE, pady=2)
        Network_entry.grid(row=1, column=15, sticky=Tk.SE, pady=2)

        CommunicationPort_label = ttk.Label(self, text="CommunicationPort", foreground="#FFFFFF", background="#000000")
        MethodCode_label = ttk.Label(self, text="MethodCode", foreground="#FFFFFF", background="#000000")
        MessageType_label = ttk.Label(self, text="MessageType", foreground="#FFFFFF", background="#000000")


        CommunicationPort_label.grid(row=5, column=14, sticky=Tk.SE, pady=2)
        spinbox_CommunicationPort.grid(row=5, column=15, sticky=Tk.SE, pady=2)

        IP_label.grid(row=7, column=14, sticky=Tk.SE, pady=2)
        IP_entry.grid(row=7, column=15, sticky=Tk.SE, pady=2)

        MethodCode_label.grid(row=9, column=14, sticky=Tk.SE, pady=2)
        combobox_MethodCode.grid(row=9, column=15, sticky=Tk.SE, pady=2)

        MessageType_label.grid(row=11, column=14, sticky=Tk.SE, pady=2)
        combobox_MessageType.grid(row=11, column=15, sticky=Tk.SE, pady=2)





class MainInt(Tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Aplicatie Client CoAP")
        self.geometry("500x500")

        self.resizable(width=False, height=False)

        int_gr(self).grid()


app = MainInt()
app.config(background="#000000")
app.mainloop()
       


