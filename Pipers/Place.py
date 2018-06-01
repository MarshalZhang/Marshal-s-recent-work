class Place():
    def __init__(self,name,Piper,Rare_piper,Rare_piper_p,boss,inner_Place):
        self.__name=name
        self.__Piper=Piper
        self.__Rare_piper=Rare_piper
        self.__Rare_piper_p=Rare_piper_p
        self.__inner_Place=[inner_Place]   #Inner_Place is a list

    def get_name(self):
        return self.__name

    def get_Piper(self):
        return self.__Piper

    def get_Rare_piper(self):
        return self.__Rare_piper

    def get_Rare_piper_p(self):
        return self.__Rare_piper_p

    def get_boss(self):
        return self.__boss

    def get_inner_Place(self):
        return self.__inner_Place          #this one also return a list

    def set_name():
        self.__name=name

    def set_Piper(Piper):
        self.__Piper=Piper

    def set_Rare_piper():
        self.__Rare_piper=Rare_piper

    def set_Rare_piper_p():
        self.__Rare_piper_p=Rare_piper_p

    def set_boss():
        self.__boss=boss

    def add_inner_Place(Place):
        self.__inner_Place.append(Place)

    def remove_inner_Place(Place):
        while Place in self.__Inner_Place:
            self.__Inner_Place.remove(Place)
        

    def print_detail(self):
        print(self.__name+" has "+self.__Piper.get_name()+" and rare piper:"+self.__Rare_piper.get_name())

