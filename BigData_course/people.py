class Person:

    def __init__(self, name, age, dpt):
        self.name=name
        self.age=age
        self.dpt=dpt
    
    def get_name(self):
        return self.name
        
        
class Student(Person):
    def __init__(self, name, age, dpt, identifier, gpa):
        Person.__init__(self, name=name,age=age,dpt=dpt)
        self.identifier = identifier
        self.gpa = gpa
    
    def print_info(self):
        print("'제 이름은 %s, 나이는 %d, 학과는 %s, 지도교수님은 %s 입니다'"
             %(self.get_name(), self.age, self.dpt, self.reg_advisor_name))
        return
        
    def reg_advisor(self, pName):
        # pName이 Professor객체로 전달되기 때문에
        # professor의 상위 클래스인 Person에 있는 get_name()을 사용해서
        # 이름만 가져와서 저장한다.
        self.reg_advisor_name=pName.get_name()
        return

    
class Professor(Person):
    reg_student_names=[]
    
    def __init__(self, name, age, dpt, position,laboratory):
        Person.__init__(self, name=name, age=age, dpt=dpt)
        self.position = position
        self.laboratory = laboratory
              
      
    def print_info(self):
        
        #저장된 담당 학생 리스트에서 학생이름을 가져와 문자열을 생성한다.
        students=str(self.reg_student_names[0])
        for s in self.reg_student_names[1:]:
              students+=", %s"%s
              
        print("'제 이름은 %s, 나이는 %d, 학과는 %s, 지도학생은 %s 입니다'"
             %(self.get_name(), self.age, self.dpt, students))
        return
    
    def reg_student(self, sName):
        # sName이 Student객체로 전달되기 때문에
        # student의 상위 클래스인 Person에 있는 get_name()을 사용해서
        # 이름만 가져와서 담당 학생 리스트에 append한다.
        self.reg_student_names.append(sName.get_name())
        return

def main():
    stu1 =Student('kim',30,'Computer',20001234, 4.5)
    stu2 = Student('Lee', 22, 'Computer', 20101234, 0.5)
    prof1 = Professor('Lee', 55, 'Computer', 'Full', 'KLE')

    stu1.reg_advisor(prof1)
    stu2.reg_advisor(prof1)

    prof1.reg_student(stu1)
    prof1.reg_student(stu2)

    stu1.print_info()
    stu2.print_info()
    prof1.print_info()


if __name__ == '__main__':
    main()
