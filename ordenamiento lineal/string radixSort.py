import sys                                  
import math                                 
from time import time                       
class sd (object):                          
    def __init__(self):                     
        self.origin = ""                    
        self.compr = ""                     
                                            
                                            
                                            
def sizeStr(x):                             
    # retorna el tamaño del numero          
    return len(str(x))                      
                                            
                                            
def initQ(mtr):                             
    for i in range(10):                     
        mtr.append([])                      
                                            
                                            
def maxSizeLen(A):                          
    max = ""                                
    for i in range(0, len(A)):              
        if len(max) < len(A[i]):            
            max = A[i]                      
    print(max)                              
    return len(str(max))                    
                                            
                                            
def printM(A):                              
    for i in range(len(A)):                 
        print(str(i) + ": " + str(A[i]))    
                                            
                                            
def rmp_array(dr):                          
    Bs = []                                 
    for i in range(len(dr)):                
        # print("#asda")                    
        # print(dr[i])                      
        for j in range(len(dr[i])):         
            s = dr[i][j]                    
            Bs.append(s)                    
    return Bs                               
                                            
                                            
def Mradix(As):                             
    maxSize = maxSizeLen(As)                
                                            
    for i in range(maxSize):                
        dr = []                             
        initQ(dr)                           
        for j in range(len(As)):            
            number = As[j]                  
            if len(number) - 1 < i:         
                dr[0].append(As[j])         
            else:                           
                n = len(number) - i - 1     
                dr[int(number[n])].append(As
        As = rmp_array(dr)                  
    return As                               
                                            
                                            
T = int(sys.stdin.readline().strip())       
