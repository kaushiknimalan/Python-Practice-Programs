import datetime
import math as m
import random


class Basics:
    @staticmethod
    def swap():
        # Ex : 1
        # Write a program that swaps the values of variables a and b.
        # You are not allowed to use a third variable. You are not allowed to perform arithmetic on a and b.
        a = 16
        b = 20
        print(f"Variable a(Before) : {a}")
        print(f"Variable b(Before) : {b}")
        print(' ')
        a, b = b, a
        print(f"Variable a(After) : {a}")
        print(f"Variable b(After) : {b}")

    @staticmethod
    def trig():
        # Write a program that makes use of trigonometric functions
        # available in math module.

        x = 100
        y = 50

        print(m.degrees(x))
        print(m.radians(x))
        print(m.sin(x))
        print(m.cos(x))
        print(m.tan(x))
        print(m.sinh(x))
        print(m.cosh(x))
        print(m.tanh(x))
        print(m.acos(m.cos(x)))
        print(m.asin(m.sin(x)))
        print(m.atan(x))
        print(m.hypot(x, y))

    @staticmethod
    def rand_num():
        # Write a program that generates 5 random numbers in the range 10
        # to 50. Use a seed value of 6. Make a provision to change this seed
        # value every time you execute the program by associating it with
        # time of execution?
        random.seed(datetime.time(), 6)
        i = 1
        while i <= 5:
            print(random.randint(10, 50))
            i += 1

    @staticmethod
    def maths(number):
        # Use trunc( ), floor( ) and ceil( ) for numbers -2.8, -0.5, 0.2, 1.5 and
        # 2.9 to understand the difference between these functions clearly.

        floor_ = []
        ceil_ = []
        trunc = []

        for i in number:
            floor_.append(m.floor(i))
            ceil_.append(m.ceil(i))
            trunc.append(m.trunc(i))
        print(f"Original Numbers = {str(number)}")
        print(f"Ceil of all the numbers = {str(ceil_)}")
        print(f"Trunc of all the numbers = {str(trunc)}")
        print(f"Floor of all numbers = {str(floor_)}")

    @staticmethod
    def fahrenheit_converter(far):
        # Assume a suitable value for temperature of a city in Fahrenheit
        # degrees. Write a program to convert this temperature into
        # Centigrade degrees and print both temperatures.
        # Formula : (50°F − 32) × 5/9 = 10°C

        temp_cel = (far - 32) * 5 // 9
        print(f"Temperature in Fahrenheit: {far}")
        print(f"Temperature in Celsius: {temp_cel}")

    @staticmethod
    def complex_printer(eq, imag_or_real):
        # Print imaginary part out of 2 + 3j.
        eq = complex(eq)
        if imag_or_real == 0:
            print(eq.imag)
        elif imag_or_real == 1:
            print(eq.real)
        else:
            print("You can use 1 for real and 0 for imaginary parts, the number you used is invalid..")

    @staticmethod
    def conj_number(eq):
        # Obtain conjugate of 4 + 2j.
        eq = complex(eq)
        print(eq.conjugate())

    @staticmethod
    def binary_converter(binary):
        # Print decimal equivalent of binary '1100001110'.
        print(int(str(binary), 2))

    @staticmethod
    def numeric_string_converter(float_value):
        #  Convert a float value 4.33 into a numeric string.
        print(str(round(float_value)))

    @staticmethod
    def division(dividend, divisor, remainder=True, quotient=True):
        #  Obtain integer quotient and remainder while dividing 29 with 5,
        # Obtain remainder on dividing 3.45 with 1.22.
        if quotient:
            if type(dividend) == float or type(divisor) == float:
                print(f"Quotient = {dividend / divisor}")
            else:
                print(f"Quotient = {dividend // divisor}")
        if remainder:
            print(f"Remainder = {dividend % divisor}")

    @staticmethod
    def hexadecimal_converter(number):
        # Obtain hexadecimal equivalent of decimal 34567.
        print(int(str(number), 16))

    @staticmethod
    def decimal_rounder(float_num, place=0):
        #  Round-off 45.6782 to second decimal place,
        #  Obtain 4 from 3.556,
        # Obtain 17 from 16.7844.
        print(round(float(float_num), int(place)))


