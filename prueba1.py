from tkinter import *
y=750

vent = Tk()
vent.title("Prueba1-II bimestre")
canvas= Canvas(vent, width=1000, height=600)
canvas.pack()
i1= PhotoImage(file="nave.png")
i= PhotoImage(file="planeta.png")
canvas.create_image(750,50,anchor=NW, image=i1)
canvas.create_image(10,50,anchor=NW, image=i)

def choque(event):
    global y
    if event.keysym == 'Left':
        canvas.move(1,-15,0)
        y=y-3
        print("coor x: ",1,"y: ",y)
        if y==633:
            print("Choque")
      
    else:
        canvas.move(1,3,0)


canvas.bind_all('<KeyPress-Left>',choque)
canvas.bind_all('<KeyPress-Right>',choque)


vent.mainloop()

