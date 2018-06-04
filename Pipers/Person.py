import random

def normal_generate(average, sd):  #Change later, I forget the algorithm
    n=average+((random.random()-0.5)*sd)
    return n


class Person():       #Person defines the talent of the person (prototype)
    def __init__(self,name,major,initial,powers,hpg,EQg,IQg,QDg,IDg,speedg):#g stand for growth
        self.__name=name
        self.__major=major
        self.__initial=initial       # The intial 
        self.__powers=powers
        #The initial 6
        self.__hpi=0.00
        self.__EQi=0.00
        self.__IQi=0.00
        self.__QDi=0.00
        self.__IDi=0.00
        self.__speedi=0.00
        #The growth of 6
        self.__growth=[hpg,EQg,IQg,QDg,IDg,speedg]
        self.__hpg=hpg
        self.__EQg=EQg
        self.__IQg=IQg
        self.__QDg=QDg
        self.__IDg=IDg
        self.__speedg=speedg

    def get_initial_6(self):   #define the initial 6 of the person
        initial_6=[]       #Stores the initial6 of the person
        average=self.__intial/6
        self.__hpi=normal_generate(average, 5)
        initial_6.append(self.__hpi)
        self.__EQi=normal_generate(average, 5)
        initial_6.append(self.__EQi)
        self.__IQi=normal_generate(average, 5)
        initial_6.append(self.__IQi)
        self.__QDi=normal_generate(average, 5)
        initial_6.append(self.__QDi)
        self.__IDi=normal_generate(average, 5)
        initial_6.append(self.__IDi)
        self.__speedi=normal_generate(average,5)
        initial_6.append(sefl.__speedi)
        return initial_6

    def get_name(self):
        return self.__name

    def get_major(self):
        return self.__major

    def get_powers(self):
        return self.__powers

    def get_growth(self):
        return self.__growth
    


