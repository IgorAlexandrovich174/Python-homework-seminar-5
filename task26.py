'''Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.'''

def myPow(a: int, b: int) :
    
    if b == 0 :
        return 1
    if b == 1 :
        return a        
    else :
        return a * myPow(a, b - 1)
    
print(myPow(3,5))