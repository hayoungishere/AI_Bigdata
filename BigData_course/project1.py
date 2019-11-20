import sys
import os
import re

class _StudentManageProgram():
    def __init__(self):
        # Constructor Method
        
        self.students=[]
        self.fileOpen()
        self.openFileName=""
            
            
    def calGrade(self,score):
        # method :: 성적을 계산해주는 함수
        # score : 계산하고자하는 mid, fianl의 평균점수
        
        if score>=90 :
            return "A"
        elif score>=80:
            return "B"
        elif score>=70:
            return "C"
        elif score>=60:
            return "D"
        else:
            return "F"
    
    def isNumber(self, inputValue):
        # method :: 입력받은 값이 숫자로만 이루어져 있는지를 확인하는 메소드
        # inputValue : 사용자로부터 입력받은 값
        
        r=re.compile("[a-zA-Z가-힣]+")
        if r.search(inputValue) == None:
            return True
        else:
            return False
        
    def isString(self, inputValue):
        # method :: 입력받은 값이 문자로만 이루어져 있는지를 확인하는 메소드
        # inputValue : 사용자로부터 입력받은 값
        r=re.compile("[0-9]+")
        if r.search(inputValue) == None:
            return True
        else:
            return False        

  
    def fileOpen(self):
        # method :: 파일을 열어 데이터를 멤버 변수에 저장하는 메소드
        
        argv=sys.argv[1:]
        
        # Step 1. 사용자로부터 파일명을 입력받았는지 확인한다.
        # 1-1. 사용자로부터 특정한 파일명을 입력 받은 경우        
        if len(argv)>=1 :    
            self.openFileName=argv[0]
            #self.openFileName="students.txt"
            #print(self.openFileName)
            
        # 1-2. 사용자로부터 특정한 파일명을 입력받지 않은 경우, default 파일인 student.txt에서 데이터를 가져온다.
        else:
            self.openFileName="students.txt"

        # Step 2. 파일이 사용자에 컴퓨터에 존재하는지 확인한다.   
        if os.path.exists(self.openFileName):
            #something

        # Step 3. 파일을 open한다.
            with open(self.openFileName, "r") as student_info:
        
        # Step 4. 파일에 있는 학번, 이름, 중간, 기말 점수를 가져와 평균점수와 학점을 계산해
        #           멤버 변수인 students 리스트에 딕셔너리 형태로 저장한다.
        
                for student in student_info:
                    temp=dict()
                    s=student.split("\t") #tab으로 구분된 데이터를 가져온다.
                    s[-1]=s[-1].replace("\n",'') #마지막 데이터에 붙은 줄바꿈 문자('\n')를 제거한다.

                    temp['id']=s[0]; temp['name']=s[1]; temp['mid']=int(s[2]); temp['final']=int(s[3])
                    temp['average']=(int(temp['mid'])+int(temp['final']))/2
                    temp['grade']=self.calGrade(temp['average'])
                    self.students.append(temp)
            
        # Step 5. 파일에서 읽어온 데이터를 출력한다.
            self.show_student_list()
                
        else:
            print("입력하신 파일이 존재하지 않습니다. 기본파일을 열겠습니다.")
            self.openFileName="students.txt"
            with open(self.openFileName, "r") as student_info:
                for student in student_info:
                    temp=dict()
                    s=student.split("\t") #tab으로 구분된 데이터를 가져온다.
                    s[-1]=s[-1].replace("\n",'') #마지막 데이터에 붙은 줄바꿈 문자('\n')를 제거한다.

                    temp['id']=s[0]; temp['name']=s[1]; temp['mid']=int(s[2]); temp['final']=int(s[3])
                    temp['average']=(int(temp['mid'])+int(temp['final']))/2
                    temp['grade']=self.calGrade(temp['average'])
                    self.students.append(temp)
            self.show_student_list()

            
            
    def show_student_list(self, student=None, sameGrade_students=None):
        # method :: 학생들의 정보를 출력하는 메소드
        # student : 특정학생의 정보를 출력하려 할때 매개변수로 학생의 정보가 담겨져 있는 딕셔너리가 전달되게 된다.
        # sameGrade_students : 같은 학점을 가진 학생들을 출력하려 할때 매개변수로 학생 리스트가 전달되게 된다.
        
        # Step1. 데이터 header출력
        strFormat = '%10s %15s %10s %10s %10s %10s' # 컬럼명의 출력 포멧
        print(strFormat% ("Student","Name","Midterm","Final","Average","Grade"))
        print("-"*100)
        
        strFormat1 = '%10s %15s %10d %10d %10.1f %10s' #데이터의 출력 포멧
        
        # Step2. 데이터 출력
        # 2-1. 특정 학생 출력(1명)
        if student != None:
            print(strFormat1%(student['id'],student['name'],student['mid'],student['final'],student['average'],student['grade']))
            
        # 2-2. 같은 학점을 가진 학생들 출력(n명)
        elif sameGrade_students !=None:
            # 중간, 기말 시험의 평균을 가지고 오름차순 정렬을 수행한다.
            s=sorted(sameGrade_students, key=lambda x:x['average'],reverse=True)
            for i in s:
                print(strFormat1%(i['id'],i['name'],i['mid'],i['final'],i['average'],i['grade']))

        # 2-3. 전체 학생 출력
        else:
            # 중간, 기말 시험의 평균을 가지고 오름차순 정렬을 수행한다.
            s=sorted(self.students, key=lambda x: x['average'], reverse=True)
            for i in s:
                print(strFormat1%(i['id'],i['name'],i['mid'],i['final'],i['average'],i['grade']))
            
        print()
        return

    
    def search_student(self, sNum, call_type="search"):
        # method :: 학생을 검색하는 메소드
        # call_type 1) search : 사용자로부터 입력받은 학번을 통해 특정학생이 있는지 검색
        #               2) add_search : 사용자로부터 입력받은 학번을 통해 이미 그 학번을 사용하는 학생이 있는지 검색한다.
        #               3) same_grade_students : 사용자로부터 입력받은 학점을 가진 학생들이 존재하는지 확인한다.
        #               4) remove : 삭제하고자 하는 학생이 멤버 변수 students에 존재하는지 확인한다.
        #               5) change : 성적을 변경하고자 하는 학생의 학번이 존재하는지 확인한다.
        
        tf=False # sNum을 가지는 학생이 있는지 찾는다(이미 존재한다면 True, 없으면 False값을 갖게된다.)
        
        # res는 이미 존재하는 학생을 찾았을 때 그 학생의 정보를 담아두는 변수이다.
        # 특정인물을 검색하는 show를 수행할 때 조금더 빠르게 수행하도록 하고 싶어서 정보를 담아 전달해주는 용도로 사용되었다.
        res=dict() 
        
        # Call_type == same_grade_student인 경우.
        if call_type=="same_grade students":
        # sNum과 같은 학점을 가진 학생(들)의 정보를 res리스트에 담은 뒤 res를 반환.
            res=[]
            for i in self.students:
                if i['grade']==sNum:
                    res.append(i)
            return res
        
        #Step 1. 입력(sNum)과 같은 학번을 가지는 학생을 self.students에서 찾는다.
        idx=0
        
        for i in self.students:
            if sNum==i['id']:
                tf=True; findStudent=i; 
                break
            idx+=1
        
        # Call_type==remove인 경우
        if call_type=="remove":
            # 학생의 존재 여부와, self.students에서의 위치를 반환한다.
            return tf,idx
        
        
        # Step2. 입력(sNum)과 같은 학번을 가지는 학생이 존재하지 않는다면 문구 출력후 반환.
        if not tf:
            # Call_type==add_search인 경우
            # False를 반환한다.
            if call_type=="add_search":
                return tf
            
            print("NO SUCH PERSON.")
            return
       
        # Step3. 입력(sNum)과 같은 학번을 가지는 학생이 존재하는 경우.
        # call_type == search
        # 학생의 정보를 self.show_student_list의 매개변수로 전달해 화면에 출력한다.
        if call_type=="search":
            self.show_student_list(student=findStudent)
            return
        
        # call_type == change
        # 학생의 정보와 self.students에서의 위치를 self.change_score의 매개변수로 전달해 값을 변경하게 한다.
        elif call_type=="change":
            self.change_score(findStudent,idx)
            return
        
        # call_type == add_search
        # 존재여부를 반환한다.
        elif call_type=="add_search":
            return tf
        
        
    def change_score(self, stu_info, idx):
        # method :: 학생의 정보를 변경하는 메소드
        # stu_info : search_student로 부터 전달된 학생의 정보가 매개변수로 들어온다.
        # idx : 학생 정보의 self.students에서의 위치가  search_student로부터 매개변수로 전달되어 온다.
        
        cScore=input("Mid/Final?")
        if self.isString(cScore):
            if (cScore == "mid") or (cScore=="final"):
                nScore=input("Input new score:")
                if self.isNumber(nScore):
                    nScore=int(nScore)
                    if (nScore>=0) and (nScore<=100):
                        
                        # 변경전 정보를 출력한다.
                        self.search_student(stu_info['id'])
        
                        if cScore=="mid":
                            self.students[idx]['mid']=nScore
                        else:
                            self.students[idx]['final']=nScore

                        print("Score changed.")
                        self.students[idx]['average'] = (self.students[idx]['mid']+self.students[idx]['final'])/2
                        self.students[idx]['grade']=self.calGrade(self.students[idx]['average'])
                        self.search_student(stu_info['id'])
                else:
                    return
        else:
            return

        
    def add_student(self, stu_num):
        #method :: 학생을 새로 추가하는 메소드
        # stu_num : 새로 추가할 학생의 학번
        
        if self.search_student(stu_num,call_type="add_search"):
            #입력받은 학번이 이미 존재하는 경우
            print("ALREADY EXISTS")
            return
        else:
            #Step1. 데이터를 입력받는다.
            # 1-1. 문자열로 구성된 이름을 입력받는다.
            newStudentName=input("Name: ")
            while True:
                if self.isString(newStudentName):
                    break
                else:
                    print("이름은 문자열로 구성되어야 합니다. 다시 입력해주세요.\n")
                    newStudentName=input("Name:" )
                
                
            # 1-2. 숫자로 구성된 중간 점수를 입력받는다.
            newStudentMid = input("Midterm score: ")
            while True:
                if self.isNumber(newStudentMid):
                    newStudentMid=int(newStudentMid)
                    if(newStudentMid >=0 and newStudentMid<=100):
                        break
                    else:
                        print("0에서 100사이의 숫자로 다시입력해주세요.")
                        
                else:
                    print("점수는 숫자로 입력해주세요.'n'")
                newStudentMid = input("Midterm score: ")
            

            # 1-3. 숫자로 구성된 기말 점수를 입력받는다.
            newStudentFinal = input("Final score: ")
            while True:
                if self.isNumber(newStudentFinal):
                    newStudentFinal=int(newStudentFinal)
                    if(newStudentFinal >=0 and newStudentFinal<=100):
                        break
                    else:
                        print("0에서 100사이의 숫자로 다시입력해주세요. ")
                else:
                    print("점수는 숫자로 입력해주세요.")
                newStudentFinal = input("Final score: ")
                    
        
         # step2. 입력받은 데이터를 StudentList에 추가한다.
            newbie = dict()
            newbie["id"]=stu_num; newbie['name']=newStudentName; newbie['mid']=newStudentMid
            newbie['final']=newStudentFinal; newbie['average']=(newStudentMid+newStudentFinal)/2;
            newbie['grade']=self.calGrade(newbie['average'])
            
            try:
                self.students.append(newbie)
                print("Student added.")
            except:
                pass
            
    def search_same_grade(self, grade):
        #method :: 같은 grade를 가진 학생들의 리스트를 출력하는 메소드
        # grade: 찾고자 하는 학생의 성적
        
        res=self.search_student(grade, "same_grade students")
        if len(res) ==0:
            print("No Results")
        else:
            self.show_student_list(sameGrade_students=res)
        return

    def removeStudent(self, sid):
        # method :: 학생을 삭제하는 메소드
        # sid: 삭제할 학생의 학번
        
        res,idx=self.search_student(sid, call_type="remove")
        if res ==False:
            print("NO SUCH PERSON.")
        else:
            try:
                del self.students[idx]
                print("Student removed.")
            except:
                pass

    def save_file(self, fname):
        # method :: 성적관리 프로그램 종료 전 작업 데이터 저장하는 메소드.
        # fname : 새로 생성할 파일의 이름
        with open(fname, "w") as student_info:
            res=""
            self.students=sorted(self.students,key=lambda x:x['average'],reverse=True)
            for student in self.students:
                res+=student['id']+"\t"
                res+=student['name']+"\t"
                res+=str(student['mid'])+"\t"
                res+=str(student['final'])+"\n"

            student_info.write(res)
        
        return
        
