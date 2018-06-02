import random

class Place():         # Place is a subclass of Map
    def __init__(self,name,Piper,Rare_piper,Rare_piper_p,boss,Connected_Place):
        self.__name=name
        self.__Piper=Piper
        self.__Rare_piper=Rare_piper
        self.__Rare_piper_p=Rare_piper_p
        self.__pipers=[Piper,boss]
        self.__pipers_str=[]  #The str format of all the pipers in the map
        
        self.__boss=boss      #The dic contains all the information
        self.__dict={"Name":name,"Common piper":Piper,"Boss":boss,"Connected place":Connected_Place}
        if random.random()<Rare_piper_p:
            self.__dict["Rare piper"]=Rare_piper
            self.__pipers.append(Rare_piper)
            
        self.__Connected_Place=Connected_Place   #Connected_Place is a list
        for p in self.__pipers:
            self.__pipers_str.append(p.get_name())
        self.__places_str=[]    # The str format of all the places we can go
        for p in Connected_Place:
            self.__places_str.append(p.get_name())
        
        
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

    def get_dict(self):
        return self.__dict

    def get_Connected_Place(self):
        return self.__Connected_Place          #this one also return a list

    def get_pipers_str(self):
        return self.__pipers_str

    def get_pipers(self):
        return self.__pipers

    def get_places_str(self):
        return self.__places_str

    def set_name(self,name):
        self.__name=name
        dict["Name"]=name

    def set_Piper(self,Piper):
        self.__Piper=Piper
        dict["Common piper"]=Piper

    def set_Rare_piper(self,Rare_piper):
        self.__Rare_piper=Rare_piper

    def set_Rare_piper_p(self,Rare_piper_p):
        self.__Rare_piper_p=Rare_piper_p

    def set_boss(self,boss):
        self.__boss=boss
        dict["Boss"]=boss

    def add_Connected_Place(self,Place):
        self.__Connected_Place.append(Place)
        self.__places_str.append(Place.get_name())

    def remove_Connected_Place(self,Place):
        while Place in self.__Connected_Place:
            self.__Connected_Place.remove(Place)

    def print_details(self):
        for key,value in self.__dict.items():
            if key=="Name":
                print("Current planet:"+value)
            elif key=="Common piper":
                print("Common piper:"+value.get_name())
            elif key=="Boss":
                print("Boss:"+value.get_name())
            elif key=="Rare piper":
                print("Rare piper:'"+value.get_name()+"' occurs")

            elif key=="Connected_Place":
                names=[]
                for p in value:
                    names.append(p.get_name())
                print("Places that you can go to:")
                print(names)
            
    


        



