#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    
    def gcd(self,A,B) :
        # print("A : {} B: {}".format(A,B))
        if B == 0 :
            return A 
        else : return self.gcd(B,A % B)
        
    def rotateArr(self,A,D,N):
        #Your code here
        D = D% N 
        
        g = self.gcd(N,D)
        # print("g: {}".format(g))
        for i in range(g) :
            temp  = A[i]
            k = i + D
            while k % N != i :
                A[(k-D)%N] = A[k]
                k = (k+D) % N
            A[(i-D)%N] = temp
        
            


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