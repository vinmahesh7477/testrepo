#Program to test out the strings in Python
str1= 'test'
str2="test"

#multi line string using triple quotes

str3 = """ this is a multi line quotes
to be used in multiple lines
when the value of a string is too big to fit in a single line"""

print(str1)
print(str2)
print(str3)


str1 ="Hello World"
print(str1[6])

#for x in str1:
#print(x)

vowels='a','e','i','o','u'    

strinput="aeiouabdc"
vowelCount=0

for i in strinput: 
    if i in vowels:
        vowelCount+=1

print("Number of vowels: ",vowelCount)
    