smp=_StudentManageProgram()

while True:
    command=input("#")
    command=command.lower() #command를 통일시키기 위해 모든 문자를 소문자로 변환하였다.
    if command=="quit":
        wantSave=input("Save data?[yes/no]")
        if wantSave=="yes":
            filename=input("File name: ")
            smp.save_file(filename)
            
        #반복문 종료
        break 
            
    
    if command=="show":
        smp.show_student_list()
             
    if command=="search":
        sid=input("Student ID : ")
        
        # 학번은 숫자로 구성되어 있어야하므로, 문자가 잘못입력되었을 경우에는
        # 오류메시지를 출력한다.
        if smp.isNumber(sid):
            smp.search_student(sid)
        else:
            print("학번은 숫자로 구성되어 있어야 합니다\n")
            
    if command=="changescore":
        sid=input("Student ID : ")
        
        # 학번은 숫자로 구성되어 있어야하므로, 문자가 잘못입력되었을 경우에는
        # 오류메시지를 출력한다.
        if smp.isNumber(sid):
            smp.search_student(sid, "change")
        else:
            print("학번은 숫자로 구성되어 있어야 합니다.\n")
        
    if command=="add":
        sid=input("Student ID : ")
        
        # 학번은 숫자로 구성되어 있어야하므로, 문자가 잘못입력되었을 경우에는
        # 오류메시지를 출력한다.
        if smp.isNumber(sid):
            smp.add_student(sid)
        else:
            print("학번은 숫자로 구성되어 있어야 합니다.\n")
            
    if command=="searchgrade":
        sgrade = input("Grade to search : ").upper()
        if smp.isString(sgrade):
            if sgrade =="A" or sgrade =="B" or sgrade=="C" or sgrade =="D" or sgrade =="F":
                smp.search_same_grade(sgrade)
        else:
            print("잘못된 입력입니다.")
    
    if command=="remove":
        if len(smp.students)==0:
            print("List is empty")
        
        else:
            sid=input("Student ID : ")
        
            # 학번은 숫자로 구성되어 있어야하므로, 문자가 잘못입력되었을 경우에는
            # 오류메시지를 출력한다.
            if smp.isNumber(sid):
                smp.removeStudent(sid)
            else:
                print("학번은 숫자로 구성되어 있어야 합니다.\n")

