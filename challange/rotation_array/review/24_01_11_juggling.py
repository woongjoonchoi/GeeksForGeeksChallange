import math
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        g = math.gcd(D,N)
        D = D % N

        for  i in range(g) :
            x = i
            temp = A[i]
            for k in range(N//g) :
                new_x = (x-D) % N
                t_temp = A[new_x]
                A[new_x] = temp
                x= new_x
                temp = t_temp
                
        return A