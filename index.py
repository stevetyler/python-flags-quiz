import tkinter as tk
import pycountry
import os
import random

root = tk.Tk()

def getFlags():
    global flaglist
    flaglist = []
    pathlist = os.listdir('./flagopedia')  # get list of flag images, eg ['uk.png', 'fr.png', 'it.png', etc]
    pathlistLen = len(pathlist) - 1

    #choose 3 random countries from pathlist
    for num in range (0, 3):
        index = random.randint(0, pathlistLen)
        fileName = pathlist[index]
        countryCode = fileName[:-4].upper() #remove '.png' from name and make uppercase
        countryName = pycountry.countries.get(alpha_2=countryCode).name
        flaglist.append(countryName)
    print(flaglist)
    #showFlag()

def showFlag():
    global displayedFlagIndex

    flagIndex = random.randint(0, 2) #
    print('flagIndex %d'  %(flagIndex))
    displayedFlagIndex = flagIndex
    displayedFlag = flaglist[flagIndex]
    print(displayedFlag)

    country = pycountry.countries.get(name=displayedFlag)
    flagImgPath = "./flagopedia/%s.png" %(country.alpha_2.lower())
    #print(flagImgPath)

    flagImg = tk.PhotoImage(file=flagImgPath)

    #flagImg = tk.PhotoImage(file=flagImgPath)
    lbl.configure(image=flagImg)
    lbl.myFlagImg = flagImg #save reference to image or garbage collection will remove

def displayButtons():
    btn1 = tk.Button(root, text=flaglist[0])
    btn1.bind("<Button-1>", selectFlag) # bind to left click
    btn1.pack()

    btn2 = tk.Button(root, text=flaglist[1])
    btn2.bind("<Button-1>", selectFlag) # bind to left click
    btn2.pack()

    btn3 = tk.Button(root, text=flaglist[2])
    btn3.bind("<Button-1>", selectFlag) # bind to left click
    btn3.pack()

def selectFlag(index):
    if index == displayedFlagIndex:
        tk.Label(root, text = 'Correct!').pack()
    else:
        tk.Label(root, text = 'Incorrect!').pack()


getFlags()
showFlag()
displayButtons()


#input = tk.Entry(root)
#input.pack()
#input.focus_set()
#input.bind("<Return>", showFlag)

#photo = tk.PhotoImage(file='./splash.png')
#lbl = tk.Label(root, image=photo)
#lbl.pack()



root.mainloop()
