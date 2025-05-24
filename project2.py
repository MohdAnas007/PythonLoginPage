from tkinter import *
from PIL import ImageTk,Image
import os
def load_next_img():
    global count
    img_label.config(image=img_arr[count])
    count+=1
    if count>len(img_arr)-1:
        count=0

count=1
root=Tk()
root.title('Wallpaper Viewer')
root.geometry('250x400')
root.config(bg='black')


files=os.listdir('wallpapers')
img_arr=[]

for file in files:

    img = Image.open(os.path.join('wallpapers',file))
    resized_img=img.resize((200,300))
    img_arr.append(ImageTk.PhotoImage(resized_img))

img_label=Label(root,image=img_arr[0])
img_label.pack(pady=(15,15))


button=Button(root,text='Next',bg='white',fg='black',height=2,width=19,command=load_next_img)
button.pack(pady=(5,15))
print(img_arr)
root.mainloop()
