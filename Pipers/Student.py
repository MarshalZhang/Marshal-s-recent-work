import random
import numpy as np

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
    r=np.random.normal(loc=0.0,scale=1.0,size=None)
    return r*sd+average

def cal_talent(list_6,person_6):
    sum1=sum(list_6)
    sum2=sum(person_6)
    
    if sum1>=14.1*1.6449+sum2:
        return "Study God"  #Top 5%
    elif sum1>=14.1*0.84162+sum2:
        return "Stduy King"  #Top 20%
    elif sum1>=sum2-14.1*0.25335:
        return "Study Soso"   #Top 60%
    elif sum1>=sum2-14.1*1.6449:
        return "Study Bad"   #Top 95%
    else:
        return "Better given up"

    
class Student():
    def __init__(self,name,person,xp,current6):
        self.__name=name
        self.__person=person    
        self.__diploma=cal_diploma(xp)
        self.__xp=xp
        self.__xp_left=cal_xp_left(xp)
        self.__current6=current6
        self.__hp=current6[0]
        self.__EQ=current6[1]
        self.__IQ=current6[2]
        self.__ED=current6[3]
        self.__ID=current6[4]
        self.__speed=current6[5]
        self.__current_powers=[]
        
        self.__this6_growth=[]      #This student's growth
        for growth in self.__person.get_growth():
            self.__this6_growth.append(normal_generate(growth,10))

        self.__talent=cal_talent(self.__this6_growth,self.__person.get_growth())

    def get_talent(self):
        return self.__talent

    def get_name(self):
        return self.__name

    def set_name(name):
        self.__name=name

    def get_diploma(self):
        return self.__diploma

    def get_xp(self):
        return self.__xp

    def Inc_xp(self,inc):      #Gain xp from fighting
        print("You have gained:"+str(inc)+"XP")
        left=cal_xp_left(self.__xp)
        while inc>=left:
            self.diploma_up()
            self.__xp+=cal_xp_left(self.__xp)
            inc-=cal_xp_left(self.__xp)       #Fix this tomorrow
            left=cal_xp_left(self.__xp)
        self.__xp+=inc
        print(self.__name+" is now in diploma "+self.__diploma)    #This def is in charge of gain in xp
        print("XP required to next grade:",str(cal_xp_left(self.__xp)))

    def diploma_up(self):
        print("Congrats, "+self.__name+" has been up'graded', increased value:")
        l=[]
        int_list=[]
        for i in(self.__this6_growth):
            l.append(normal_generate(i,3))
        for i in l:
            int_list.append(int(i))
        print(int_list)
        for i in range(6):
            self.__current6[i]+=l[i]
        self.__diploma=diploma_list[diploma_list.index(self.__diploma)+1]

    def get_hp(self):
        return self.__hp

    def set_hp(hp):
        self.__hp=hp
        self.__current6[0]=hp

    def get_powers(self):
        return self.__current_powers

    def get_hp(self):
        return self.__hp

    def get_IQ(self):
        return self.__IQ

    def get_EQ(self):
        return self.__EQ

    def get_ID(self):
        return self.__ID

    def get_ED(self):
        return self.__ED

    def get_speed(self):
        return self.__speed

    def print_detail(self):
        print("Name:"+self.__name+" Diploma:"+str(self.__diploma)+" Major:"+self.__person.get_major()+" Talent:"+self.__talent)

    def fight_against(self,opponent_student):  
        print("You are using:" +self.__name+" to fight against "+opponent_student.get_name())
        my_speed=self.__speed
        my_damage=(self.__EQ*self.__IQ/opponent_student.get_ED())/10
        my_hp=self.__hp
        opp_speed=opponent_student.get_speed()
        opp_damage=((opponent_student.get_IQ())*(opponent_student.get_EQ())/self.__ED)/10
        opp_hp=opponent_student.get_hp()

        fight_finished=False
        
        while fight_finished==False and my_hp>0 and opp_hp>0:
            if my_speed>opp_speed:
                d=normal_generate(my_damage,3)
                print(self.__name+" attacts "+opponent_student.get_name()+", dealing a damage of:"+str(int(d)))
                opp_hp-=d
                opp_speed+=opponent_student.get_speed()
                
            else:
                d=normal_generate(opp_damage,3)
                print(self.__name+" is attackted by "+opponent_student.get_name()+", undertaking a damge of:"+str(int(d)))
                my_hp-=d
                my_speed+=self.__speed
                    
        if my_hp<=0:
            print(self.__name+" have been beaten by:"+opponent_student.get_name())
        elif opp_hp<=0:
            print(self.__name+" have beaten:"+ opponent_student.get_name())
            self.Inc_xp(opponent_student.get_xp()/10)
            


