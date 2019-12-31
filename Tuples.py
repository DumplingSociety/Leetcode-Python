# Tuples are immutable
# like a list, valuies stored in a tuple can be any type, and they are indexed by integers.
# Tuples are also comparable and hashable so we can sort lists of them and use tuples as key values in Python dict

# Creat tuples
t = ('a', 'b', 'c', 'd', 'e')
t1 = ('a',)     # have to include the final comma
print(type(t1)) # <class 'tuple'>
t2 = ('a')
print(type(t2)) # <class 'str'>

# Another way of creation 
tup = 'python', 'geeks'
print(tup)       # ('python', 'geeks')
print(type(tup)) # <class 'tuple'>
# Another for doing the same 
tup = ('python', 'geeks') 
print(tup)  # ('python', 'geeks')

# Third way to constuct a tuple
t = tuple() 
print(type(t)) # <class 'tuple'>


# An empty tuple 
empty_tuple = () 
print (empty_tuple)  # ()
print(type(empty_tuple)) # <class 'tuple'>

t = ('a', 'b', 'c', 'd', 'e')
# you cant modify the elements of a tuple
t = ('A',) + t[1:]
print(t)


# Comparing tuples 
print((0, 1, 2) < (0, 3, 4)) # True

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:              # the first loop builds a list of tuples, where each tuple is a word preceded by its length
    t.append((len(word), word))
# print(t) --> [(3, 'but'), (4, 'soft'), (4, 'what'), (5, 'light'), (2, 'in'), (6, 'yonder'), (6, 'window'), (6, 'breaks')]

t.sort(reverse=True)   # sort to go in decreasing order
# print(t) --> [(6, 'yonder'), (6, 'window'), (6, 'breaks'), (5, 'light'), (4, 'what'), (4, 'soft'), (3, 'but'), (2, 'in')]
 

res = list()
for length, word in t: # traverses the list of tuples and builds a list of words in descending order of length
    res.append(word)

print(res) # ['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']

# Tuples are immutable, you cannot alter its contents - similar to a string
y = (3, 2, 1)
# y[2] = 'D' Traceback
print(type(y)) # <class 'tuple'>
# x.sort() Traceback
# x.append(5), x.reverse() Traceback

# since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memory use and performance than lists
# so when we are making temporary variables, we prefer tuples over lists

# Tuple assignment : allows you to assign more than one varible at a time when the left side is a sequence
m = ['have', 'fun'] # list
x, y = m
print(x) # have
print(y) # fun
# we can put a tuple on the left-hand side 
# we can even omit the parentheses

(x, y) = (4, 'fred')
print(y) # fred


# Tuples and Dictionaries
# itmes() method 
d = dict()
d['csev'] = 2
d['vwen'] = 4
for (k,v) in d.items(): # items() gives as a list of (key, value) tuples
    print(k, v) # csev 2  
                # vwen 4
tups = d.items()
print(tups) # dict_items([('csev', 2), ('vwen', 4)])



# sort by values instead of key
c = {'a':10, 'b':1, 'c': 22}
tmp = list()
for k, v in c.items() : # creates a list of tuples
    tmp.append((v,k))  # changed position of v and k
print(tmp)            # [(10, 'a'), (1, 'b'), (22, 'c')]
tmp = sorted(tmp, reverse=True) # sort it by value
print(tmp)            # [(22, 'c'), (10, 'a'), (1, 'b')]

# the top 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
lst = list()
for k, v in counts.items(): # items() get a list of keys and values from a dict
    newtup = (v, k)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for v, k in lst[:10]: # from 0 - 9
    print(k, v)
'''
the 3
is 3
and 3
sun 2
yonder 1
with 1
window 1
what 1
through 1
soft 1
'''

# using tuples as keys in dict
# becasue tuples are hashable and list are not
# if we want to creat a composite key to use in a dict we must use a tuple as the key
 # we could use tuple assignment in a for loop to traverse this dict
 
'''
directory[last, first] = number   # the expression in brackets is a tuple. 
 for last, first in directory:
    print(first, last, directory[last, first])
'''

"""
Exercise  10.1: Revise a previous program as follows: Read and parse the "From"
lines and pull out the addresses from the line. Count the number of messages
from each person using a dictionary.
After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the
list in the reverse order and print out the person who has the most commits.
Sample line:
From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""
lst = list()
counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] !='From' : continue     
    if words[1] not in counts:
        counts[words[1]] = 1
    else:
        counts[words[1]] += 1
        
for k, v in list(counts.items()): # get values
    newtup = (v, k)
    lst.append(newtup)
    
lst = sorted(lst, reverse=True) # sort the list in the reverse order

for v, k in lst[:1]: #
    print(k, v)


        
"""
Exercise  10.2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the "From" line by finding
the time string and then splitting that string into parts using the colon
character. Once you have accumulated the counts for each hour, print out the
counts, one per line, sorted by hour as shown below.
Sample line: From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008
Sample Execution:
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

"""
lst = list()
counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 6 or words[0] != 'From': continue
    if words[5][:2] not in counts:
        counts[words[5][:2]] = 1
    else:
        counts[words[5][:2]] += 1
        
for k, v in list(counts.items()): # get values
    newtup = (k, v)
    lst.append(newtup)  # creating a list of (key, values) tuples from the dictionary
    
lst = sorted(lst, reverse=False)
    
print(lst)
# [('04', 3), ('06', 1), ('07', 1), ('09', 2), ('10', 3), ('11', 6), ('14', 1), ('15', 2), ('16', 4), ('17', 2), ('18', 1), ('19', 1)]