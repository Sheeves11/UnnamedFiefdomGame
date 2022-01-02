import os
import time
import random

'''

Welcome to the Unnamed Fiefdom Game!

This game was designed and written by
Mike Quain of the University of Arkansas

More info can be found at
github.com/Sheeves11/UnnamedFiefdomGame

'''

#initial screen clear
os.system("clear")

answer = input('Would you like to wipe the server and all user data? (y/n)\n')

if answer == 'y':
    print('Deleting all text files...\n\n')
    os.system("rm *.txt")
    print('Delete Complete\n\n')
    throwaway = input('Press Enter To Contiue:\n')
    pass

if answer != 'y':
    print('Aborting Reset Process')
    throwaway = input('Press Enter To Contiue:\n')
    pass
