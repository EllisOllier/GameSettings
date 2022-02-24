import main
from os import path
import os
import shutil


cwd = os.getcwd()
currentDir = "{0}".format(cwd)
optionsName = currentDir

mcPath = path.expandvars(r'%APPDATA%\.minecraft')
os.chdir(mcPath)
print("Minecraft Settings Loaded Successfully!\n")

fileInit = open("options.txt")
fileConts = fileInit.read()

def mcSettings():

    saveOrEditMc = input(" \nSave: s \nEdit: e\nWould you like to save or edit your options: ")
    if saveOrEditMc == 's' or saveOrEditMc == 'S':
        os.popen(r'copy ' + str(mcPath + "\options.txt") + " " + str(currentDir))
        print("options.txt has been saved in: " + currentDir)
    elif saveOrEditMc == 'e' or saveOrEditMc == 'E':
        optionChanger()

def optionChanger():
    isFound = 0
    changeOption = input("What setting would you like to change(e.g. gamma, fov, renderDistance): ")
    for i in fileConts:
        if changeOption in fileConts:
            
            isFound = 1
        else:
            isFound = 0
            break
    if isFound == 1:
        print("Option found!")
    else:
        print("Option not found!")