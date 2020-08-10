# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:00:32 2020

@author: Daniel
"""
def cipherDict():
    m=dict()
    ch=ord('a')
    ch2=ord('z')
    for i in range(26):
        m[chr(ch+i)]=chr(ch2-i)
        #ch+=1
        #ch2-=1
    return m



def encodeDecodeStr(st):
       
    st2=''
    for i in st:
        if(ord(i)>=ord('a') and ord(i)<=ord('z')): #אם תו רגיל
            st2+=cipherDict()[i]
            
        else:                        #כל תו אחר
            st2+=st[i]
 
    return st2


def main():
    st1='abcd'
    print(encodeDecodeStr(st1))
    
main()