class Strings:
    @staticmethod
    def output_generator():
        # S h
        # a n
        # enanigan
        # Shenan
        # Shenan
        # Shenan
        # Shenan
        # Shenanigan
        # Seaia
        # Snin
        # Saa
        # ShenaniganType
        # ShenanWabbite
        s = "Shenanigan"
        print(s[:2])
        print(s[4:6])
        print(s[2:])
        print(s[:6])
        print(s[:6])
        print(s[:6])
        print(s[:6])
        print(s)
        print(s[0:9:2])
        print(s[0:10:3])
        print(s[0:9:4])
        print(s + "Type")
        print(s + "Wabbite")

    @staticmethod
    def titlizor(sentence):
        # Write a program to convert the following string
        # 'Visit ykanetkar.com for online courses in programming'
        # into
        # 'Visit Ykanetkar.com For Online Courses In Programming'

        print(str(sentence).title())

    @staticmethod
    def caps_lock():
        s = 'Light travels faster than sound. This is why some people appear bright until you hear them speak.'
        s = s.replace("Light", "LIGHT")
        s = s.replace("sound", "SOUND")
        print(s)


class DecisionControl:

    @staticmethod
    def evenorodd(num):
        # Any integer is input through the keyboard. Write a program to find
        # out whether it is an odd number or even number.

        if num % 2 == 0:
            print(f"Integer {num} is Even.")
        else:
            print(f"Integer {num} is Odd.")

    @staticmethod
    def leap_year_finder(year):
        # Any year is input through the keyboard. Write a program to
        # determine whether the year is a leap year or not.

        if year % 4 == 0:
            print(f"Year {year} is a leap year.")
        else:
            print(f"Year {year} is Not a leap year.")

    @staticmethod
    def youngest(ages):
        # If ages of Ram, Shyam and Ajay are input through the keyboard,
        # write a program to determine the youngest of the three.

        ages = list(ages)
        youngest = 0
        for i in ages:
            i = int(i)
            if i > 0:
                youngest = i
        print(youngest)

    @staticmethod
    def triangle_valid_finder(angles):
        # Write a program to check whether a triangle is valid or not, when
        # the three angles of the triangle are entered through the keyboard.

        # A triangle is valid if the sum of all the three angles is equal to 180
        # degrees.

        angles = list(angles)
        sum_ = 0
        if not len(angles) == 3:
            print("Invalid Number of angles given. Valid number = 3.")
        else:
            for i in angles:
                sum_ += int(i)
            if not sum_ == 180:
                print("Invalid Triangle")
            else:
                print("Valid Triangle")

    @staticmethod
    def absolute_value(number):
        # Write a program to find the absolute value of a number entered
        # through the keyboard

        print(abs(int(number)))

    @staticmethod
    def area_greater_than_perimeter(length, breadth):
        #  Given the length and breadth of a rectangle, write a program to find
        # whether the area of the rectangle is greater than its perimeter. For
        # example, the area of the rectangle with length = 5 and breadth = 4
        # is greater than its perimeter

        area = length * breadth
        perimeter = 2 * (length + breadth)
        if area > perimeter:
            print("Area is greater than Perimeter.")
        elif area < perimeter:
            print("Perimeter is greater than Area.")
        else:
            print("Area is equal to Perimeter.")

    @staticmethod
    def is_on_line(points):
        # Given three points (x1, y1), (x2, y2) and (x3, y3), write a program to
        # check if all the three points fall on one straight line.

        true = []
        points = list(points)
        for i in points:
            if int(i[1]) == 3 * int(i[0]) - 1:
                true.append(1)
        print(true)

    @staticmethod
    def is_point_circle(point, centre, radius):
        # Given the coordinates (x, y) of center of a circle and its radius, write
        # a program that will determine whether a point lies inside the circle,
        # on the circle or outside the circle. (Hint: Use sqrt( ) and pow( )
        # functions)

        x_1 = point[0]
        x_2 = centre[0]
        y_1 = point[1]
        y_2 = centre[1]
        distance = m.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        if distance > radius:
            print("Point is Outside of the circle.")
        elif distance < radius:
            print("Point is Inside the circle.")
        else:
            print("Point is on the circle.")

    @staticmethod
    def x_or_y_axis(coord):
        # Given a point (x, y), write a program to find out if it lies on the X-axis, Y-axis or on the origin.

        x = coord[0]
        y = coord[1]
        if x == 0 and y == 0:
            print("Point is in the Origin.")
        elif x == 0 and y > 0:
            print("Point is in the Y axis.")
        elif x > 0 and y == 0:
            print("Point is in the X axis.")

    @staticmethod
    def leap_year_finder_2(year):
        # A year is entered through the keyboard, write a program to
        # determine whether the year is leap or not. Use the logical operators
        # and and or.

        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(f"{year} is a Leap year.")
        else:
            print(f"{year} is not a Leap year.")

    @staticmethod
    def is_triangle_valid_finder(angles):
        # If the three sides of a triangle are entered through the keyboard,
        # write a program to check whether the triangle is valid or not. The
        # triangle is valid if the sum of two sides is greater than the largest of
        # the three sides.

        hyp = max(angles)
        angles.remove(max(angles))
        sum_ = 0
        for i in angles:
            sum_ += int(i)
        if sum_ == hyp:
            ans = True
        else:
            ans = False

        return ans

    @staticmethod
    def right_angle_finder(angles):
        # If the three sides of a triangle are entered through the keyboard,
        # write a program to check whether the triangle is valid or not. The
        # triangle is valid if the sum of two sides is greater than the largest of
        # the three sides.

        hyp = max(angles)
        angles.remove(hyp)
        if angles[0] ** 2 + angles[1] ** 2 == hyp ** 2:
            ans = True
        else:
            ans = False

        return ans

    @staticmethod
    def triangle_type(sides, angles):
        # If the three sides of a triangle are entered through the keyboard,
        # write a program to check whether the triangle is isosceles,
        # equilateral,scalene or right angled triangle.

        a, b, c = sides[0], sides[1], sides[2]

        if DecisionControl.is_triangle_valid_finder(angles):
            if a == b != c or a != b == c or b != a == c:
                print("The triangle is an isosceles triangle.")
            elif a == b == c:
                print("The triangle is an equilateral")
            elif DecisionControl.right_angle_finder([a, b, c]):
                print("The triangle is a Right angle.")
            elif a != b != c:
                print("The triangle is a scalene triangle.")
            else:
                print("Invalid triangle")
        else:
            print("Invalid Triangle")


class RepetitionControl:
    @staticmethod
    def range_print_odd(r):
        # Write a program to print first 25 odd numbers using range()

        for i in range(r + 1):
            if i % 2 != 0:
                print(i)

    @staticmethod
    def rewrite():
        # Rewrite the following program using for loop.
        # lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
        # s = 'Mumbai'
        # i = 0
        # while i < len(lst) :
        # if i > 3 :
        # break
        # else :
        # print(i, lst[i],s[i])
        # i += 1

        lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
        s = 'Mumbai'
        for j in range(len(lst) + 1):
            if j > 3:
                break
            else:
                print(j, lst[j], s[j])

    @staticmethod
    def alphanum_counter(st):
        # Write a program to count the number of alphabets and number of
        # digits in the string 'Nagpur-440010'

        alpha_count = 0
        num_count = 0
        for i in st:
            if isinstance(i, str):
                try:
                    int(i)
                    num_count += 1
                except:
                    alpha_count += 1
        print(f"Alphabet count: {alpha_count}")
        print(f"Number count: {num_count}")

    @staticmethod
    def reverse_number(number):
        number = str(number)
        number_reversed = []
        for i in enumerate(number):
            # number_reversed.append(number[i*-1])



rt = RepetitionControl
rt.reverse_number(1332)
