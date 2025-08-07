#1. write a recurssive function to print N natural numbers.

def rec(n):
    if n > 0:
        rec(n-1)
        print(n)

#rec(5)

#2.write a recursive function to print N natural numbers in reverse order.

def reVrec(n):
    if n > 0:
        print(n)
        reVrec(n-1)
        

#reVrec(5)

#3. Write a recursive function to print first N odd natural numbers.

def printOddN(n):
    if n>0:
        printOddN(n-1) 
        print(2*n-1)
#printOddN(10)

#4. write a recursive function to print first N even natural numbers.

def printEvenN(n):
    if n>0:
        printEvenN(n-1)
        print(2*n)

#printEvenN(10)

#5. write a recursive function to print first N odd natural numbers in reverse order.
def revPrintOddN(n):
    if n>0:
        print(2*n-1)
        revPrintOddN(n-1) 

#revPrintOddN(10)        

#6. write a recursive function to print first N even natural numbers in reverse order

def revPrintEvenN(n):
    if n>0:
        print(2*n)
        revPrintEvenN(n-1) 

#revPrintEvenN(10)

#7. Write a recursive fucntion to calculate sum of first N natural numbers.

def sumOfN(n):
    if n == 1:
        return 1
    else:
        return n + sumOfN(n-1)

#print(sumOfN(3))

#8. Write a recursive fucntion to calculate sum of first N odd natural numbers.

def sumOddN(n):
    if n == 1:
        return 1
    else:
        return 2*n-1 + sumOddN(n-1)
    
#print(sumOddN(3))

#9. Write a recursive fucntion to calculate sum of first N even natural numbers.

def sumEvenN(n):
    if n == 1:
        return 2
    else:
        return 2*n + sumEvenN(n-1)
    
#print(sumEvenN(3))

#10. Write a recursive fucntion to calculate sum of first N even natural numbers.

def factN(n):
    if n == 1:
        return 1
    else:
        return n * factN(n-1)
    
#print(factN(3))

#11. Write a recursive fucntion to calculate sum of squares of first N even natural numbers.

def sumSqrN(n):
    if n == 1:
        return 1
    else:
        return n**2 + sumSqrN(n-1)
    
#print(sumSqrN(3))
    
