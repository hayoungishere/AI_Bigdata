import sys
import os

argv=sys.argv[1:] #argument vector를 통해 입력 파일 이름과 출력파일이름을 전달받는다.

if os.path.exists(argv[0]):
    # 원본파일이 존재 할때만 파일 복사를 수행한다.
    
    if len(argv) ==2 : 
        with open(argv[0], "r") as inFile:
            with open(argv[1], "w") as outFile:
                for line in inFile:
                    #입력파일을 줄단위로 읽는다.
                    outFile.write(line)
    else:
        print("Copy File Name is Not FOUND in your command.")
else:
    print("Original file is Not FOUND")