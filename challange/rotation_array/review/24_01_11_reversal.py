#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    
    
    def rotateArr(self,A,D,N):
        #Your code here
        
        def reverse(x,y) :
            while x <=y :
                A[x] , A[y] = A[y] ,A[x]
                x+=1
                y-=1
            
        reverse(0,D-1)
        reverse(D,N-1)
        reverse(0,N-1)
        # A[0:D].reverse()
        # A[D:].resverse()
        # A.reverse()
        
        return A

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends