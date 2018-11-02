def exercise01():
    # Create a variable x and set it to 5.
    # ------ Place code below here \/ \/ \/ ------
    x=5
    # ------ Place code above here /\ /\ /\ ------
    return x
def exercise02():
    # Create a string variable called name and set it to your first name.
    # ------ Place code below here \/ \/ \/ ------
    name="Zhipeng"
    # ------ Place code above here /\ /\ /\ ------
    return name
def exercise03():
    # Create a string variable called sentence and assign it to an arbitrary sentence that contains at least 3 words
    # ------ Place code below here \/ \/ \/ ------
    sentence="I love python"
    # ------ Place code above here /\ /\ /\ ------
    return sentence
def exercise04():
    # Create two string variables. The first variable is called first_name, the second is last_name. Set both variables to your first name and last name respectively.
    # ------ Place code below here \/ \/ \/ ------
    first_name="Zhipeng"
    last_name="Xu"
    # ------ Place code above here /\ /\ /\ ------
    return first_name, last_name
def exercise05():
    # Repeate exercise 4 here and assign the datatype of the variable first_name to a variable called name_type
    # ------ Place code below here \/ \/ \/ ------
    first_name="Zhipeng"
    last_name="Xu"
    name_type=first_name
    # ------ Place code above here /\ /\ /\ ------
    return first_name, last_name, name_type
def exercise06():
    # Assign 20 to the variable hours_worked, 15 to the variable wage_per_hour and the product of the two to variable total_pay
    # ------ Place code below here \/ \/ \/ ------
    hours_worked=20
    wage_per_hour=15
    total_pay=hours_worked*wage_per_hour
    # ------ Place code above here /\ /\ /\ ------
    return hours_worked, wage_per_hour, total_pay
def exercise07():
    # Create a variable wage and assign 17.0 to it. Print to the screen the datatype of wage. Create a second variable called doubled that prints to the screen 2 times wage
    # ------ Place code below here \/ \/ \/ ------
    wage=17.0
    print(type(wage))
    doubled=float(wage*2)
    # ------ Place code above here /\ /\ /\ ------
    return wage, doubled
def exercise08():
    # Assign 5 to the variable quantity, 'hello' to the variable hello and a variable hello_repeated that holds a string that contains whatever is contained in the variable hello repeated quantity times
    # ------ Place code below here \/ \/ \/ ------
    quantity=5
    hello='hello'
    hello_repeated=hello*quantity
    # ------ Place code above here /\ /\ /\ ------
    return quantity, hello, hello_repeated
def exercise09():
    # Assign 10 to a variable qty, 5 to a variable price and the product of the two to a variable total_cost
    # ------ Place code below here \/ \/ \/ ------
    qty=10
    price=5
    total_cost=qty*price
    # ------ Place code above here /\ /\ /\ ------
    return qty, price, total_cost
def exercise10():
    # Create 5 variables named factorN where N is the numbers 1 to 5 and set them to 1 through 5, respectively. Create a variable called product that holds the product of the 5 variables
    # ------ Place code below here \/ \/ \/ ------
    factor1=1
    factor2=2
    factor3=3
    factor4=4
    factor5=5
    product=factor1*factor2*factor3*factor4*factor5
    # ------ Place code above here /\ /\ /\ ------
    return factor1, factor2, factor3, factor4, factor5, product
def exercise11():
    # Create a variable pi and literally set it to pi 10 decimal places out
    # ------ Place code below here \/ \/ \/ ------
    import math
    n=str(math.pi)
    m=n[:n.find('.')+11]
    pi=float(m)
    # ------ Place code above here /\ /\ /\ ------
    return pi
def exercise12():
    # Create a variable called x and set it to 10. Then create a variable y that equals to x to the 7th power
    # ------ Place code below here \/ \/ \/ ------
    x=10
    y=1
    for i in range(1,8):
        y=y*x
    # ------ Place code above here /\ /\ /\ ------
    return x, y
def exercise13():
    # Create variables volume_sphere, r. Set r to 7 and calculate the volume of the sphere with r = 7 and assign it to volume_sphere
    pi = 3.14159
    # ------ Place code below here \/ \/ \/ ------
    r=7
    volume_sphere=4/3*pi*r*r*r
    # ------ Place code above here /\ /\ /\ ------
    return pi, r, volume_sphere
def exercise14():
    # Create a variables area, length, height. Set length and height equal to 50 and 10.2 respectively. Assign area to the product of length and height, assign the variable area_type to the datatype of area
    # ------ Place code below here \/ \/ \/ ------
    length=50
    height=10.2
    area=length*height
    area_type=type(area)
    # ------ Place code above here /\ /\ /\ ------
    return area, length, height, area_type
def exercise15():
    # Calculate the distance covered by a car moving at 80 miles per hour for 3 hours
    # ------ Place code below here \/ \/ \/ ------
    speed_mph=80
    duration=3
    distance=speed_mph*duration
    # ------ Place code above here /\ /\ /\ ------
    return distance, speed_mph, duration
def exercise16():
    # Implement pythogorean thereom and find the length of hypotenuse c given sides a and b. Select any numbers for a and b. Use math.sqrt() for square root.
    # ------ Place code below here \/ \/ \/ ------
    import math
    a=3
    b=4
    c=math.sqrt(a*a+b*b)
    # ------ Place code above here /\ /\ /\ ------
    return a, b, c      

        



     



        
        
  