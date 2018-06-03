class Character():
    def __init__(self,name,students,Money,Tools,Position):
        self.__name=name
        self.__students=students
        self.__Money=Money
        self.__Tools=[]
        self.__students_str=[]
        self.__Position=Position
        for p in students:
            self.__students_str.append(p.get_name())

    def get_students(self):
        return self.__students

    def add_student(self,student):
        self.__students.append(student)
        self.__students_str.append(student.get_name())

    def display_students(self):
        print("Your study group:")
        for s in self.__students:
            s.print_detail()

    def get_students_str(self):
        self.__students_str

    def get_Position(self):
        return self.__Position

    def exchange_position(self,a,b):
        Temp=self.__students[a]
        self.__students[a]=self.__students[b]
        self.__students[b]=Temp

    def get_money(self):
        return self.__Money

    def inc_money(self,gain):
        self.__money+=gain

    def set_Position(self,p):
        self.__Position=p






    
