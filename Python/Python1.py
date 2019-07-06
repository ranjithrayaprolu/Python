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


















