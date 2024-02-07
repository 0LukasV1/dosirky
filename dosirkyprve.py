import tkinter as tk
fr1=open("vrcholy.txt","r",encoding="UTF-8")
fr2=open("hrany.txt","r",encoding="UTF-8")
mesta={}
m=0
def kresli_mesta(mesta):
    for i in fr1:
        parts=i.strip().split(";")
        x=int(parts[1])
        y=int(parts[2])
        canvas.create_oval(x,y,x+5,y+5,fill="aqua")
        canvas.create_text(x,y+10,text=parts[0])
        mesta[parts[0]]={0:x,1:y, 'visited': False, 'neighbours': []}
    #print(mesta)
def kresli_hrany(mesta):
    global m
    for i in fr2:
        parts=i.strip().split(";")
        canvas.create_line(mesta[parts[0]][0], mesta[parts[0]][1], mesta[parts[1]][0], mesta[parts[1]][1], fill="RoyalBlue")
        mesta[parts[0]]['neighbours'].append(parts[1])
        mesta[parts[1]]['neighbours'].append(parts[0])
        if m == 0:
            m = parts[0]
def into_the_width(m, mesta):
    queue = [m]
    while queue:
        current_mesto = queue.pop(0)
        if not mesta[current_mesto]['visited']:
            mesta[current_mesto]['visited'] = True
            canvas.create_oval(mesta[current_mesto][0], mesta[current_mesto][1], mesta[current_mesto][0]+5, mesta[current_mesto][1]+5, fill="gold")
            for neighbour in mesta[current_mesto]['neighbours']:
                if not mesta[neighbour]['visited']:
                    queue.append(neighbour)

win=tk.Tk()
canvas=tk.Canvas(width=1000,height=600,bg="hotpink")
canvas.pack()
kresli_mesta(mesta)
kresli_hrany(mesta)
into_the_width(list(mesta.keys())[0],mesta) #intothewidth(next(iter(mesta)),mesta)
win.mainloop()
