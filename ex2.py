import sys

print(sys.argv)

with open(sys.argv[1], "r") as oriF:
    with open(sys.argv[2],"w") as newF:
        for line in oriF:
            newF.write(line)