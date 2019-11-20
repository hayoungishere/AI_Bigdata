def add_comma(val):
    res=""
    
    while val>0:
        res=","+str(val%1000)+res
        val=val//1000
    
    res=res[1:]
    return res


def main():
    comma_added_1234 = add_comma(1234)
    comma_added_12345678 = add_comma(12345678)
    comma_added_12 =add_comma(12)
    
    print(comma_added_1234)
    print(comma_added_12345678)
    print(comma_added_12)
    
if __name__ == '__main__':
    main()