# ***********************
# (Ctrl+/) comment/uncomment line(s) to verify output
# res is assigned the value of the problems extracted from quizes problems for output
# ***********************

res = 0

# res = len("Good") # string is 4 characters long

# res = max("Programming is fun") # u has the highest unicode value (117)
# res = ord("u")

# res = min("Programming is fun") # blank space is 32 in unicode

# name = [1, 2, 3, 4, 5, 6]
# res = initial = name[0] # indexing operator [i] retireves the ith element in the structure, starting from 0

# code = "abaaaaab"
# res = isValidCode = code[0] < code[-1] and code[1] > code[-2] # negative index counts from last to first starting at -1
# res = "Programming is fun"[-1] # if a string literal isn't stored, will be released next line

'''
slice operator extracts piece of an object 
[begin=0:end=-1:step=1] begin is inclusive, end is not inclusive
is for loop shortcut using range
'''
# name = "Clarence"
# res = studentCode = name[1:4]
# cityName = "Toronto"
# res = airportCode = cityName[:3]
# text = "6712345"
# res = ending = text[-5:]
# res = "Programming is fun"[4:6]
# res = "Programming is fun"[1:1]
# res = "Programming is fun"[-3 : -1]

# res = text = text.upper() # upper() returns the upper case copy of the string
# res = text = text.lower() # lower() returns the lower case copy of the string
# res = type(5.6) # decimals type are called "float"ing point value/variable

'''
Which of the following statements is false?
1) A variable that holds a value is actually a reference to an object for the value.
2) Each object has a unique id.
3) Objects of the same kind have the same type.
4) Objects of the same type have the same id.

otion 4 is flase, each object is assigned a unique id
'''

# s = "Welcome"
# res =  type(s) # string type is called 'Str' by python

# text = '      '
# res = isEmpty = text.isspace() # isspace() returns true if string is made of empty space(s)

# compare the vlaues of first and rest of the string, to their upper and lower version
# if they match, is Capitalized is true
# 
# definitelyNotText = 'value'
# first, rest = definitelyNotText[0], definitelyNotText[1:]
# res = isCapitalized = first == first.upper() and rest == rest.lower()

'''
Suppose s is "welcome". Which of the following is True? Please select all that apply.
1) s.isalpha()
2) s.isdigit()
3) s.islower()
4) s.isupper()
5) None of the above.

1 and 3
'''
# s = "welcome"
# res = s.isalpha()
# res = s.isdigit()
# res = s.islower()
# res = s.isupper()

'''
write a statement that checks whether your email starts with Dear and ends with Kind regards.. Assign the result to checkPassed.
'''
# email = 'Dear Kind regards.'
# res = checkPassed = email.startswith('Dear') and email.endswith('Kind regards.')

'''
text must:

Only contain letters and numbers;
Have the same three-characters string at the start as at the end;
And have at least three letters a in it.
Write a statement that assigns to checkPassed whether someMoreText conforms to the above test.

Examples:

The string abchelloCodeGradeabc conforms to the above tests because (1) it only contains letters, (2) it has the string abc both at the start and end, and (3) it contains 3 letters a.

The string abbhellothere!bba does not conform to the above tests because (1) it contains a non-alphanumeric character (!), (2) while the 3 characters at the beginning and end are the same, they are in a different order (abb is not bba), and (3) it contains only 2 letters a.

'''
# someMoreText = 'abchelloCodeGradeabc'
# s = someMoreText
# start, end = s[:3], s[-3:]
# res = checkPassed = s.isalnum() and start == end and s.count('a') > 2

'''
assigns to insert the portion of textAgain between the first and last ,. Assume there are at least two commas in textAgain. Assume there is always a space after each comma.

Example:

The string "This is, as you would expect, an insert" would yield "as you would expect" as insert, while "This is, as you would expect, if you know the English language, an insert" would yield "as you would expect, if you know the English language" as insert.
'''
# textAgain = "This is, as you would expect, an insert"
# t = textAgain
# res = insert = t[t.find(',') + 2: t.rfind(',')]

'''
text has been assigned a string. Write some code that assigns to updatedText:

The value of text if text contains no periods;
The uppercased version of text if text contains exactly one period;
The string of text after the second period, followed by a whitespace, and finally, the string from the beginning up to the first period.
Example

if text is "Some text. More text. Final text", updatedText will be "Final text Some text".
'''
# text = "Some text. More text. Final text"
# if not text.count("."): updatedText = text
# elif text.count(".") == 1: updatedText = text.upper()
# else:
#     second = text.find(".", text.find(".") + 1)
#     updatedText = text[second + 1:] + " " + text[:text.find(".")]
# res = updatedText

'''
Given a string s = "Welcome", what is s.count('e')?
1
2
4
3

2
'''
# res = "Welcome".count('e')

'''
Given a string s = "Programming is fun", what is s.find('ram')?
4
1
-1
3
2

4
'''
# res = "Programming is fun".find('ram')

'''
Given a string s = "Programming is fun", what is s.startswith('Program')?
0
-1
1
False
True

True
'''
# res = "Programming is fun".startswith('Program')

'''
Assignment: Usernames has the format <surname>.<name>#<unique number>. 
Assume the username is assigned to username, and its casing is random (letters may be upper- or lower-case without a pattern). Write some code that assigns to fullName the string with <name> <surname>, both name and surname should be capitalized. Capitalized means the first letter is in uppercase.
'''
# username = "Jhon.Doe#77"
# surname, name = username.split('.')
# name = name[:name.find('#')]
# res = fullName = (name + ' ' + surname).title()

'''
Assignment: Assume text has been assigned a string. Write some code that replaces all vowels (a, e, i, o, u) in text with i and assigns the result to text. Assume vowels are always lowercase.
'''
# text = 'aeiou'
# res = text = text.replace("a","i").replace("e","i").replace("i","i").replace("o","i").replace("u","i")

# is this valid?
# s = "Welcome"
# s[1] = 'r'

# res = "\t\tWelcome\n".strip()

# res =  format(345.3546, "10.3f")

print(res)
