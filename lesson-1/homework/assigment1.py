#1.Given a side of square. Find its perimeter and area.
side=float(input('Enter value of a side : '))

perimeter=4*side
area=side* side

print('Perimeter of the square:' , perimeter)
print('Area of the square: ', area)

#2.Given diameter of circle. Find its length.

import  math


diameter=float(input('Enter  diameter of circle:'))


length=math.pi*diameter


print('Length of circle is :', length)


#3.Given two numbers a and b. Find their mean.

a=float(input('Enetr value of a: '))
b=float(input('Enter value of b: '))

mean=(a+b)/2

print('mean of  two numbers is  ', mean)


#4.Given two numbers a and b. Find their sum, product and square of each number.

a=float(input('Enter value of a :'))
b=float(input('Enter value of b:'))

sum=a+b
product=a*b
square1=a*a
square2=b*b


print('Sum is', sum )
print('Product is' ,product)
print('Square1 is ' , square1)
print('Square2 is', square2)



