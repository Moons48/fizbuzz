"""Fizzbuzz app for Thinkful Class"""

def initial():
    """"Verifies validity of user input"""
    print ("Let\'s play FizzBuzz!")
    print ("FizzBuzz starts at the number 0... but where would you like to end?")
    end = input()
    if end.isnumeric():
        game(end)
    else:
        print ("Not a number! Try again!")
        initial()

def game(i):
    """"Conducts FizzBuzz caluclations""""
    for i in range(0,int(i)):
        if i%3 == 0 and i%5 == 0:
            print ("**Fizz Buzz**")
        elif i%3 == 0:
            print ("*Buzz*")
        elif i%5 == 0:
            print ("*Fizz*")
        else:
            print int(i)
        
initial()

""" FizzBuzz with exception handling"""
def initial():
    print ("Let\'s play FizzBuzz!")
    print ("FizzBuzz starts at the number 0... but where would you like to end?")
    end = input()
    try:
        int(end)
        game(end)
    except ValueError:
        print ("Not a number! Try again!")
        initial()

def game(i):
    for i in range(0,int(i)):
        if i%3 == 0 and i%5 == 0:
            print ("**Fizz Buzz**")
        elif i%3 == 0:
            print ("*Buzz*")
        elif i%5 == 0:
            print ("*Fizz*")
        else:
            print int(i)
        
initial()





"""Another version with a countdown"""
"""Fizzbuzz app for Thinkful Class"""
import time

def initial():
    print "Let\'s play FizzBuzz!"
    print "FizzBuzz starts at the number 0... but where would you like to end?\n\nYou have 10 seconds to choose, or the game defaults to 100"
    for i in range(0,10):
        time.sleep(1)
        if i == 0:
            end == 10
    end = raw_input()
    if end.isdigit():
        game(end)
    else:
        print "Not a number! Try again!"
        initial()

def game(i):
    for i in range(0,int(i)):
        if i%3 == 0 and i%5 == 0:
            print "**Fizz Buzz**"
        elif i%3 == 0:
            print "*Buzz*"
        elif i%5 == 0:
            print "*Fizz*"
        else:
            print int(i)
        
initial()