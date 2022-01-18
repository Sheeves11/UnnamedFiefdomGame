import os
import time
import random

'''

This program deletes and initializes all data files
for the Unnamed Fiefdom Game.

More info at github.com/Sheeves11/unnamedfiefdomgame

'''

#initial screen clear
os.system("clear")

answer = input('Would you like to wipe the server and all user data? (y/n): ')

if answer == 'y':
    print('\nDeleting all text files...\n\n')

    #Delete Fiefdoms
    dir_name = "fiefs/"
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".txt"):
            os.remove(os.path.join(dir_name, item))
    print('Fiefdoms Deleted')

    #Delete Users
    dir_name = "users/"
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".txt"):
            os.remove(os.path.join(dir_name, item))
    print('User Account Files Deleted')

    #Delete Strongholds
    dir_name = "strongholds/"
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".txt"):
            os.remove(os.path.join(dir_name, item))
    print('User Strongholds Deleted')

    #Rewrite/Initialize settings.txt
    try:
        with open('settings.txt', 'r+') as settingsFile:
            print('Opened settings.txt')

            print('Attempting to write over file')
            settingsFile.truncate() 
            settingsFile.write('Map Initialized: no')
            print('Server Settings Initialized')

            settingsFile.close()
    except:
        print('settings.txt rewrite did not succeed')

    #Truncate serverMap.txt
    try:
        with open('map/serverMap.txt', 'r+') as mapFile:
            print('Opened settings.txt')

            mapFile.truncate() 
            mapFile.close()
            print('Server Map Truncated')
    except:
        print('serverMap.txt rewrite did not succeed')

    #Truncate serverMarket.txt
    try:
        with open('market/serverMarket.txt', 'r+') as marketFile:
            print('Opened marketFile.txt')

            marketFile.truncate() 
            marketFile.close()
            print('Market File Truncated')
    except:
        print('marketFile.txt rewrite did not succeed')

    #Truncate chatlog.log
    try:
        with open('chatlog.log', 'r+') as chatFile:
            print('Opened marketFile.txt')

            chatFile.truncate() 
            chatFile.close()
            print('Chat Log Truncated')
    except:
        print('Chat Log rewrite did not succeed')

    print('\nDelete Complete. Your server is now ready to go!\n')
    throwaway = input('Press Enter To Contiue:\n')

if answer != 'y':
    print('Aborting Reset Process')
    throwaway = input('Press Enter To Contiue:\n')
