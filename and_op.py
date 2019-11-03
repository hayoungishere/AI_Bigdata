def main():
    x1 = np.array([[0,0]])
    x2 = np.array([[0,1]])
    x3 = np.array([[1,0]])
    x4 = np.array([[1,1]])

    while True:
        w=np.random.randn(2,2)
        b=np.random.randn(2,)

        xx1=(x1.dot(w)+b).argmax()
        xx2=(x2.dot(w)+b).argmax()
        xx3=(x3.dot(w)+b).argmax()
        xx4=(x4.dot(w)+b).argmax()

        #print(xx1,xx2,xx3,xx4)
        if xx1==0 and xx2==0 and xx3==0 and xx4==1:
            #and의 연산의 결과와 일치하면 반복문 종료
            break

    print("[0,0] : ",xx1)
    print("[0,1] : ",xx2)
    print("[1,0] : ",xx3)
    print("[1,1] : ",xx4)
    print("W:",w)
    print("b:",b)


if __name__ == '__main__':
    main()