import random

XP_Level_list=[]     #XP upgarde table
for i in range(25):
    XP_Level_list.append(i*(i+1))
diploma_list=["Kindergarten 1","Kindergarten 2","Kindergarten 3","Primary 1","Primary 2",
              "Primary 3","Primary 4","Primary 5","Primary 6","Junior High 1","Junior High 2",
              "Junior High 3","Senior High 1", "Senior High 2","Senior High 3","Freshman year1",
              "Sophomore year2","Junior year 3","Senior Year 4","Masters Level 1",
              "Master Level 2","Master Level 3","PhD Level 1","PhD Level 2","PhD Level 3"]
    
def cal_diploma(xp):
    i=0
    while XP_Level_list[i]<xp and i<24:
        i+=1
        
    return diploma_list[i]
    
def cal_xp_left(xp):
    if xp>XP_Level_list[24]:
        return(999999)
    else:
        i=0
        while xp>=XP_Level_list[i]:
            i+=1
        return XP_Level_list[i]-xp

def majors_attact(a, b):    # a and b are two majors(str)
    # a attact b, this def return the coeffieint of major attact
    # Majors=[Math, Physics, Engineer, Philosophy,Biologay, Chemistry, CS]
    if a=="Math":
        if b=="Physic" or b=="Engineers":
            return 1.4
        if b=="Biology":
            return 0.7
        if b=="Chemistry":
            return 0.85

    elif a=="Chemistry":
        if b=="Biology":
            return 1.4
        if b=="CS":
            return 0.7

    elif a=="CS":             #CS can solve engineering problem and Organic structure
        if b=="Chemistry" or b=="Engineer":
            return 1.4
        if b=="Physics":
            return 0.85

    elif a=="Philosophy":
        return 1.2

    elif a=="Engineer":
        if b=="Physics" or b=="Math":
            return 0.8

def normal_generate(average, sd):
    n=average+((random.random()-0.5)*sd)
    return n


class Person():       #Person defines the talent of the person (prototype)
    def __init__(self,name,major,initial,powers,hpg,EQg,IQg,QDg,IDg,speedg):#g stand for growth
        self.__name=name
        self.__major=major
        self.__initial=intial       # The intial 
        self.__powers=powers
        self.__hpi=0.00
        self.__EQi=0.00
        self.__IQi=0.00
        self.__QDi=0.00
        self.__IDi=0.00
        self.__speedi=0.00
        self.__hpg=hpg
        self.__EQg=EQg
        self.__IQg=IQg
        self.__QDg=QDg
        self.__IDg=IDg
        self.__speedg=speedg

    def get_initial_6(self):   #define the initial 6 of the person
        average=self.__intial/6
        self.__hpi=normal_generate(average, 5)
        self.__EQi=normal_generate(average, 5)
        self.__IQi=normal_generate(average, 5)
        self.__QDi=normal_generate(average, 5)
        self.__IDi=normal_generate(average, 5)
        
    def get_talent(self):
        q=hpg


    
class Student():
    def __init__(self,name,person,xp,hp,powers,EQ,IQ,QD,ID,speed):
        self.__name=name
        self.__person=person
        self.__major=major     
        self.__diploma=cal_diploma(xp)
        self.__xp=xp
        self.__xp_left=cal_xp_left(xp)
        self.__hp=hp
        self.__powers=powers
        self.__quaility=""      #Common,Rare,Epic, Lengendary
        self.__powers_str=[]       #The string format of current power
        for p in powers:
            self.__powers_str.append(p.get_name())
        self.__EQ=EQ
        self.__IQ=IQ
        self.__QD=QD
        self.__ID=ID
        self.__speed=speed
        

    def get_name(self):
        return self.__name

    def set_name(name):
        self.__name=name

    def get_major(self):
        return self.__major
    
    def set_major(major):
        self.__major=major

    def get_diploma(self):
        return self.__diploma

    def set_diploma(diploma):
        self.__diploma=diploma

    def get_xp(self):
        return self.__xp

    def Inc_xp(self,inc):      #Gain xp from fighting
        self.__xp+=inc
        self.__diploma=cal_diploma(self.__xp)
        print("You have gained:"+str(inc)+"XP"+", and is now in diploma "+self.__diploma)    #This def is in charge of gain in xp
        print("XP required to next grade:",str(cal_xp_left(self.__xp)))
        
    def get_hp(self):
        return self.__hp

    def set_hp(hp):
        self.__hp=hp

    def get_powers(self):
        return self.__powers

    def set_powers(powers):
        self.__powers=powers

    def print_detail(self):
        print("Name:"+self.__name+" Diploma:"+str(self.__diploma)+" Major:"+self.__major+" Hp:"+str(self.__hp))

    def fight_against(self,opponent_student):   #Huge work later to change this
        print("You are using:" +self.__name+" to fight against "+opponent_student.get_name())
        if self.__hp>opponent_student.get_hp():
            print(self.__name+" have beaten:"+ opponent_student.get_name())
            self.Inc_xp(opponent_student.get_xp()/10)
        else:
            print(self.__name+" have been beaten by:"+opponent_student.get_name())
