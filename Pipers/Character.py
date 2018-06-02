class Character():
    def __init__(self,name,Pipers,Money,Tools,Position):
        self.__name=name
        self.__Pipers=Pipers
        self.__Money=Money
        self.__Tools=[]
        self.__Pipers_str=[]
        self.__Position=Position
        for p in Pipers:
            self.__Pipers_str.append(p.get_name())

    def get_Pipers(self):
        return self.__Pipers

    def add_Piper(self,Piper):
        self.__Pipers.append(Piper)
        self.__Pipers_str.append(Piper.get_name())

    def get_Pipers_str(self):
        self.__Pipers_str

    def get_Position(self):
        return self.__Position

    def exchange_position(self,a,b):
        Temp=self.__Pipers[a]
        self.__Pipers[a]=self.__Pipers[b]
        self.__Pipers[b]=Temp

    def get_money(self):
        return self.__Money

    def inc_money(self,gain):
        self.__money+=gain

    def set_Position(self,p):
        self.__Position=p






    
