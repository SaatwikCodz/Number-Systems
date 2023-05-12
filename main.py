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
    button1 = CTkButton(frame, text = "Start",font = ("Times", 75, "bold"),fg_color="transparent",text_color = "#a51212",border_width = 2, border_color = "blue",corner_radius = 12, command = login1234).place(x = framex / 2- 200 - 50 + 50 + 100, y =150)
    button2 = CTkButton(frame, text = "Quit",font = ("Times", 75, "bold"),fg_color="transparent",text_color = "#a51212",border_width = 2, border_color = "blue",corner_radius = 12, command = signup).place(x = framex / 2- 200 - 50 + 50 + 100 - 35, y = framey - 300 - 50 + 25)
    button3 = CTkButton(frame, text = "View Credits",font = ("Times", 75, "bold"),fg_color="transparent",text_color = "#a51212",border_width = 2, border_color = "blue",corner_radius = 12, command = quitoff).place(x = framex / 2- 200 - 50 + 50 + 100 + 15, y = framey - 150)
    win1.attributes('-fullscreen',True)
    win1.mainloop()
    print('damn')
    return
    print('YOO')
def Login():
    global j
    win2 = CTk()
    framey, framex = h - 101, w - 121
    old = Image.open('Default Stuff\\Wallpaper.jpg')
    new_image = old.resize((w, h))
    new_image.save('Default Stuff\\Wallpaper.jpg')
    background = CTkImage(light_image = Image.open('Default Stuff\\Wallpaper.jpg'),
                        size=(w, h))
    back = CTkLabel(win2,text = ' ', image = background).pack()
    frame = CTkFrame(win2,fg_color="white",width=w - 121,height=h - 101)
    frame.place(x = w / 2 - (w - 121) / 2, y = h / 2 - (h - 101) / 2)
    label2 = CTkLabel(frame, text = 'Please Log-in!', font = ("Times", 75, "bold"), text_color = 'Black')
    label2.place(x = framex / 2- 230, y =10)
    spaces = '       '
    label3 = CTkLabel(frame, text = "Username Below", font = ("Times", 45, "bold"), text_color = 'Black').place(x = framex / 2 - 200 + 25, y = 200 - 40)
    entry1 = CTkEntry(frame, placeholder_text = f'{spaces}Username Here', width = 360, font = ("Times", 35, "bold"))
    entry1.place(x = framex / 2 - 200, y = 275 - 40)
    label4 = CTkLabel(frame, text = "Password Below", font = ("Times", 45, "bold"), text_color = 'Black').place(x = framex / 2 - 200 + 25, y = 336 -40)
    entry2 = CTkEntry(frame, placeholder_text = f'{spaces}Password Here',font = ("Times", 35, "bold"), width = 360, show = '*')
    entry2.place(x = framex / 2 - 200, y = 275 + 136 - 40)
    green = 0
    def sblind():
        nonlocal green, entry2
        if green == 0:
            te = entry2.get()
            show = CTkButton(frame, image = CTkImage(light_image = Image.open('Fixed Stuff\\Blind.png'),
                        size=(30, 30)), text = '', width = 30, fg_color="transparent", hover_color = 'white', command = sblind).place(x = framex / 2 + 50 + 120, y = 275 + 136 - 40 + 3)
            entry2 = CTkEntry(frame, placeholder_text = f'{spaces}Password Here',font = ("Times", 35, "bold"), width = 360)
            entry2.place(x = framex / 2 - 200, y = 275 + 136 - 40)

            if te != '':
                entry2.insert(0, te)
            green = 1
        elif green == 1:
            text = entry2.get()
            show = CTkButton(frame, image = CTkImage(light_image = Image.open('Fixed Stuff\\Show.png'),
                        size=(30, 30)), text = '', width = 30, fg_color="transparent", hover_color = 'white', command = sblind).place(x = framex / 2 + 50 + 120, y = 275 + 136 - 40 + 3)
            entry2 = CTkEntry(frame, placeholder_text = f'{spaces}Password Here',font = ("Times", 35, "bold"), width = 360, show = '*')
            entry2.place(x = framex / 2 - 200, y = 275 + 136 - 40)
            if text != '':
                  entry2.insert(0, text)
            green = 0
    show = CTkButton(frame, image = CTkImage(light_image = Image.open('Fixed Stuff\\Show.png'),
                        size=(30, 30)), text = '', width = 30, fg_color="transparent", hover_color = 'white', command = sblind).place(x = framex / 2 + 50 + 120, y = 275 + 136 - 40 + 3)
    def singup():
        nonlocal win2
        global flag
        win2.destroy()
        j = 1
        flag = 'Go to Signup'.lower()
        return 
    def laggin():
        Username = entry1.get()
        Password = entry2.get()
    button1 = CTkButton(frame, text = "Login!",font = ("Times", 55, "bold"),fg_color="transparent",width = 400 - 43, text_color = "#041a5d",border_width = 2, border_color = "blue",corner_radius = 12, hover_color = 'yellow').place(x = framex / 2 - 200, y = 275 + 136 + 100 - 50 - 20)
    button2 = CTkButton(frame, text = "SignUp!",font = ("Times", 55, "bold"),fg_color="transparent",width = 400 - 43, text_color = "#041a5d",border_width = 2, border_color = "blue",corner_radius = 12, hover_color = 'yellow', command = singup).place(x = framex / 2 - 200, y = 275 + 136 + 100 - 50 + 50 + 25)
    def last():
        nonlocal win2
        global flag, j
        win2.destroy()
        j = 1
        print(win2)
        flag = 'Go to landing'.lower()
        return 
    lastpage = CTkButton(frame, text = '<-', width = 50 - 15, command = last).place(x = 5, y = 5)
    win2.attributes('-fullscreen', True)
    win2.mainloop()
    win1.attributes('-fullscreen',True)
    win1.mainloop()
Landing()