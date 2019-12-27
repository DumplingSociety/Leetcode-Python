# Exercises 1: Write a while loop that starts at the last character in the string and works its way backwards
# to the first character in the string, printing each letter on a separate line, except backwards
'''
index = 1
word = 'hello'
for char in word:
    print(word[len(word)-index])
    index = index + 1
'''

# solution 2
'''
def backwards(word):
    index = len(word) - 1  # adjust for 0th index
    while index >= 0:
        print(word[index])
        index -= 1
        
word = "python"
backwards(word)


#String slices
s = 'Monty Python'
print(s[0:5]) # Monty
print(s[:3])  # Mon 
new_s = 'P' + s[:3]
print(new_s) #PMon

# Sting is immutable 


#Looping and counting

word = 'banana'
count = 0
for latter in word:
    count = count + 1
print(count)

# The in operatior 
print('a' in 'banana') # True

'''


# Exercise 4 : write an invocation that counts the number of times the letter a occurs in "banana"

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# Parsing strings
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('uct')
print(atpos)

# Format operator
camels = 42            
print('%d' % camels) # % is the format operatopr, allows us to construct strings, replacing parts of stings with data in variables
# %d means that the second operand
# should be formatted as an integer("d" stands for "decimal")
# this result is the string '42', not the integer value 42
print('I have spotted %d camels.' % camels)

# Debugging
'''
while True:
    line = input('> ')
    if len(line) > 0 and line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')    
'''

# Exercise 5 
str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(':')
final = str[atpos+1 :]
ffinal = float(final)
print('This is a floating point number %g' %ffinal) 

# Stripping
greet = '        Hello Bob '
print(greet.lstrip())
print(greet.strip())