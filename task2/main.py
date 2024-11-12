from math_operations.add import addition
from math_operations.div import division
from math_operations.mul import multiply
from math_operations.sub import subtraction


if __name__  == '__main__':
    print('this is main code')

    n1 = int(input("enter the first number : "))
    n2 = int(input("enter the second number : "))
    op = input("which math opperation do you want to perfrom - \n sub \n multi \n add \n div \n --:  ")

    if op.lower == 'add' or 'addition' :
        add=addition(n1,n2)
        print(f'addition = {add}')

    elif op.lower == 'multi' or 'multiplication' :

        mul=multiply(n1,n2)
        print(f'multiplication = {mul}')

    elif op.lower == 'sub' or 'subtraction' :

        sub=subtraction(n1,n2)
        print(f'subtracction = {sub}')

    elif op.lower == 'div' or 'division' :

        div=division(n1,n2)
        print(f'division  = {div}')

    else :
        print("ENTER THE CORRECT OPERATION YOU WANT TO PERFROM :- \n sub \n multi \n add \n div")


    