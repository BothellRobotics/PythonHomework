#! /usr/bin/env python
circle = "circle"
rectangle = "rectangle"
square = "square"
print("My awesome program can Compute Area and Perimeter of a rectangle, square, and circle!!!")
print("Please Type the shape you want: ")

answer = input()

if answer == circle:
    print("Enter Circle Raidus decimal numbers are allowed :")

    radius = float (input())

    pi = 3.147

    area = pi * radius * radius 

    perimeter = 2 * pi * radius 

    print(area,  " is the area of the Circle")

    print(perimeter, " is the perimeter of the Circle")
else:
    if answer == rectangle:
        print("Enter the horizontal of the Rectangle , decimal numbers are allowed :")


        print("Enter the vertical of the Rectangle, decimal numbers are allowed :")  

        horizontal = float (input())
        vertical  = float (input())

        area = horizontal  * vertical 

        perimeter =  horizontal + horizontal + vertical + vertical 

        print(area,  " is the area of the Rectangle")

        print(perimeter, " is the perimeter of the Rectangle")
    else:
        if answer == square:
            print("Enter one Side of the Square, decimal numbers are allowed :")

            Side = float (input())


            area = Side * Side

            perimeter =  Side + Side + Side + Side

            print(area,  " is the area of the square")

            print(perimeter, " is the perimeter of the square")
