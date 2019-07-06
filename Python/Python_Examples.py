# Print less value if the numbers are even & higher if the one of the numbers is odd
def lesser(x,y):
    if(x %2 == 0 and y%2 == 0):
        if(x<y):
            return x
        else:
            return y
    elif(x%2 == 0 or y%2 == 0):
        if(x<y):
            return y
        else:
            return x

lesser(10,100)

####

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
lesser_of_two_evens(10,12)


# Problem 2:
#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same #letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


animal_crackers('Levelheaded Llama')

#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, #return False
def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20

def sum_20(x,y):
    if(x+y == 20):
        return True
    elif(x == 20 or y==20):
        return True
    else:
        return False

sum_20(30,10)

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def capitalize(x):
    if(len(x)>3):
        return x[:3].capitalize()+x[3:].capitalize()
capitalize('Old Macdonald')

#
#MASTER YODA: Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

def master_yoda(x):
    return ' '.join(x.split()[::-1])

master_yoda('I need a mentor')

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(x):
    return ((abs(100-x)<=10 or (abs(200-x)<=10)))
almost_there(130)

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
        else:
            return False


has_33([1,3,1])

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    result =''
    for char in text:
        result += char*3
    return result

paper_doll('xyz')

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
blackjack(5,6,7)

#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(nums):
    total = 0
    add = True
    for num in nums:
        while add:
            if(num != 6):
                total += num
                break
            else:
                add = False
        while not add:
            if(num != 9):
                break
            else:
                add = True
                break
    return total


#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works

return len(code) == 1

spy_game([1,2,4,1,0,7,5])

#Write a function that returns the number of prime numbers that exist up to and including a given number¶

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
count_primes(100)

#Functions and Methods Homework
def vol(rad):
    return 4/3*3.14*rad**3

vol(2)

#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(number, low, high):
    if number in range (low, high):
        print('{} is in the range of {} {}' .format(number, low, high))
    else:
        print('number is out of range')
ran_check(3,7,10)

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output :
#No. of Upper case characters : 4
#No. of Lower case Characters : 33

def up_low(s):
    d={"upper": 0 , "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass

print("Original String : ", s)
print("No. of Upper case characters : ", d["upper"])
print("No. of Lower case Characters : ", d["lower"])

up_low('To Test The Upper And Lower')

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def uniq_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

uniq_list([1,1,1,1,2,2,3,3,3,3,4,5])










