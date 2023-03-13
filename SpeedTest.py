
import tkinter as tk
import time
from essential_generators import DocumentGenerator
import Levenshtein

class TypeSpeedGUI:
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("TypingSPeedTest")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        
    
        
        global s
        gen = DocumentGenerator()
        s1=gen.paragraph()
        s2=s1[0:10]
        s=s2.rstrip()
        
        self.frame=tk.Frame(self.root)
        
        self.sample_label = tk.Label(self.frame, text=s, font=("Time New Roman",11))
        self.sample_label.grid(row=0,column=0,columnspan=10,padx=5,pady=10)
        
        self.input_entry = tk.Entry(self.frame, width=40, font=("Arial",11))
        self.input_entry.grid(row=1,column=0,columnspan=10,padx=5,pady=10)
        
        self.input_entry.bind("<KeyPress>",self.start)
        
        self.speed_label = tk.Label(self.frame, text="Speed= 0.00 \n CPM =0.00 \n Accuracy=0.00%", font=("Time New Roman",11))
        self.speed_label.grid(row=2,column=0,columnspan=2,padx=5,pady=10)
    
        self.frame.pack(expand=True)
        
        self.counter = 0
        self.running = False
        
        self.root.mainloop()
        
        
    def start(self, event):
        
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                global start
                global end
                start=time.time()
                self.submit_button = tk.Button(self.frame, text="Submit",command=self.print)
                self.submit_button.grid(row=3,column=0,columnspan=2,padx=5,pady=10)
                


                
            
        
    

    def print(self):
        
        
        end=time.time()
        t=end-start
        cps = len(self.input_entry.get())/t
        cpm = cps * 60
        s2=self.input_entry.get()
        d=Levenshtein.distance(s,s2)
        accuracy= (len(s)-d)/len(s) * 100
        if accuracy==100:
            self.input_entry.config(fg= "green")
            self.root.configure(bg='green')
            self.running=False
        else:
            self.input_entry.config(fg= "red")
            self.root.configure(bg='red')

             
        self.speed_label.config(text=f"Speed = {t:.2f}  \n CPM={cpm:.2f} \n Accuracy = {accuracy:.2f} %")

                
             
          
        pass
TypeSpeedGUI()    





