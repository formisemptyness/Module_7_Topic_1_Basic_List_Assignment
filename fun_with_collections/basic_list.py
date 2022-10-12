'''
Program: basic_list.py
Author: Joshua M McGinley
Last Date Modified: 10/12/2022

In PyCharm, set up Module7. Declare a directory fun_with_collections.
Write a python file basic_list.py and declare two functions make_list() to return a list of user input while and
get_input() to get one input and return it.
Write the function get_input() function

    prompt user for input
    do not worry about validating input

Write the function make_list(num) that

    asks for a given number of user input (num) in a loop by
        a call to get_input()
            returns a string
            casts the input to desired type, raising exception on non-numeric input
        there are a few loop options:
            while loop, using symbolic constant
            for loop with range()
    stores them in a list
        There are a a few options to add to your list.
            .append(value)
            use a variable to get input then .insert(index,object)
    returns the list


Write your main to call your function with various numbers.
print(make_list(1))
print(make_list(2))
print(make_list(3))
This is worth 5 points.

If it helps, think of it like this: Your driver code will call make_list, which will (loop) to call get_input() an
'num' of times which will return a value each time. Do input validation, if it passes add it to the list. return
that list back to the driver, which will print it.
Using the above examples, in the make_list(1) case, make_list should be called once, and get_input will be called
once.
make_list(2) will call make_list once, and call get_input twice.
make_list(3) will call make_list once, and call get_input thrice. etc
'''

def get_input():
    userinput = str(input('Input number: '))
    return userinput

def make_list(num):
    count = 0
    list = []
    while(count < num):
        value = get_input()
        try:
            float(value) and int(value)
        except:
            print('Danger, Danger')
        list.append(value)
        count = count + 1
    return list

if __name__ =='__main__':
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))
