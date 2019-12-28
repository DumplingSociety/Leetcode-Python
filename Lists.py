
#  
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

# 
cheeses = ['cheddar', 'Edam', 'Gouda']

# Lists are mutable
print(cheeses[0])

numbers = [17, 123]
numbers[1] = 5
print(numbers)

# Traversing a list
# loop 
for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    print(numbers[i])
# nested list

nestlist = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
print(nestlist)


# + operation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
d = [0] * 4
print(d)


# List slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[0:2])

print(t[:])

# mutable
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t[:])

# List methods
t = ['a', 'b', 'c']
t.append('d')
print(t)

# extend ,adds a new element to the end 
t = ['a', 'b', 'c']
t.append('d')
# it also takes a list as an argument and appends all of the elements
t1 = ['a', 'b', 'c']
t2 = ['d', 'e', 'f']
t1.append(t2)
print(t1)
#['a', 'b', 'c', ['d', 'e', 'f']]

# sort arranges 
t = ['a', 'b', 'd', 'c', 'f', 'e']
t.sort()
print(t)

# deleteing elemetns
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
#['a', 'c']
print(x)
# b
 # if you dont need the removed value, use del
t = ['a', 'b', 'c']
del t[1]
print(t)
# ['a', 'c']

# if you know the element you want to remove, use remove
t = ['a', 'b', 'c']
t.remove('b')
print(t)

# to remove more than one element, you can use del with a slice index
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t) # ['a', 'f']

# functions
nums = [3, 41, 12, 9, 74,  15]
print(len(nums))

print(max(nums))

print(sum(nums))

# rewrite a program
'''
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print('Average:', average)'''


# Lists and strings
# string is a sequence of character, a list is a sequence of values, to convert you can use list
s = 'spam'
t = list(s) ## list breaks a string into individual letters
print(t) # ['s', 'p', 'a', 'm']
 
# break a sting into words, use split
s = 'pining for the fjords'
t = s.split()
print(t)
print(t[2])


# you can specify what delimiter character to sue in the splitting
s = 'spam-spam-spam'
delimiter = '-'
print(s.split(delimiter)) # s.split('-')


# join is the inverse of split
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
print(delimiter.join(t)) 


#Parsing lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Form '): continue
    words = line.split()
    email = words[1]
    piece =email.split('@') # double split 
    print(words[2])
    print(piece[1])

# Objects and values
a = 'banana'
b = 'banana'
print(a is b) # True, a and b both refer to a string, there are two possible states: Variables and Objects
# In hrere, python only created one sting bject, and both a and b refer to it.

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False, since the two lists have the same elements, but not idetical, they are not the same 
# object

# Aliasing
a = [1, 2, 3]
b = a  # an object with more than one refernce has more than one name, we say the object is aliased
print(b is a) # True, the association of a variable with an object is called a reference. here, two refer 
#  to the same object

b[0] = 17
print(a)  # [17, 2, 3] , aliased object is mutable, changes made with one alias affect the other

# in general , it is safer to aviod aliasing when you working with mutable objects

# for immutable objects like strings, aliasing is not as much of a problem
a = 'banana'
b = 'banana'

# List arguments
def delete_head(t):
    del t[0]
letters = ['a', 'b', 'c']
delete_head(letters)
print(letters) # ['b', 'c'] the parameter t and the variable letters are aliases for the same object

# it is important to distinguish between operations that modify lists and operations that create new lists
# the append method modifies a list, but + creates a new lists
t1 = [1, 2]
t2 = t1.append(3)
print(t1) # [1, 2, 3]
print(t2) # None
 
t3 = t1 + [3]
print(t3) # [1, 2, 3, 3]
print(t2 is t3) # False

# example of the differences 
def bad_delete_head(t):
    t = t[1:]
# WRONG
# slice creates a new list and the assignment makes t refer to it, but non of that has any effect 
# on the list that we passed as an arguiment

# An alternative
def tail(t):
    return t[1:]
# tail returns all but the first element of a list
letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest) # ['b', 'c']

# Exercise 1: write a function called chop that takes a list and modifies it, removing the first and last elements, and
# returns None. Then write a function called middle that takes a list and returns a new list that contains all but 
# the first and last elements

def chop(t):
    del t[0]
    del t[-1]

letters = ['a', 'b', 'c']
chopped = chop(letters)
print(chopped)


def middle(nt):
    newlist = nt[1:-1]
    return newlist
letters = ['a', 'b', 'c', 'd', 'e']
middled = middle(letters)
print(middled)

# Debugging
# most list methods modify the argument and return None. This is the opposite of the string methods, which return a new string and leave the orignal alone
t = t.sort() # WRONG!
# sort returns None

# make copies to avoid aliasing
# orig = t[:]
# t.sort()
# want to use a method like sort, but also keep the original list 

# can also use sorted, which returns a new, sorted list band leaves the original alone. but avoid using sorted as a variable name
letters = ['a', 'b', 'c', 'd', 'e']
# print(letters.sorted())

# Debugging

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
#    print('Debug: ', words)
    if len(words) == 0: continue  # put this if in the frist, if we have zero words, 
# we use continue to skip to the next line
    if words[0] !='From': continue  # the error occurs when it encounters a blank line! >>> Debug:  []
    print(words[2])
    
# Exercise 3: rewite the guardian code in the above example without two if statements. Instead, use a compound
# logical expression using the and logical opeator with a single if statement
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] !='From': continue
    print(words[2])

# Exercise 4: write a program to open the file romeo.txt and read it line by line. For each line, split the line
# into a list of words using the split function. For each word, check to see if the word is already in a list. If the 
# word is not in the list, add it to the list. When the program completes, sort and print the resulting words in 
# alphabetical order

inp_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east',
'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick',
'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
fhand = open('romeo.txt')
for line in fhand:
    word = line.split()
    if word in inp_list: continue
    inp_list.append(word)
#print(sorted(inp_list))    
     

# Exercise  8.5: Write a program to read through the mail box data and when you
# find the line that starts with "From", you will split the line into words
# using the split function. We are interested in who sent the message, which is
# second word on the From line.
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a
# count at the end.
# This is a good sample output with a few lines removed:
'''
python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[... some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
'''
count = 0
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue
    print(words[1])
    count += 1
print('There were %d lines in the file with From as the first word' % count)


"""
Exercise  8.6: Rewrite the program that prompts the user for a list of numbers
and prints out the maximum and minimum of the numbers at the end when the user
enters "done". Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum
numbers after the loop completes.
Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
"""

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        value = float(inp)
    except ValueError:
        print('Invalid input')
        quit()
        
    numlist.append(value)
    maxnum = max(numlist)
    minnum = min(numlist)
print('Maximum: ', maxnum)
print('Minimum: ', minnum)

