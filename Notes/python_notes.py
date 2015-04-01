# Python notes

# basic printing
test="Hello people"
print (test)
print (len(test))

# string stuff
name = "Pete"
quest = "Bitches"
print ("Ah, so your name is %s, your quest is %s" % (name, quest))

# string methods
'''
s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
s.strip() -- returns a string with whitespace removed from the start and end
s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
'''

# conditonal statements
a = 20
if a >= 22:
	print ("if")
elif a >= 21:
	print ("elif")
else:
	print ("else")


# functions
def someFunction(a,b):
	print (a+b)
someFunction(12,451)


# for loop
for a in range(1,3):
	print(a)


# while loop
num=1
while num <=10:
	print (num**2)
	num+=1

import random
print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print ("Sorry, you lose!")
        break
    count += 1
else:
    print ("You win!")


# Lists
'''
listname.append(value) - appends element to end of the list
listname.count('x') - counts the number of occurrences of 'x' in the list
listname.index('x') - returns the index of 'x' in the list
listname.insert('y','x') - inserts 'x' at location 'y'
listname.pop() - returns last element then removes it from the list
listname.remove('x') - finds and removes first 'x' from list
listname.reverse() - reverses the elements in the list
listname.sort() - sorts the list alphabetically in ascending order, or numerical in ascending order
'''
samplelist=[1,2,3,4,5]
for a in samplelist:
	print (a)

animals=["ant", "bat", "cat"]
print (animals.index("bat"))
animals.insert(1, "dog")

start_list=[1,2,3,4]
square_list=[]
for a in start_list:
	square_list.append(a**2)
square_list.sort()

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a<b:
        print (b)
    elif a>b:
        print (a)
else:
	print ("Else at the end of FOR loops execute if loop completed normally")

# List Comprehension: builds lists according to some logic
new_list=[x**2 for x in range(1,11) if (x**2)%2==0]
squares = [x**2 for x in range(10)]
mylist = [{'age':x} for x in range(1,10)] #create a list of dictionaries


# Dictionaries
my_dict = {
    "fish": ["c", "a", "r", "p"],
    "cash": -4483,
    "luck": "good"
}
print (my_dict["fish"][0])

for x in my_dict:
	print (my_dict[x])

for k,v in my_dict.items():
    print (k, v)


# filter and lamba
cubes=[x**3 for x in range(1,11)]
print (filter(lambda x: x%3==0, cubes))