# prime.py
# 소수 판단하는 함수 정의하기
# 소수면, True 반환
# 소수가 아니면, False 반환

def check_prime(num):
    cnt=0
    res=True
    for i in range(1,num):
        if num%i == 0: cnt+=1 # i가 1일때도 cnt는 증가됨. 
        if cnt>=2:
            # 1을 제외한 다른 수로 나누어 떨어진다면
            # 해당 숫자는 소수가 아니고
            # 반환값을 False로 바꾼후
            # for문을 종료한다.
            res=False
            break
   
    return res

def main():
    a=13
    b=15
    if check_prime(a):
        print(str(a)+'는 소수입니다.')
    else:
        print(str(a)+'는 소수가 아닙니다.')
        
    if check_prime(b):
        print(str(b)+'는 소수입니다.')
    else:
        print(str(b)+'는 소수가 아닙니다.')
        
        
if __name__ =='__main__':
    main()