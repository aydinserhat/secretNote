import tkinter
from tkinter import *
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
ekran = tkinter.Tk()
ekran.title("Screet Notes")
ekran.minsize(width=400, height=800)
my_key= ""
key = Fernet.generate_key()
fernet=Fernet(key)
encMessage = ""

def enc_text():
    check_text()
    z = my_text_cevap.get("1.0", END)
    global my_key
    my_key= key_sonuc.get()
    global encMessage
    encMessage = fernet.encrypt(z.encode())
    with open('deneme.txt', 'w') as f:
        f.write(str(encMessage))

def dec_text():
    global encMessage
    key1 = key_sonuc.get()
    my_title= baslik_cevap.get()
    if key1 == my_key:
        decMessage = fernet.decrypt(encMessage).decode()
        with open('deneme1.txt', 'w') as f:
            f.write(my_title)
            f.write(str(decMessage))
    else:
        label=tkinter.Label(text="Please enter true key")
        label.place(x=50, y=690)


def check_text():
    t=baslik_cevap.get()
    y=my_text_cevap.get("1.0",END)
    print(y)
    k=key_sonuc.get()
    if t== "" or t == " ":
        label=tkinter.Label(text="Enter title!")
        label.place(x=50,y=690)

    elif y== "" or y == " ":
        label=tkinter.Label(text="Enter text!")
        label.place(x=50,y=690)
    elif k == "" or k == " ":
        label=tkinter.Label(text="Enter key!!")
        label.place(x=50,y=690)

image=(Image.open("lastly.png"))
resize_image = image.resize((150,150),Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resize_image)
label=tkinter.Label(ekran,image=new_image)

label.place(x=125,y=0)

baslik= tkinter.Label(text="Enter your title;",font=('Arial',16,"normal"))
baslik.place(x=20,y=140)

baslik_cevap = tkinter.Entry(width=38)
baslik_cevap.place(x=20,y=170)

my_text= tkinter.Label(text="Enter your text;",font=('Arial',16,"normal"))
my_text.place(x=20,y=220)

my_text_cevap= tkinter.Text(width=50)
my_text_cevap.place(x=20,y=250)

key= tkinter.Label(text="Enter your key;",font=('Arial',16,"normal"))
key.place(x=20,y=580)

key_sonuc = tkinter.Entry(width=38)
key_sonuc.place(x=20,y=610)



save = tkinter.Button(text="Save & Encrypt",command=enc_text)
save.place(x=140,y=710)

decrypt = tkinter.Button(text="Decrypt",command=dec_text)
decrypt.place(x=165,y=740)


ekran.mainloop()