#First make functioning game 
#then as extra challenge scoresheet
#extra extra challenge: would you like to play with integers or floating point numbers?
import random
import string


#helper functions
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


#main functions
def decimal_to_binary(number):
    remainder = []
    num = number
    while(num!=0):
        rem = num%2
        remainder.append(int(rem))
        new_num = num/2
        num = truncate(new_num)
    result = remainder.reverse()
    return result
    
def binary_to_decimal(number):
    #use list comprehension to convert number 
    #to list of integers
    num = [int(x) for x in str(number)]
    power= len(num)-1
    result = 0
    for i in num:
        result += i * (2**power)
        power -= 1
    return result

def decimal_to_hexadecimal(number):
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    remainder = []
    num = number
    while(num!=0):
        rem = num%16
        remainder.append(int(rem))
        new_num = num/16
        num = truncate(new_num)
    result = ""
    remainder.reverse()
    for x in remainder:
        result += str(hex[x])
    return result

def hexadecimal_to_decimal(number):
    hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex_num = [x for x in str(number)]
    num = []
    for i in hex_num:
        num.append(hex.index(i))
    power = len(num)-1
    result = 0
    for i in num:
        result += i * (16**power)
        power -= 1
    return result


#randomly pick a game
def random_conv_pick():
    game = random.randrange(1, 5)
    number = 0
    if(game == 1):
        print("I got it, we will be converting decimal to binary numbers!")
        #generate number
        number = random.randrange(1, 999)
        #ask for calculation
        print("What is the binary expression for the decimal number {number}?".format(number=number))
        input_result = input("please enter your answer: ")
        #compare results
        result = decimal_to_binary(number)
        if (input_result==result):
            print("Correct! The right answer is {result}".format(result=result))
        else:
            print("Wrong! You submitted {input_result} as your final answer but the right one is: {result}".format(input_result=input_result, result=result))

    elif(game == 2):
        print("I got it, we will be converting binary to decimal numbers!")
        #generate number
        binary = []
        count = 0
        while(count!=8):
            num = random.randrange(0,2)
            binary.append(num)
            count += 1
        number = ''.join(str(e) for e in binary)
        #ask for calculation
        print("What is the decimal expression for the binary number {number}?".format(number=number))
        input_result = input("please enter your answer: ")
        #compare results
        result = binary_to_decimal(number)
        if (input_result==result):
            print("Correct! The right answer is {result}".format(result=result))
        else:
            print("Wrong! You submitted {input_result} as your final answer but the right one is: {result}".format(input_result=input_result, result=result))


    elif(game == 3):
        print("I got it, we will be converting decimal to hexadecimal numbers!")
        #generate number
        number = random.randrange(1, 999)
        #ask for calculation
        print("What is the hexadecimal expression for the decimal number {number}?".format(number=number))
        input_result = input("please enter your answer: ")
        #compare results
        result = decimal_to_hexadecimal(number)
        if (input_result==result):
            print("Correct! The right answer is {result}".format(result=result))
        else:
            print("Wrong! You submitted {input_result} as your final answer but the right one is: {result}".format(input_result=input_result, result=result))


    else:
        print("I got it, we will be converting hexadecimal to decimal numbers!")
        #generate number
        number = "".join([random.choice(string.hexdigits[:16]) for x in range(5)])
        #ask for calculation
        print("What is the decimal expression for the hexadecimal number {number}?".format(number=number))
        input_result = input("please enter your answer: ")
        #compare results
        result = hexadecimal_to_decimal(number)
        if (input_result==result):
            print("Correct! The right answer is {result}".format(result=result))
        else:
            print("Wrong! You submitted {input_result} as your final answer but the right one is: {result}".format(input_result=input_result, result=result))


print("---------------------------------------------------------------------------------------------")
print("    w  e  l  c  o  m  e    t  o    t  h  e    m  a  t  h  s     c  h  a  l  l  e  n  g  e    ")
print("---------------------------------------------------------------------------------------------")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
name = input("Please enter your name here:")
print("Hello {name}, would you like to play a game of Convertion or Calculation?".format(name=name))
game_choice = input("Select 0 for Convertion and 1 for Calculation:")
if game_choice=="0":
    print("You chose to solve a Convertion problem! Let me find you something appropriate...")
    random_conv_pick()
else:
    print("You chose to solve a Calculation problem! Let me find you something appropriate...")


#would you like to play 0 Convertion or 1 Calculation?

#------Convertion---------
#randomly choose a conversion prompt
#prompt user to convert random number
#check result and add to scoresheet

#------Calculation--------
#randomly choose a calculation prompt
#prompt user to calculate 2 random numbers

