# This is my project called: students
# Created by Marshal Studio
# This is a total coommand line interface game

from Place import *
from Student import *
from Power import *
from Character import *
from Person import *

#All the objects that I created at the start

#All the powers
Masturbate= Power("Masturbate","Major",1000,1)
Suckowndick= Power("Suck","Minor",10,1)
Fireball=Power("Power","Emotional",250,1)

#All the persons
Marshal=Person("Marshal","Physics",600,[Masturbate],20,8,20,8,20,20)
Kevin= Person("Kevin","Engineering",600,[Suckowndick],16,16,16,16,16,16)
Rex=Person("Rex","Math",600,[Fireball],21,18,25,15,15,15)


#All the students
M=Student("Marshal",Marshal,1,[200,65,200,75,65,90])
K=Student("Kevin",Kevin,10,[100,100,100,100,100,100])
R=Student("Rex",Rex,90,[120,70,110,80,100,120])


#All the places

Cambridge=Place("Cambridge",M,K,0.05,R,[])
Madison=Place("Madison",R,K,0.01,M,[Cambridge])
Waterloo=Place("Waterloo",M,R,0.1,K,[Madison,Cambridge])
ICC=Place("ICC",K,M,0.2,R,[Cambridge,Waterloo,Madison])
Cambridge.add_connected_place(ICC)
Madison.add_connected_place(Waterloo)

#Initialisation of the character
name="Marshal"
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
                        Main.set_Position(place.get_connected_place()[i])
    
    
        
initialisation()


    
    
    
    
    
    
