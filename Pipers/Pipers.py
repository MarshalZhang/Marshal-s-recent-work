# This is my project called: Pipers
# Created by Marshal Studio
# This is a total coommand line interface game

from Place import *

class Userinterface():
    def __init__(self,pipers,transport):
        self.__pipers=pipers

    def get_pipers(self):
        return self.__pipers

    def set_pipers(pipers):
        self.__pipers=pipers

    def get_detail(self):
        return self.__pipers


        

class Piper():
    def __init__(self,name,blood, max_blood, powers,growence):
        self.__name=name
        self.__blood= blood
        self.__max_blood=max_blood
        self.__powers=powers
        self.__growence=growence
        self.__attribute=''

    def get_name(self):
        return self.__name

    def set_name(name):
        self.__name=name

    def get_blood(self):
        return self.__blood

    def set_blood(blood):
        self.__blood=blood

    def get_max_blood(self):
        return self.__max_blood

    def get_powers(self):
        return self.__powers

    def set_powers(powers):
        self.__powers=powers

    def print_detail(self):
        print("Name:"+self.__name+" Current blood:"+str(self.__blood)+" Max_blood:"+str(self.__max_blood)+" Power:"+self.__powers.get_name())


        
class Power():
    def __init__(self,name,damage):
        self.__name=name
        self.__damage=damage

    def set_name(name):
        self.__name=name

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def set_damage(damage):
        self.__damage=damage
        
    def print_detail(self):
        print("Power_name:"+self.__name+"Power damage:"+self.__damage)
        

Masturbate= Power("Masturbate",1000)           
Marshal= Piper("Marshal",100,100,Masturbate,1.2)
Suckowndick= Power("Suck",10)
Rex=Piper("Rex",1,1,Suckowndick,0.9)
Earth=Place(None,None,None,None,None,[])
Mars=Place("Mars",Rex,Marshal,0.05,Marshal,[Earth])
Earth=Place("Earth",Marshal,Rex,0.9,Rex,[Mars])
Place_list=[Mars,Earth]       # This list stores all the placed in the game

def displayPipers(Pipers):
    for Piper in Pipers:
        Piper.print_detail()

def initialisation():
    Pipers=[]          #This list stores all the pipers the player have
    print("Welcome to Pipers, the game created by Marshal")
    print("You can choose between three Pipers from the start")
    Marshal.print_detail()
    Rex.print_detail()
    First=str(input("Please enter your option:"))
    if First=="Marshal":
        Pipers.append(Marshal)
    elif First=="Rex":
        Pipers.append(Rex)
    displayPipers(Pipers)
    chooseOption(Mars)

def chooseOption(place):
    print("You are currently at:")
    place.print_detail()
    Option=input("Choose between fight or go:")
    if Option=="fight":
        print("You are currently fighting with:",place.get_Piper())

    elif Option=="go":
        names=[]
        '''
        for p in place.get_inner_Place():
            names.append(p.get_name())
        
        print("Possible location to go into:"+names)
        '''
        Target_place=str(input("Enter the name of the place you want to go:"))
        for p in Place_list:
            if Target_place==p.get_name():
                chooseOption(p)
            
        
    
    
        
initialisation()


    
    
    
    
    
    
