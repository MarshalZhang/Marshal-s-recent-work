import random

class Place():  
    def __init__(self,name,student,rare_student,rare_student_p,professor,connected_place):
        self.__name=name
        self.__student=student
        self.__rare_student=rare_student
        self.__rare_student_p=rare_student_p
        self.__students=[]
        self.__students_str=[]  #The str format of all the students in the map
        
        self.__professor=professor      #The dic contains all the information
        self.__dict={}
            
        self.__connected_place=connected_place   #connected_place is a list
        
        self.__places_str=[]    # The str format of all the places we can go
        for p in connected_place:
            self.__places_str.append(p.get_name())
        
        
    def get_name(self):   
        return self.__name

    def get_student(self):
        return self.__student

    def get_rare_student(self):
        return self.__rare_student

    def get_rare_student_p(self):
        return self.__rare_student_p

    def get_professor(self):
        return self.__professor

    def get_dict(self):
        return self.__dict

    def get_connected_place(self):
        return self.__connected_place          #this one also return a list

    def get_students_str(self):
        return self.__students_str

    def get_students(self):
        return self.__students

    def get_places_str(self):
        return self.__places_str

    def update_rare(self):            #Update the scence
        self.__students=[self.__student,self.__professor]
        self.__dict={}
        self.__dict["Name"]=self.__name
        self.__dict["Common student"]=self.__student
        self.__dict["Professor"]=self.__professor
        self.__dict["Connected place"]=self.__connected_place
        self.__students_str=[]

        if random.random()<self.__rare_student_p:
            self.__dict["Rare student"]=self.__rare_student
            self.__students.append(self.__rare_student)
        for p in self.__students:
            self.__students_str.append(p.get_name())

    def set_name(self,name):
        self.__name=name
        dict["Name"]=name

    def set_student(self,student):
        self.__student=student
        dict["Common student"]=student

    def set_rare_student(self,rare_student):
        self.__rare_student=rare_student

    def set_rare_student_p(self,rare_student_p):
        self.__rare_student_p=rare_student_p

    def set_professor(self,professor):
        self.__professor=professor
        dict["Professor"]=professor

    def add_connected_place(self,place):
        self.__connected_place.append(place)
        self.__places_str.append(place.get_name())

    def remove_connected_place(self,place):
        while place in self.__connected_place:
            self.__connected_place.remove(place)

    def print_details(self):
        for key,value in self.__dict.items():
            if key=="Name":
                print("Current position:"+value)
            elif key=="Common student":
                print("Common student:"+value.get_name())
            elif key=="Professor":
                print("Professor:"+value.get_name())
            elif key=="Rare student":
                print("Rare student:'"+value.get_name()+"' occurs")

            elif key=="Connected_Place":
                names=[]
                for p in value:
                    names.append(p.get_name())
                print("Places that you can go to:")
                print(names)
            
    


        



