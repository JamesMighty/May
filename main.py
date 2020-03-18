# -*- coding: utf-8 -*-
import os
import sys
import random
import re
from command import node
from nodeThree import Three
from utility import any_common, text_edit, TTS

def logo():
    print()
    print("                                                     @@@@    @@@   @@@#  @@@@   @@@@. @@@@    @@@@ &@@@@@@@@@  @@@@     ")
    print("                                                     @@@@@(  @@@   @@@#  @@@@ @@@@/    @@@    @@@  &@@@        @@@@     ")
    print("                                                     @@@@@@@ @@@   @@@#  @@@@@@@@.     &@@@  @@@   &@@@@@@@@&  @@@@     ")
    print("                                                     @@@@ @@@@@@   @@@#  @@@@@&@@@%     @@@/&@@@   &@@@        @@@@     ")
    print("                                                     @@@@  @@@@@   @@@#  @@@@   @@@@     @@@@@@    &@@@,,,,,,  @@@@@@@@@")
    print("                                                     @@@@   *@@@   @@@#  @@@@    @@@@     @@@@     &@@@@@@@@@  @@@@@@@@@")
    print("__________________________________________________________________________________________________________________________________________________________________________")
"""
def comands (text):
    text_cp = text
    text = text_edit(text)
    
    errors = ["Nerozuměla jsem ti zkus se zeptat jinak",
              "Nevím co po mě chceš!", 
              "Zkus to znovu",
        ]
        
    if (text.find("REKNI") == 0):
        TTS(text_cp.replace("rekni", ""))

    elif (text.find("AHOJ") == 0) or (text.find("NAZDAR") == 0) or (text.find("ZDRAVIM") == 0):
        print("Nikvel>> Ahoj jak se máš?")
        TTS("Ahoj jak se máš?")

    elif ((text.find("MAMSEDOBRE") == 0) or (text.find("MÁMSESKVELE") == 0)):
        print("Nikvel>> Táké se mám dobře")
        TTS("Také se mám dobře")

    elif (text.find("VYPNISE") == 0):
            TTS("Tak se měj, zatím")
            os.system('clear')
            sys.exit()

    elif (text.find("KOLIKJEHODIN") == 0):
            )
            TTS(now.strftime("Je %H hodin a %M minut"))
            
    else: TTS(random.choice(errors))
"""

def Resolve(three, inp=None, allResolvedStrings=[], doCommit=True):
    doPrintUnresolved = True
    resolved = False
    todo = []
    if inp == None:
        inp = text_edit(input("MARI>> "))
    else:
        doPrintUnresolved = False
    for comm in three: 
        matchingStrings = [string for string in comm.Conditions if (string in inp or re.match(string,inp))]
        indexes = [inp.index(string) for string in comm.Conditions if (string in inp or re.match(string,inp))]
        if len(matchingStrings) > 0 and not any_common(matchingStrings,allResolvedStrings):
            inp = comm.Decorator(inp) # mozna se bude nekdy hodit, idk
            todo.append( (min(indexes),comm) )
            resolved = True
            allResolvedStrings+=matchingStrings
            if len(comm.CommandList) > 0:
                todo += Resolve(comm.CommandList,inp,allResolvedStrings, doCommit=False) 

    if len(todo) > 0 and doCommit:
        todo = sorted(todo, key = lambda tuple: tuple[0])
        wholeOutput = "" # sberac
        for comm in todo:
            outp = comm[1].OwnCommand(inp) # vlastni vystup
            wholeOutput += outp
            print(outp)
        TTS(wholeOutput)
            
    if doPrintUnresolved and not resolved:
        print("co?")
    #print(allResolvedStrings)
    return todo
            

while True:
    os.system('clear')
    logo()

    for i in range(10):
        Resolve(Three, None, [])


