# This is my project called: Pipers
# Created by Marshal Studio
# This is a total coommand line interface game

from Place import *



class Piper():
    def __init__(self,name,hp, max_hp, powers,growence):
        self.__name=name
        self.__hp= hp
        self.__max_hp=max_hp
        self.__powers=powers
        self.__growence=growence
        self.__attribute=''

    def get_name(self):
        return self.__name

    def set_name(name):
        self.__name=name

    def get_hp(self):
        return self.__hp

    def set_hp(hp):
        self.__hp=hp

    def get_max_hp(self):
        return self.__max_hp

    def get_powers(self):
        return self.__powers

    def set_powers(powers):
        self.__powers=powers

    def print_detail(self):
        print("Name:"+self.__name+" Current hp:"+str(self.__hp)+" Max_hp:"+str(self.__max_hp)+" Power:"+self.__powers.get_name())


        
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
Mars=Place("Mars",Rex,Marshal,0.05,Marshal,[])
Earth=Place("Earth",Marshal,Rex,0.9,Rex,[Mars])
Place_list=[Mars,Earth]       # This list stores all the placed in the game

def displayPipers(Pipers):
    for Piper in Pipers:
        Piper.print_detail()

def initialisation():
    Pipers=[]          #This list stores all the pipers the player have
    quit= False
    print("Welcome to Pipers, the game created by Marshal")
    print("You can choose between three Pipers from the start")
    Marshal.print_detail()
    Rex.print_detail()
    First=(str(input("Please enter your option:"))).lower()
    if First=="marshal":
        Pipers.append(Marshal)
    elif First=="rex":
        Pipers.append(Rex)
    displayPipers(Pipers)
    New=Earth
    while quit==False:
        New=New.Choose_Option()
        
        

        
    
    
        
initialisation()


    
    
    
    
    
    
