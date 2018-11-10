import math
import unittest
import numpy as np
import requests as r
def exercise01():
    # Create a list called animals containing the following animals: cat, dog, crouching tiger, hidden dragon, manta ray
    # ------ Place code below here \/ \/ \/ ------
    animals=['cat','dog','crouching tiger','hidden dragon','manta ray']
    # ------ Place code above here /\ /\ /\ ------
    return animals
def exercise02():
    # Repeat exercise 1 and loop through and print each item in the animal list by iterating through an index number and using range(). Set the variable len_animals to the length of the animal list.
    # ------ Place code below here \/ \/ \/ ------
    animals=['cat','dog','crouching tiger','hidden dragon','manta ray']
    len_animals=(len(animals))
    for x in range(0,len_animals):
        print(animals[x])
    # ------ Place code above here /\ /\ /\ ------
    return animals, len_animals
def exercise03():
    # Reorganize the countdown list below in descending order and return the value of the 5th element in the sorted countdown list
    countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
    the_fifth_element = -999
    # ------ Place code below here \/ \/ \/ ------
    countdown.sort(reverse=True)
    the_fifth_element=countdown[4]
    # ------ Place code above here /\ /\ /\ ------
    return countdown, the_fifth_element
def exercise04(more_temperatures, iot_sensor_points, a, b, c, d, e):
    # This exercise function receives a list of temperatures and a dictionary of temperature data where the key is an arbitrary sequential number and the value is the temperature and a,b,c,d and e are each a single temperature reading
    # To Do:
    # 1. Add all of the items in more_temperatures to the temperatures list
    # 2. Add all of the temperature values in iot_sensor_points to the temperatures list
    # 3. Add a,b,c,d and e to the temperature list
    # 4. Organize the temperatures in descending order
    # 5. The samples list will contain every 5th reading from the final temperatures list i.e in list [1,2,3,4,5,6,7,8,9,10] samples would be [5,10]
    # 6. Do a shallow copy of samples into copy_of_samples
    # 7. Organize samples in ascending order

    temperatures = list(np.random.randint(-25, 25, size=10))
    samples = []
    copy_of_samples = []
    # ------ Place code below here \/ \/ \/ ------
    temperatures = list(np.random.randint(-25, 25, size=10))
    samples = []
    copy_of_samples = []

    for items in more_temperatures:
        temperatures.append(items)
    for x in iot_sensor_points.values():
        temperatures.append(x)
    temperatures.append(a)
    temperatures.append(b)
    temperatures.append(c)
    temperatures.append(d)
    temperatures.append(e)
    temperatures.sort(reverse=True)
    for i in range(0,11):
        samples.append(temperatures[5*i-1])
    copy_of_samps=samples
    samples.sort(reverse=False)
    # ------ Place code above here /\ /\ /\ ------
	return samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples
def exercise05(n):
    # This function will find n factorial using recursion (calling itself) and return the solution. For example exercise05(5) will return 120. No Python functions are to be used.
    # ------ Place code below here \/ \/ \/ ------
    if  n==1:
        return n
    else:
        return n*exercise05(n-1)
number=int(input('enter a positive integer number\n'))
print(exercise05(number))
pass# Remove this line
    # ------ Place code above here /\ /\ /\ ------
def exercise06(n):
    # This function will receive an arbitrary list of numbers of arbitrary size and find the average of those numbers. The size of the list may vary. Find the method that requires the  least amount of code. Return back the length, sum of list and average of list
    # ------ Place code below here \/ \/ \/ ------
    n=list(n)
    length_n=len(n)
    sum_n=0
    for i in n:
        sum_n=sum_n+float(i)
    average_n=sum_n/length_n
    # ------ Place code above here /\ /\ /\ ------
    return length_n, sum_n, average_n
def exercise07(n):
    # This function looks for duplicates in list n. If there is a duplicate False is returned. If there are no duplicates True is returned.
    # ------ Place code below here \/ \/ \/ ------
    m=dict()
    for i in n:
        if i not in m:
            m[i]=1
        else:
            m[i]=m[i]+1
    p=0
    for v in m.values():
        p=p+v
    if p==len(m):
            return('true')
    else:
            return('false')
    # ------ Place code above here /\ /\ /\ ------
    # Exercise 8
	# Create a function called display_menu that receives an argument called menu. The function should do the following:
	# 1. Verify that menu is in fact a tuple. If it isnt, return back -1.
	# 2. Determine the number of elements in menu
	# 3. Loops through menu & enumerate through to the a menu to the screen. The test case will describe what the menu items are. The enumeration should be generate by code and not hardcoded.
	# 4. Using input(), asks the user to select a menu item by entering a number and hitting Enter 
	# 5. Validates if the number entered is a valid menu option and asks user to retry if number is not valid or is not a number / int
	# 6. An exit menu option should be added at the end of the displayed list of menu options allowing the user to exit selecting a menu causing the display_menu() function to return back the number of the last menu option chosen prior to exit and also return the length of menu
	# 7. If a valid menu option is chosen, call a function named similarly to the menu option that prints the menu option chosen i.e. def buy_burger() prints('Burger bought!')
	# 8. The menu options should repeatedly be displayed after each selection (and appropriate delegate function is called) until user selects exist
	# ------ Place code below here \/ \/ \/ ------
def made(item):
    print(str(item) + " made!")
def display_menu(menu):
	order = []
    user_active = True
    exit = len(menu)
	if type(menu)==type(tuple()):
		menu_list = []
        index = 1
        for i in menu:
            menu_list.append(str(index) + ' '+ i )
            index = index + 1
        menu_list.append(str(index)+ '.' +'Exit')

        len_menu = len(menu_list)
        exit_n = len_menu
        while user_active:
            print("Menu: ")
            for i in menu_list:
                print(i)
            try:
                choice = int(input("entering  a number\n"))
                if choice > len_menu:
                    print(" The number is out of range! Please type in a number on the menu")
                elif choice == exit_n:
					user_active = False
                    return len_menu,exit
                else:
                    made(menu[choice-1])
                    order.append(menu[choice-1])
            except:
                print(" Please enter integer number\n ")
    else:
        error = -1
        return error,exit
    # ------ Place code above here /\ /\ /\ ------
def exercise09():
    # Compile a list of 10 random URLs of dog pics
    import requests as  r
    dogs = []
    url = 'https://random.dog/woof.json'
    dog_media = r.get(url=url)
    print(str(dog_media.content))
    # ------ Place code below here \/ \/ \/ ------
    for  n in range(0,9):
        dogs.append(str(dog_media.content))
        dog_media=r.get(url=url)
    # ------ Place code above here /\ /\ /\ ------
    return dogs
def exercise10(sentence):
    # Exercise10 receives an arbitrary string. Return the sentence backwards with the cases inverted and spaces an underscore _, i.e. HelLo returns OlLEh
    reversed = ''
    # ------ Place code below here \/ \/ \/ ------
    m=sentence.swapcase()
    c=m.replace(' ','_')
    b=c.split()
    list1=[]
    list2=[]
    b.reverse()
    space1='_'
    space2=''
    for word in b:
        l=len(word)
        for i in range(0,l):
            list1.append(word[l-i-1])
        d=space2.join(list1)
        list2.append(d)
    reversed=space1.join(list2)
    # ------ Place code above here /\ /\ /\ ------
    return (reversed)




