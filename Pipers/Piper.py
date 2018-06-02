
XP_Level_list=[]
for i in range(100):
    XP_Level_list.append(i*(i+1))
    
def cal_lv(xp):
    lv=0
    while XP_Level_list[lv]<xp and lv<100:
        lv+=1

    return lv
    
def cal_xp_left(lv,xp):
    if lv==99:
        return(999999)
    else:
        return XP_Level_list[lv+1]-xp
    
        


class Piper():
    def __init__(self,name,xi,xp,hp,powers,pugong,tegong,pufang,tefang,speed):
        self.__name=name
        self.__xi=xi      #one of "water","plant","fire"
        self.__lv=cal_lv(xp)
        self.__xp=xp
        self.__xp_left=cal_xp_left(cal_lv(xp),xp)
        self.__hp=hp
        self.__powers=powers
        self.__quaility=""      #Common,Rare,Epic, Lengendary
        self.__powers_str=[]       #The string format of current power
        for p in powers:
            self.__powers_str.append(p.get_name())
        self.__pugong=pugong
        self.__tegong=tegong
        self.__pufang=pufang
        self.__tefang=tefang
        self.__speed=speed
        

    def get_name(self):
        return self.__name

    def set_name(name):
        self.__name=name

    def get_xi(self):
        return self.__xi
    
    def set_xi(xi):
        self.__xi=xi

    def get_lv(self):
        return self.__lv

    def set_lv(lv):
        self.__lv=lv

    def Inc_xp(inc):
        print("You have gained:"+inc+"XP")    #This def is in charge of gain in xp
        self.__xp+=inc
        if inc>=self.__xp_left:
            print("Congrat Lv. up")
        
    def get_hp(self):
        return self.__hp

    def set_hp(hp):
        self.__hp=hp

    def get_powers(self):
        return self.__powers

    def set_powers(powers):
        self.__powers=powers

    def print_detail(self):
        print("Name:"+self.__name+" XI:"+self.__xi+" Hp:"+str(self.__hp))
