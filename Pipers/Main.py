# This is my project called: students
# Created by Marshal Studio
# This is a total coommand line interface game

from Place import *
from Student import *
from Power import *
from Character import *

#All the objects that I created at the start

#All the powers
Masturbate= Power("Masturbate",1000,1)
Suckowndick= Power("Suck",10,1)
Fireball=Power("Power",250,1)

#All the students
M=Student("Marshal","Physics",1,110,[Masturbate],100,100,100,100,100)
K=Student("Kevin","Engineering",10,100,[Suckowndick],90,90,111,109,99)
R=Student("Rex","Math",10,90,[Fireball],110,110,90,90,110)


#All the places

Cambridge=Place("Cambridge",M,K,0.05,R,[])
Madison=Place("Madison",R,K,0.01,M,[Cambridge])
Waterloo=Place("Waterloo",M,R,0.1,K,[Madison,Cambridge])
ICC=Place("ICC",K,M,0.2,R,[Cambridge,Waterloo,Madison])
Cambridge.add_connected_place(ICC)
Madison.add_connected_place(Waterloo)
name=str(input("Please enter your name:"))
Main=Character(name,[],0,[],ICC)




def initialisation():
    quit= False
    print("Hi!"+name+", Welcome to students, the game created by Marshal")
    print("You can choose between three students from the start")
    M.print_detail()
    R.print_detail()
    K.print_detail()
    while True:
        First=(str(input("Please enter your option:"))).lower()
        if First=="marshal":
            Main.add_student(M)
            break
        elif First=="rex":
            Main.add_student(R)
            break
        elif First=="kevin":
            Main.add_student(K)
            break
        else:
            continue
        
    while quit==False:
        Choose_Option(Main.get_Position())
        

def str_to_student(List,Str):      #Convert the name of the student to the object
    for i in range(len(List)):
        if List[i].get_name()==Str:
            return List[i]
        
        
def Choose_Option(place):
    place.update_rare()
    place.print_details()
    Option=(input("Choose between Fight or Leave:")).title()
    if Option=="Fight":
        Main.display_students()
        print(place.get_students_str())
        valid=False
            
        while valid==False:
            opponent_student_str=str(input("Aginst which student:"))
            if opponent_student_str in place.get_students_str():
                (Main.get_students())[0].fight_against(str_to_student(place.get_students(),opponent_student_str))
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


    
    
    
    
    
    
