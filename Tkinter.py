from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
def handle_click():
    email=email_input.get()
    passw=pass_input.get()
    if email=='anas@gmail.com' and passw=='1234':
        messagebox.showinfo('yay','Login Succesful')

    else:
        messagebox.showerror('Login Failed!','try again ')



root=Tk()
root.title("Login Window")
# root.minsize(100,100)
# root.maxsize(500,500)

root.geometry('350x500')
root.configure(background='#0096DC')
img=Image.open('Wallpapers/flipkart-icon.png')
resized_img=img.resize((70,70))
img=ImageTk.PhotoImage(resized_img)
img_label =Label(root,image=img)
img_label.pack(pady=(10,10))
text_label=Label(root,text='Flipkart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))


#for email input
email_input=Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_input.pack(pady=(20,5))
email_input.config(font=('verdana',12))
email_input=Entry(root,bg='white',fg='black',width=50)
email_input.pack(ipady=2)

#for password input

pass_input=Label(root,text='Enter Password',fg='white',bg='#0096DC')
pass_input.pack(pady=(20,5))
pass_input.config(font=('verdana',12))
pass_input=Entry(root,bg='white',fg='black',width=50)
pass_input.pack(ipady=2)


# for button

login_button=Button(root,text='Login',bg='white',fg='black',width=10,height=1,command=handle_click)
login_button.pack(pady=(10,20))
login_button.config(font=('verdana',10))
root.mainloop()


