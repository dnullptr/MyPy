# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:42:37 2020

@author: Daniel
"""
def ReverseDic(m):
    rev = list(zip(m.values(), m.keys()))
    return rev



def main():
    m={'a':1,'b':2}
    print(ReverseDic(m))
    
main()