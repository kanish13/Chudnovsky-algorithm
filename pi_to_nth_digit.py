import math
from decimal import *
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
def summation_value(k):
    k=k+1
    getcontext().prec = k
    summation=0
    for i in range(k):
        denominators_numerator=(factorial(6*i))*((545140134*i)+13591409)
        denominators_denominator=(factorial(3*i))*((factorial(i))**3)*((-262537412640768000)**i)
        denominator=denominators_numerator/denominators_denominator
        summation=summation+denominator
        return Decimal(summation)
def return_value(k):
    iter=summation_value(k)
    numerator=426880*math.sqrt(10005)
    pi=Decimal(numerator)/iter
    return pi
n=int(input("Enter number of digits you want to print the pi:"))
print(return_value(n))
