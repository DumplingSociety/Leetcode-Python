# Dictionary is like a list. In a list, the index positions have to be integers
# in a dic the indices can be any type
eng2sp = dict()
print(eng2sp) # {} repersent an empty dictionary
eng2sp['one'] = 'uno' # this creats an item from the key 'one' to the value "uno"
print(eng2sp) # {'one': 'uno'}
eng2sp = {'one': 'uno', 'two': 'dos','three':'tres'}
print(eng2sp) # {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp['two']) # dos
print('one' in eng2sp) # True
# to see whhether something appears as a value in a dictionary, use the method values, which returns the value 
vals = list(eng2sp.values())
print('uno' in vals) # True

"""
Exercise  9.1: Write a program that reads the words in words.txt and stores
them as keys in a dictionary. Download a copy of the file from
https://www.py4e.com/code3/words.txt. It doesn't matter what the values are.
Then use the 'in' operator as a fast way to check whether a string is in the
dictionary.
Solution by Xiangwei Li, Dec 28, 2019
"""
count = 0
wordsdict = dict()
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in wordsdict: continue
        wordsdict[word] = count
print(wordsdict)
print('newfound' in wordsdict)

# Dictionary as a set of counters
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

# get method, takes a key and a default value. if the key appears in the dict, get returns the corresponding value
# otherwise it returns the default value
counts = {'chuck' : 1, 'annie' : 42, 'jan': 100}
print(counts.get('jan', 0)) # return 100
print(counts.get('tim', 0)) # return 0

# we can use get to write our histogram loop more concisely.
# coz get automatically handles the case where a key is not in dict
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1 # d[b] = 0 + 1 
print(d)
print("\n")
# {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

# Dictonaries and files
# One common uses of a dict is to count the occurence of words in a file 


#fname = input('Enter the file name: ')
fname = 'romeo.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts = dict() 
for line in fhand:   # outer loop is reading the lines of the file
    words = line.split()  #  
    for word in words:   # inner loop is iterating throught each of the word on that particular line
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1 # equivalent to counts[word] + 1
print(counts)
            


# looping and dictionaries
# it traverses the keys of the dict
counts = {'chuck' : 1, 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
print("\n")
'''
chuck 1
annie 42
jan 100
'''

# find all the entries in a dict with a value > 10
counts = {'chuck' : 1, 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
print("\n")
        
# print kyes in alphabetical order
counts = {'chuck' : 1, 'annie' : 42, 'jan': 100}
lst = list(counts.keys()) # get values: ['chuck', 'annie', 'jan']
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])
print("\n")
# ['chuck', 'annie', 'jan']
# annie 42
# chuck 1
# jan 100

# advanced text parsing
import string
print(string.punctuation) 
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# split func looks for spaces and treats words as tokens searated by spaces, we would treat the words "soft!" and "soft" diffently
# herer we can solve this problem by suing string methods.
# translate is 
fname = 'romeo.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation)) # line.translate(str.maketrans(fromstr, tostr, deletestr))  here we use deletestr to del all punctuation
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)            
print("\n")

# {'but': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'it': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'juliet': 1, 'sun': 2, 'arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}


#Debugging
# Scale down the input
# Check summaries and types
# Write self-checks
# pretty print the output

# hashtable: the algorithm used to implement Python diciionaries
# hash function: A function used by a hashtable to compute the location for a key 
# histogram: a set of counters

"""
Exercise  9.2: Write a program that categorizes each mail message by which day
of the week the commit was done. To do this, look for lines that start with
"From", then look for the third word and keep a running count of each of the
days of the week. At the end of the program, print out the contents of your
dictionary (order does not matter).
Sample Line: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
Solution by Xiangwei Li, Dec 28, 2019
"""

counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue # <3 means it filters records that contain no data 
    if words[2] not in counts:
        counts[words[2]] = 1
    else:
        counts[words[2]] += 1
print(counts)
print("\n")

#{'Sat': 1, 'Fri': 20, 'Thu': 6}

"""
Exercise  9.3: Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from each email
address, and print the dictionary.
Enter file name: mbox-short.txt
{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3,
'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5,
'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1,
'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1,
'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}
Solution by Xiangwei Li, Dec 28, 2019
"""

counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue # <3 means it filters records that contain no data 
    if words[1] not in counts:
        counts[words[1]] = 1
    else:
        counts[words[1]] += 1
print(counts)
print("\n")
# {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}
"""
Exercise  9.4: Add ccode to the above program to figure out who has the most
mesasges in the file.
After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Chapter 5: [maximumloop]) to
find who has the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.ed 5
Enter a file name: mbox.txt
zqian@umich.edu 195

Solution by Xiangwei Li, Dec 28, 2019
"""
email_address = ''
largest = None
counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue # <3 means it filters records that contain no data 
    if words[1] not in counts:
        counts[words[1]] = 1
    else:
        counts[words[1]] += 1

for itervar in counts:
    if largest is None or counts[itervar] > largest :
        largest = counts[itervar]
        email_address = itervar
#        print(itervar)   # stephen.marquard@uct.ac.za...
print(email_address, largest)

print("\n")
# cwen@iupui.edu 5

"""
Exercise  9.5: This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e., the
whole email address). At the end of the program, print out the contents of
your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
['media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1,
'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""

counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue
    atpos = words[1].find('@')   # stephen.marquard@uct.ac.za  --> atpos = 16
    domain = words[1][atpos+1: ] # 
    if domain not in counts:
        counts[domain] = 1
    else:
        counts[domain] += 1
print(counts)
# {'uct.ac.za': 6, 'media.berkeley.edu': 4, 'umich.edu': 7, 'iupui.edu': 8, 'caret.cam.ac.uk': 1, 'gmail.com': 1}