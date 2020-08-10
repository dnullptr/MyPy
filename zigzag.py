def zigZagEncode(st):
    line1=''
    line2=''
    for i in range(len(st)):
        if(i%2==0):
            line1+=st[i]
        else:
            line2+=st[i]
            
    return [line1,line2]

def zigZagDecode(zipIter):
    stOut=''
    iterIndex1=0;iterIndex2=0
    
    recursiveLength=0
    for i in zipIter:
        recursiveLength+=len(i)
        
    for i in range(recursiveLength):
        if(i%2==0):
            stOut+=zipIter[0][iterIndex1]
            iterIndex1+=1
        else:
            stOut+=zipIter[1][iterIndex2]
            iterIndex2+=1
    return stOut
    
def main():
    st="abcdefg"
    print(zigZagEncode(st))
    print(zigZagDecode(zigZagEncode(st)))
main()
    
        