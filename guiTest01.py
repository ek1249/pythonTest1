from tkinter import *

canvas_height = 400
canvas_width= 600
canvas_color = "black"

window = Tk() #tk()는 윈도우를 만들어주는 함수이다.
window.title("마음대로 그려 보세요.")

Label(window,text="이름뭐고?").grid(row=0,column=0,sticky=W)
name = Entry(window,width=20,bg="light green").grid(row=1,column=0,sticky=W)
Button(window,text="제출",width=5,command=click).grid(row=2,column=0,sticky=W)
window.mainloop()