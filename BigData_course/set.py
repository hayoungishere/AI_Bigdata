class Set:
    def __init__(self, member=[]):
        
        self.member=[]
        self.member.append(member[0])
        #객체를 생성할 때 받아온 데이터 리스트의 원소가 겹치는지 확인 후 제거한다.
        for item in member[1:]:
            if item not in self.member:
                self.member.append(item)
        return 
    
    def append(self,a):
        if a not in self.member:
            #집합에 속하지 않은 새로운 변수가 들어온 경우
            self.member.append(a)
            return True
        else:
            # 집합에 이미 속한 변수가 입력으로 들어온 경우
            # 실패의 의미로 False를 반환한다.
            return False
    
    def delete(self, a):
        #if a in self.member:
            #print(a)
            
        for i in range(len(self.member)):
            if self.member[i] == a:
                #delete 하고 싶은 원소가 member list안에 속해 있으면 삭제.
                del self.member[i]
                return True
        
        # 전달받은 원소가 member list에 존재하지 않는 경우로.
        # delete실패의 의미로 False를 반환한다.
        return False 

    def union(self, s2):
        uniSet=[item for item in self.member]
        uniSet=uniSet+[item for item in s2.member if item not in uniSet]
        
        # New_Set이라는 Set을 상속받는 자식 클래스를 사용하여
        # 새로운 New_Set 객체가 만들어지게 한다.
        return New_Set(uniSet)
    
       
    def intersection(self, s2):
        interSet=[item for item in self.member if item in s2.member]
        
        # New_Set이라는 Set을 상속받는 자식 클래스를 사용하여
        # 새로운 New_Set 객체가 만들어지게 한다.
        return New_Set(interSet)
        
    def difference(self, s2):
        diffSet=[item for item in self.member if item not in s2.member]
        
        # New_Set이라는 Set을 상속받는 자식 클래스를 사용하여
        # 새로운 New_Set 객체가 만들어지게 한다.        
        return New_Set(diffSet)
    
    # operation overriding of "+"
    def __add__(self, another): #Union(+)
        return self.union(another)
    
    # operation overriding of "-"        
    def __sub__(self, another) : #Difference(-)
        return self.difference(another)
    
    # operation overriding of "/" 
    def __truediv__(self, another): #Intersection(/)
        return self.intersection(another)
    
    def __repr__(self):
        return str(self.member)
    
class New_Set(Set):
    # Set 클래스를 상속받는 자식 클래스를 선언한다.
    # union / intersection / difference 수행후 
    # set 객체를 반환하기 위한 클래스 이다.
    pass




def main():
    a=Set([1,2,3,3])
    b=Set([2,3,4])
    print("original data in set of a ==>", a)
    print("original data in set of b ==>", b)
    
    print("="*50)
    a.append(5); a.append(1)
    print("After:: append 5 and 1 in a ==>", a)
    
    a.delete(1)
    print("After:: delete 1 in a ==>",a)

    print("="*50)
    c=a.union(b)
    print("[1,2,3,5].union([2,3,5]) ==>", c)

    d=a.difference(b)
    print("[1,2,3,5].difference([2,3,5]) ==>",d)

    e=a.intersection(b)
    print("[1,2,3,5].intersection([2,3,5]) ==>",e)

    print("="*50)
    f=Set([1,3,5])+Set([2,4,6])
    print("[1,3,5] + [2,4,6]: 합집합 ==>", f)

    g=Set([1,2,3,4,5])-Set([1,3,6])
    print("[1,2,3,4,5]-[1,3,6]: 차집합 ==>",g)

    h=Set([1,2,3,4,5])/Set([1])
    print("[1,2,3,4,5]/[1]: 교집합 ==>",h)

if __name__ == '__main__':
    main()
