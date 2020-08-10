# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:30:44 2020

@author: Daniel
"""

def wigglyPath(st): #mat will be hardcoded inside
    sqr=int(len(st)**0.5)
    mat=[[] for i in range(sqr)]
    arrNum=0
    dirSw=1 # 1 for forward , -1 for reverse
    for i in range(len(st)):
       mat[arrNum].append(i)
       if(arrNum<sqr-1 and dirSw==1): #ole ve katan mi shoresh
           arrNum+=1
       elif(arrNum==sqr-1 and dirSw==1): #ole ve hegia la shoresh , aheret bli shoresh itaka po alia rishona bimkom elif mitahat she morid
           dirSw=-1
       elif(arrNum>0 and dirSw==-1):
           arrNum-=1
       elif(arrNum==0):
           dirSw=1
        
       
    
        
def main():
    st="the quick brown foxy"
    mat=[[] for i in range(int(len(st)**0.5))]
    print(mat)
    
main()