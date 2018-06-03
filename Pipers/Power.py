class Power():
    def __init__(self,name,damage,diploma):       #The name, damage, diploma defines the power
        self.__name=name
        self.__damage=damage
        self.__diploma=diploma

    def set_name(name):
        self.__name=name

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def set_damage(damage):
        self.__damage=damage
        
    def print_detail(self):
        print("Power_name:"+self.__name+"Power damage:"+self.__damage)
