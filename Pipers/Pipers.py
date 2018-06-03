# This is my project called: Pipers
# Created by Marshal Studio
# This is a total coommand line interface game

from Place import *
from Piper import *
from Power import *
from Character import *

#All the objects that I created at the start

#All the powers
Masturbate= Power("Masturbate",1000,1)
Suckowndick= Power("Suck",10,1)
Fireball=Power("Power",250,1)

#All the pipers
X=Piper("XiaoHuoHou","Fire",1,110,[Masturbate],100,100,100,100,100)
B=Piper("BuBu","Plant",1,100,[Suckowndick],90,90,111,109,99)
Y=Piper("YiYou","Water",1,90,[Fireball],110,110,90,90,110)


#All the places

Mars=Place("Mars",X,B,0.05,B,[])
Earth=Place("Earth",B,X,0.01,X,[Mars])
Vinus=Place("Vinus",B,X,0.1,B,[Earth,Mars])
Mercury=Place("Mercury",B,X,0.2,B,[Mars,Vinus,Earth])
Mars.add_Connected_Place(Mercury)
Earth.add_Connected_Place(Vinus)
name=str(input("Please enter your name:"))
Main=Character(name,[],0,[],Mercury)




def initialisation():
    quit= False
    print("Hi!"+name+", Welcome to Pipers, the game created by Marshal")
    print("You can choose between three Pipers from the start")
    X.print_detail()
    B.print_detail()
    Y.print_detail()
    while True:
        First=(str(input("Please enter your option:"))).lower()
        if First=="xiaohuohou":
            Main.add_Piper(X)
            break
        elif First=="bubu":
            Main.add_Piper(B)
            break
        elif First=="yiyou":
            Main.add_Piper(Y)
            break
        else:
            continue
        
    while quit==False:
        Choose_Option(Main.get_Position())
        

def str_to_piper(List,Str):      #Convert the name of the piper to the object
    for i in range(len(List)):
        if List[i].get_name()==Str:
            return List[i]
        
        
def Choose_Option(place):
    place.print_details()
    Option=(input("Choose between Fight or Leave:")).title()
    if Option=="Fight":
        print(place.get_pipers_str())
        valid=False
            
        while valid==False:
            opponent_piper_str=str(input("Aginst which piper:"))
            if opponent_piper_str in place.get_pipers_str():
                (Main.get_Pipers())[0].fight_against(str_to_piper(place.get_pipers(),opponent_piper_str))
                valid=True
        Choose_Option(place)

    

    
                                                                       
                        
    elif Option=="Leave": 
        print("Possible location to go into:")
        print(place.get_places_str())
        while True:
            Target_place=str(input("Enter the name of the place you want to go:"))
            if Target_place in place.get_places_str():
                break
            else:
                continue
        for i in range(len(place.get_places_str())):
                    if (place.get_places_str())[i]==Target_place:
                        Main.set_Position(place.get_Connected_Place()[i])
    
    
        
initialisation()


    
    
    
    
    
    
