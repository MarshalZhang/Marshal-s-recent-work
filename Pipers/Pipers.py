# This is my project called: Pipers
# Created by Marshal Studio
# This is a total coommand line interface game

from Place import *
from Piper import *
from Power import *

#All the objects that I created at the start

Masturbate= Power("Masturbate",1000,1)           
X= Piper("XiaoHuoHou","Fire",100,100,[Masturbate],100,100,100,100,100)
Suckowndick= Power("Suck",10,1)
B=Piper("Bubu","Plant",1,100,[Suckowndick],10,10,10,10,10)
Mars=Place("Mars",X,B,0.05,B,[])
Earth=Place("Earth",B,X,0.9,X,[Mars])
Place_list=[Mars,Earth]       # This list stores all the placed in the game

def displayPipers(Pipers):
    for Piper in Pipers:
        Piper.print_detail()

def Fight(a,b):# a is own piper and b is opponent piper
    print("You are using:" + a.get_name()+"to fight with"+b.get_name())

def initialisation():
    Pipers=[]          #This list stores all the pipers the player have
    quit= False
    print("Welcome to Pipers, the game created by Marshal")
    print("You can choose between three Pipers from the start")
    X.print_detail()
    B.print_detail()
    First=(str(input("Please enter your option:"))).lower()
    if First=="XiaoHuoHou":
        Pipers.append(X)
    elif First=="BuBuZhongZi":
        Pipers.append(B)
    displayPipers(Pipers)
    New=Earth
    while quit==False:
        New=New.Choose_Option()
        
        

        
    
    
        
initialisation()


    
    
    
    
    
    
