import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random as rm

root = tk.Tk()

root.title('Rock Paper Scissors')

pic = PhotoImage(file = 'PngItem_1219930.png')
root.iconphoto(False,pic)

root.lcount=0
root.rcount=0
root.match=1

img = PhotoImage(file="rock.png")      
img1 = PhotoImage(file="paper.png")
img2 = PhotoImage(file="scissors.png")

tb1 = PhotoImage(file="1st.png")
tb2 = PhotoImage(file="2nd.png")
tb3 = PhotoImage(file="3rd.png")
tb4 = PhotoImage(file="4th.png")

stone = PhotoImage(file = "erock.png")
scissor = PhotoImage(file = "escissors.png")
paper = PhotoImage(file = "epaper.png")

rstone = PhotoImage(file = "grock.png")
rscissor = PhotoImage(file = "gscissors.png")
rpaper = PhotoImage(file = "gpaper.png")

win = PhotoImage(file = "win.png")
loose = PhotoImage(file = "loose.png")
draw = PhotoImage(file = "draw.png")

poop = PhotoImage(file = "poop.png")
pc = PhotoImage(file = "pc.png")

up = PhotoImage(file = "thumbsup.png")
down = PhotoImage(file = "thumbsdown.png")

canvas = Canvas(root,bg="#f5f4f0", width=1600, height=1200)

def create_canvas():
    canvas.create_image(20,20, anchor=NW, image=img)
    canvas.create_image(400,400, anchor=NW, image=img1)     
    canvas.create_image(1100,200, anchor=NW, image=img2)
    canvas.pack()
    
def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    canvas.create_polygon(points, **kwargs, smooth=True)

def final():
    
    def call_main():
        root.lcount=0
        root.rcount=0
        root.match=1
        bup.destroy()
        bdown.destroy()
        main_menu()
        
    def play_aga():
        root.lcount=0
        root.rcount=0
        root.match=1
        canvas.delete(ALL)
        bup.destroy()
        bdown.destroy()
        btn1menu()
        
    create_canvas()
    
    bup = tk.Button(canvas,image = up,command = play_aga,bg = "#2980b9")
    bup.place(x=330,y=425)    
    bdown = tk.Button(canvas,image = down,command = call_main,bg = "#2980b9")
    bdown.place(x=890,y=425)
    
    round_rectangle(300,200,1000,400,fill="#f8f7f3",outline = "#2980b9")
    
    canvas.create_text(650,250,text = "Final score after  "+str(root.match-1)+" rounds is\n"+" You : "+str(root.lcount)+"\t\tMe : "+str(root.rcount),font = ("Comic Sans MS",26))
    
    if root.lcount>root.rcount:
        canvas.create_text(650,350,text = "Well I believe you might have heard.... Best of 3",font = ("Comic Sans MS",16))
    elif root.lcount<root.rcount:
        canvas.create_text(650,350,text = "You can't overpower me. Want to challenge again?",font = ("Comic Sans MS",16))
    else:
        canvas.create_text(650,350,text = "I guess we have to play another round for the winner",font = ("Comic Sans MS",16))
    
