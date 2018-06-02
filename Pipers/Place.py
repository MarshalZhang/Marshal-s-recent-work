import random
class Place():
    def __init__(self,name,Piper,Rare_piper,Rare_piper_p,boss,Connected_Place):
        self.__name=name
        self.__Piper=Piper
        self.__Rare_piper=Rare_piper
        self.__Rare_piper_p=Rare_piper_p
        self.__pipers=[Piper,boss]
        self.__pipers_str=[]  #The str format of all the pipers in the map
        self.__boss=boss
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

    def set_name(name):
        self.__name=name
        dict["Name"]=name

    def set_Piper(Piper):
        self.__Piper=Piper
        dict["Common piper"]=Piper

    def set_Rare_piper(Rare_piper):
        self.__Rare_piper=Rare_piper

    def set_Rare_piper_p(Rare_piper_p):
        self.__Rare_piper_p=Rare_piper_p

    def set_boss(boss):
        self.__boss=boss
        dict["Boss"]=boss

    def add_Connected_Place(Place):
        self.__Connected_Place.append(Place)

    def remove_Connected_Place(Place):
        while Place in self.__Connected_Place:
            self.__Connected_Place.remove(Place)

    def print_details(self):
        print("You are currently at:"+self.__name)
        for key,value in self.__dict.items():
            if key=="Name":
                print("Name of the planet:"+value)
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
            
    
    def Choose_Option(self):
        self.print_details()
        Option=(input("Choose between Fight or Leave:")).lower()
        if Option=="fight":
            print("Aginst which piper:")
            print(self.__pipers_str)
            
        elif Option=="leave": 
            print("Possible location to go into:")
            print(self.__places_str)
            while True:
                Target_place=str(input("Enter the name of the place you want to go:"))
                if Target_place in self.__places_str:
                    for i in range(len(self.__places_str)):
                        if self.__places_str[i]==Target_place:
                            return self.__Connected_Place[i]
                else:
                    continue
                    
            
                
                
                

        

        
            
        
        



