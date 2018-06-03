
XP_Level_list=[]     #XP upgarde table
for i in range(100):
    XP_Level_list.append(i*(i+1))
    
def cal_diploma(xp):
    diploma=0
    while XP_Level_list[diploma]<xp and diploma<100:
        diploma+=1

    return diploma
    
def cal_xp_left(diploma,xp):
    if diploma==99:
        return(999999)
    else:
        return XP_Level_list[diploma+1]-xp
    
        


class Student():
    def __init__(self,name,major,xp,hp,powers,EQ,IQ,QD,ID,speed):
        self.__name=name
        self.__major=major      #one of "water","plant","fire"
        self.__diploma=cal_diploma(xp)
        self.__xp=xp
        self.__xp_left=cal_xp_left(cal_diploma(xp),xp)
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

    def Inc_xp(self,inc):      #Gain xp from fighting
        print("You have gained:"+str(inc)+"XP"+", Now it has "+str(self.__xp)+" XP overall")    #This def is in charge of gain in xp
        self.__xp+=inc
        self.__diploma=cal_diploma(self.__xp)
        
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
            self.Inc_xp(opponent_student.get_diploma())
        else:
            print(self.__name+" have been beaten by:"+opponent_student.get_name())
