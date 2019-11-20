#tok.py
# 입력받은 단어 열의 n-gram을 구해주는 tokenize()함수 정의하기
def tokenize(trg, N=1):
    li=[]
    trg=trg.split()
    for i in range(len(trg)-N+1):
        # 0 ~ (길이-N+1) 부터 시작하는 문자열을 저장.
        tok=""
        for j in range(N):
            # 공백을 기준으로 나눠진 단어를 N개 붙인다.
            tok+=trg[i+j]+" "
        
        tok=tok[:-1] # 마지막 공백문자 제거한다.
        li.append(tok)
    return li

def main():
    a="There was a farmer who had a dog ."
    print(tokenize(a))
    print(tokenize(a,2))
    
if __name__ == '__main__':
    main()