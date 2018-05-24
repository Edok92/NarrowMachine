from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import analyze
import getweets

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        menubar = MenuBar(self)
        self.config(menu=menubar)

    def switch_frame(self, frame_class):
       
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
    def Pie(self, hashtag):
        text = hashtag.get()
        print(text)
        nombre = 100
        result = [0.0, 0.0, 0.0, 0.0, 0.0]
         
        compteur = 0
        tweets = getweets.get_tweets(text, nombre)
        for tweet in tweets:
            print(tweet)
            tmp_res, nb = analyze.affiche_resultat(tweet)
            result[0] += tmp_res[0]
            result[1] += tmp_res[1]
            result[2] += tmp_res[2]
            result[3] += tmp_res[3]
            result[4] += tmp_res[4]
            
            compteur += nb
            
        explode2 = (result[0]/10, result[1]/10, result[2]/10, result[3]/10, result[4]/10)  
        
        result[0] = round(result[0]/compteur * 100, 2)
        result[1] = round(result[1]/compteur * 100, 2)
        result[2] = round(result[2]/compteur * 100, 2)
        result[3] = round(result[3]/compteur * 100, 2)
        result[4] = round(result[4]/compteur * 100, 2)
         
        figure2 = Figure(figsize=(5,4), dpi=80) 
        subplot2 = figure2.add_subplot(111) 
        

        labels2 = 'Enthousiaste', 'Content', 'Neutre', 'Triste', 'Colere'
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
       
        pieSizes = [result[0], result[1], result[2], result[3], result[4]]

        subplot2.pie(pieSizes, explode=explode2, labels=labels2, colors = colors, autopct='%1.1f%%', shadow=True, startangle=90) # create the pie chart based on the input variables x1, x2, and x3
        subplot2.axis('equal')  
         
        pie2 = FigureCanvasTkAgg(figure2, self) 
        pie2.get_tk_widget().configure(background='black', highlightcolor='black', highlightbackground='black')
        pie2.get_tk_widget().pack(side=LEFT)
         
class MenuBar(Menu):
    def __init__(self, master):
        Menu.__init__(self, master)

        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(label="Menu",underline=0, menu=fileMenu)
        fileMenu.add_command(label="back to menu", underline=1, command=lambda: master.switch_frame(StartPage))


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.geometry("500x400+350+400")
        start_label = Label(self, text="Welcome")
        page_1_button = Button(self, text="Open page one",
                                  command=lambda: master.switch_frame(PageOne))
        start_label.pack(side="top", fill="x", pady=10)
        page_1_button.pack()
        
      
class PageOne(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.geometry("1920x1080")
        
        hashtag = StringVar()
        recherche = Entry(self,textvariable=hashtag)
        recherche.pack(pady = 20)
        page_1_label = Label(self, text="choose key word")
        start_button = Button(self, text="Validate",
                                 command= lambda : master.Pie(hashtag))
        
        page_1_label.pack(side="top", fill="x", pady=10)
        start_button.pack()
       

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()