import random
import math

n = 17958
N = n+1
H = 14226
G = 17

def group(x, a, b): #Groups to determind computations
    temp = x % 3

    if(temp == 0):
        x = (x * x) % N
        a = (a * 2) % n
        b = (b * 2) % n
    if(temp == 1):
        x = (x * H) % N
        b = (b + 1) % n
        
    if(temp == 2):
        x = (x * G) % N
        a = (a + 1) % n

    return x, a, b

x = 1
a = 0
b = 0

X = x
A = a
B = b

for i in range(1,n):
    #Turtle
    x, a, b = group(x, a, b)

    #Hare
    X, A, B = group(X, A, B)
    X, A, B = group(X, A, B)

    #Checks if matching
    if(x == X):
        break

print(x, a, b)
print(X, A, B)

#6228 * 12623 = 899 * 16483 = 9501
#gcd(3442, 17958) = 2; X * 3442 = 2 (mod 17958) = -2953
#9312-6938 = 2734*-2953 and 2*3442


#g^11156 = 14226^2 (mod 17958) 
#2*log_17(14226) = 11156 (mod 17958) 
#log_17(14226) = 5578 (mod 8979)

#{5578, 14557}