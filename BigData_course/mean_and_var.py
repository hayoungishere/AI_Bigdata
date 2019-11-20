def mean_and_var(*val):
    m=[]; v=[]

    
    for i in range(len(val[0])):
        s=0
        for j in range(len(val)):
            s+=val[j][i]
        m.append(s)
        
    m=[x/len(val) for x in m] #mean
    
    for i in range(len(val[0])):
        dif=0
        for j in range(len(val)):
            dif+=(val[j][i]-m[i])*(val[j][i]-m[i])
        v.append(dif)
    
    v=[x/len(val) for x in v] #variance
    
    
    
    
    return m,v

def main():
    v1=(0,1)
    v2=(0.5,0.5)
    v3=(1,0)
    
    m,var = mean_and_var(v1,v2,v3)
    print("평균:",m,"분산:",var)
    
if __name__ == '__main__':
    main()