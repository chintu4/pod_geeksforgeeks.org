#https://www.geeksforgeeks.org/problems/rightmost-different-bit-1587115621/1
#Original Answer
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




    
# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        xor = m ^ n
        rightmost_diff_bit = xor & -xor
        position = 0
        while rightmost_diff_bit > 0:
            rightmost_diff_bit >>= 1
            position += 1
        if xor == 0:
            return -1
        else:
            return position

#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends

#minethought program
#m,n=15,9


#def co(m,n):
#    mb=str(bin(m).replace('0b',''))
#    nb=str(bin(n).replace('0b',''))
#    print(mb,nb)
#    count=0
#    c=-1
#    for i in range(len(mb)):
#        count+=1
#        if mb[c]!=nb[c]:
#            print('different at ',c)
#            break
#        c-=1
#    return count
    

#print(co(11,9))
