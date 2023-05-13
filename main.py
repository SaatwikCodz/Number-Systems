from customtkinter import *
import customtkinter
import pyautogui as pag
from PIL import Image
flag = ''
w,h = pag.size()
customtkinter.set_appearance_mode("Dark")
def Landing():
    global w,h
    win1 = CTk()
    old = Image.open('Assets\\Wallpaper.jpg')
    new_image = old.resize((w, h))
    new_image.save('Assets\\Wallpaper.jpg')
    background = customtkinter.CTkImage(light_image = Image.open('Assets\\Wallpaper.jpg'),
                        dark_image = Image.open('Assets\\Wallpaper.jpg'),
                        size=(w, h))
    back = CTkLabel(win1,text = ' ', image = background).pack() 
    framey, framex = h - 101, w - 121
    back = CTkLabel(win1,text = ' ', image = background).pack()
    frame = CTkFrame(win1,fg_color="white",width=w - 121,height=h - 101)
    frame.place(x = w / 2 - (w - 121) / 2, y = h / 2 - (h - 101) / 2)
    label2 = CTkLabel(frame, text = 'Welcome Back!', font = ("Times", 75, "bold"), text_color = 'Black')
    label2.place(x = framex / 2- 230, y =10)

    def quitoff():
        nonlocal frame, win1
        nonlocal label2
        global flag, i
        def yes():
            global flag, i
            win1.destroy()
            flag = 'Quit'
            i = 1
        fy, fx = h-300,w-300
        f = CTkFrame(frame, fg_color="white",width=w - 300,height=h - 300, border_width = 3, border_color = 'blue')
        f.place(x = framex / 2 - ((w - 300) / 2), y = framey /2 - ((h - 300) / 2))
        def no():
            f.destroy()
            label2 = CTkLabel(frame, text = 'Welcome Back!', font = ("Times", 75, "bold"), text_color = 'Black')
            label2.place(x = framex / 2- 230, y =10)
        check = CTkLabel(f, text = "Do you really want to quit?",text_color = 'black', font = ("Times", 45, "bold")).place(x = fx / 2 -100 - 150, y= 5)
        yes = CTkButton(f, text = "Yes!",font = ("Times", 75, "bold"),fg_color="transparent",text_color = "blue",hover_color = 'red',border_width = 2, border_color = "red",corner_radius = 12, command = yes).place(x = fx / 2 -100 - 150 - 100, y= fy / 2 - 50)
        no = CTkButton(f, text = "Nope!",font = ("Times", 75, "bold"),fg_color="transparent",text_color = "blue",hover_color = 'green',border_width = 2, border_color = "green",corner_radius = 12, command = no).place(x = fx / 2 -100 + 150 + 100, y= fy / 2 - 50)
    button1 = CTkButton(frame, text = "Start",font = ("Times", 75, "bold"),fg_color="transparent",text_color = "#a51212",border_width = 2, border_color = "blue",corner_radius = 12).place(x = framex / 2- 200 - 50 + 50 + 100, y =150)
    button2 = CTkButton(frame, text = "Quit",font = ("Times", 75, "bold"),fg_color="transparent",text_color = "#a51212",border_width = 2, border_color = "blue",corner_radius = 12, command = quitoff).place(x = framex / 2- 200 - 50 + 50 + 100 - 35 + 35 + 5.5 + 0.4 + 0.2 , y = framey - 300 - 50 + 25)
    button3 = CTkButton(frame, text = "View Credits",font = ("Times", 75, "bold"),fg_color="transparent",text_color = "#a51212",border_width = 2, border_color = "blue",corner_radius = 12).place(x = framex / 2- 200 - 50 + 50 + 100 + 15 - 45 - 35 - 10 - 16 - 20 - 3, y = framey - 150)
    win1.attributes('-fullscreen',True)
    win1.mainloop()
Landing()