def btn1menu():
    
    canvas.delete(ALL)   
    
    def mmenu():
        canvas.delete(ALL)
        buttonback.destroy()
        buttonfwd.destroy()
        bch1.destroy()
        bch2.destroy()
        bch3.destroy()
        root.lcount=0
        root.rcount=0
        root.match=1
        main_menu()
        
    create_canvas()
    
    def btnn():
        bch1.configure(state = NORMAL)
        bch2.configure(state = NORMAL)
        bch3.configure(state = NORMAL)
        root.match+=1
        canvas.delete(ALL)
        if root.match>5 and root.lcount!=root.rcount:
            buttonback.destroy()
            buttonfwd.destroy()
            bch1.destroy()
            bch2.destroy()
            bch3.destroy()
            final()
            return
        btn1menu()
        buttonback.destroy()
        buttonfwd.destroy()
        bch1.destroy()
        bch2.destroy()
        bch3.destroy()
        
    buttonback = tk.Button(text = '\U000025c0',
                    borderwidth = 3,
                    width = 3,
                    height = 1,
                    bg = "#2980b9",
                    fg = "White",
                    font = ("Arial",24),
                    relief = RAISED,
                    activebackground = "#33B5E5",
                    command = mmenu
                   )
    buttonback.place(x=25,y=25)
    
    buttonfwd = tk.Button(text = "\U000025b6",
                borderwidth = 3,
                width = 3,
                height = 1,
                bg = "#2980b9",
                fg = "white",
                font = ("Arial",24),
                relief = RAISED,
                activebackground = "#33B5E5",
                command = btnn
               )
    buttonfwd.place(x=125,y=25)
    
    canvas.create_rectangle(400, 650, 1000, 710, fill="#91ccec",outline = "#2980b9")
    canvas.create_image(440,680,image=poop)
    canvas.create_image(960,680,image=pc)
    
    def update_count():
        canvas.create_text(490,680,text = str(root.lcount),font = ("Comic Sans MS",38,"bold"),fill = "#5f6a6a",tag="lcount")
        canvas.create_text(905,680,text = str(root.rcount),font = ("Comic Sans MS",38,"bold"),fill = "#5f6a6a",tag="rcount")
        canvas.create_text(690,680,text = "Round:"+str(root.match),font = ("Comic Sans MS",38,"bold"),fill = "#5f6a6a",tag="match")
        canvas.update()
        
    update_count()
    
    def res(i):
        if i < 0:
            canvas.create_image(1010,600,image=loose)
            root.lcount+=1
        elif i == 0:
            canvas.create_image(1020,600,image=draw)
        elif i > 0:
            canvas.create_image(1070,600,image=win)
            root.rcount+=1
        canvas.delete("lcount")
        canvas.delete("rcount")
        canvas.delete("match")
        
        update_count()

    def game(i):
        ans = rm.randint(1,3)
        lst = [rstone,rscissor,rpaper]
        canvas.create_image(1290,500,image=lst[ans-1])
        if ans == i:
            res(0)
        elif (i==1 and ans==3) or (i==2 and ans==1) or (i==3 and ans==2):
            res(1)
        else:
            res(-1)

    def btn_press1():
        bch1.configure(state = DISABLED)
        game(1)
        
    def btn_press2():
        bch2.configure(state = DISABLED)
        game(2)
        
    def btn_press3():
        bch3.configure(state = DISABLED)
        game(3)
    
    canvas.create_image(1215,70,image=tb1)
    canvas.create_image(1195,170,image=tb2)
    canvas.create_image(1130,270,image=tb3)
    canvas.create_image(190,400,image=tb4)
    
    bch1 = tk.Button(canvas,image = stone,command = btn_press1)
    bch1.place(x=70,y=360)
    bch2 = tk.Button(canvas,image = scissor,command = btn_press2)
    bch2.place(x=160,y=360)
    bch3 = tk.Button(canvas,image = paper,command = btn_press3)
    bch3.place(x=250,y=360)
    
def btn2menu():
    
    def mmenu():
        canvas.delete(ALL)
        buttonback.destroy()
        main_menu()
        
    line = "Each match consist of \U0001f590 rounds.\nThe person with the most points wins.Duh.\nAnd as of course you might not be knowing\n\t   "+"\U0000270A wins over \U0000270C \n\t   "+"\U0000270B wins over \U0000270A \n\t   "+"\U0000270C  wins over \U0000270B"
    
    round_rectangle(400, 30, 1000, 300, fill="#f8f7f3",outline = "#008080")
    
    canvas.create_text(700,60,text = "SERIOUSLY BRUH!\U0001f632",font = ("Comic Sans MS",20))
    canvas.create_text(700,200,text = line,font = ("Comic Sans MS",16))
    
    buttonback = tk.Button(text = '\U000025c0',
                    borderwidth = 3,
                    width = 3,
                    height = 1,
                    bg = "#008080",
                    fg = "White",
                    font = ("Arial",24),
                    relief = RAISED,
                    activebackground = "#40a0a0",
                    command = mmenu
                   )
    buttonback.place(x=25,y=625)
    
def main_menu():
    
    canvas.delete(ALL)
    create_canvas()

    def cfunc():
        button1.destroy()
        button2.destroy()
        button3.destroy()
        btn2menu()
        
    def callfunc():
        button1.destroy()
        button2.destroy()
        button3.destroy()
        btn1menu()
    
    button1 = tk.Button(text = 'Challenge \U0001f60f',
                        borderwidth = 3,
                        width = 16,
                        height = 3,
                        bg = "#2980b9",
                        fg = "White",
                        font = ("Comic Sans MS",24),
                        relief = RAISED ,
                        activebackground = "#33B5E5",
                        command = callfunc
                       )
    button1.place(x=550,y=100)

    button2 = tk.Button(text = 'How To Play? \U0001f9d0',
                        borderwidth = 3,
                        width = 16,
                        height = 3,
                        bg = "#008080",
                        fg = "White",
                        font = ("Comic Sans MS",24),
                        relief = RAISED,
                        activebackground = "#40a0a0",
                        command = cfunc
                       )
    button2.place(x=550,y=280)
    
    button3 = tk.Button(text = "I'm going.Byee! \U0001f44b",
                        borderwidth = 3,
                        width = 16,
                        height = 3,
                        bg = "#3a9fbf",
                        fg = "White",
                        font = ("Comic Sans MS",24),
                        relief = RAISED ,
                        activebackground = "#5eb3ce",
                        command = root.destroy
                       )
    button3.place(x=550,y=460)
    
main_menu()
mainloop() 