##String methods:
##1. Reverse a string.
##method: 1
##a='apple'
##b=''
##for i in a:   
##    b=i+b   
##print(b)

##method: 2(using slicing)
##a='apple'
##b=a[::-1]
##print(b)

##2. check whether a string is palindrome or not.
##a='mam'
##b=a[::-1]
##if a==b:
##    print('The string is a palindrome')
##else:
##    print('The string is not a palindrome')

##3.count number of vowels in a string.
##a='always happy me'
##b=0
##for i in a:
##    if i in 'aeiouAEIOU':
##        b=b+1
##print(b)

##4.count number of consonants in a string.
##a='always happy me'
##b=0
##for i in a:
##    if i.isalpha() and i not in('aeiouAEIOU'):
##        b=b+1
##print(b)

##5.count total characters(alphabets) in a string.
##method:1
##a='always happy me'
##b=len(a)
##print(b)

##method:2
##a='always happy me'
##b=0
##for i in a:
##    b=b+1
##print(b)

##6&7. convert string to uppercase & lowercase.
##method:1
##a='attitude matters'
##b=a.upper()
##print(b)
##c=a.lower()
##print(c)

##method:2
##a='efforts matters'
##b=''
##for i in a:
##    if 'a' <= i <= 'z':
##        b = b + chr(ord(i) - 32)
##    else:
##        b = b+i
##print(b)

##To lower case.
##a='efforts matters'
##b=''
##for i in a:
##    if 'A'<=i<='Z':
##        b=b+chr(ord(i)+32)
##    else:
##        b=b+i
##print(b)

##8.Remove spaces from a string.
##method: 1
##a='take one task at a time'
##b=''
##for i in a:
##    if i != ' ':
##        b=b+i
##print(b)

##method:2
##a='take one task at a time'
##b=a.replace(' ','')
##print(b)

##method:3
##a='take one task at a time'
##how to use split:
##b=a.split()
##print(b)

##b=''.join(a.split())
##print(b)

##9.count number of words in a string.
##method: 1(output shows the total words count(7))
##a='fear is temporary but regret is permanent'
##b=a.split()
##c=0
##for d in b:
##    c=c+1
##print(c)
##
##method:2(output shows the total words count(7))
##a='fear is temporary but regret is permanent'
##b=len(a.split())
##print(b)

##method:3(output shows the total alphabets counts(35))
##a='fear is temporary but regret is permanent'
##b=0
##for d in a:
##    if d != ' ':
##        b=b+1
##print(b)

##method:4(output shows the total words counts(7))
##a='fear is temporary but regret is permanent'
##b=0
##c=False
##for d in a:
##    if d != ' ' and c==False:
##        b=b+1
##        c=True
##    elif d == ' ':
##        c=False
##print(b)

##10.find first occurance of a character(any alphabets in a string).
##a='comfort makes you discomfort'
##b='t'
##c=a.find(b)
##print(c)

##11.find last occurance of a character.
##a='comfort makes you discomfort'
##b='t'
##c=a.rfind(b)
##print(c)

##12.Replace all spaces with hyphen.
##a='comfort makes you discomfort'
##b=a.replace(' ','-')
##print(b)

##13.check whether string contains only digits.
##a=input('enter the string: ')
##if a.isdigit():
##    print('the string contains only digits')
##else:
##    print('the string doesnt contains only digits')

##14.compare two strings without using equals.
##a ="hi"
##b ="hi"
##if len(a) != len(b):
##    print("Strings are not equal")
##else:
##    c = True
##
##    for i in range(len(a)):
##        if a[i] != b[i]:
##            c = False
##            break
##
##    if c:
##        print("Strings are equal")
##    else:
##        print("Strings are not equal")

##using equals:
##a='hi'
##b='hi'
##if a==b:
##    print('strings are equal')
##else:
##    print('strings are not equal')

##15.concatenate two strings.
##method:1
##a='hello'
##b='world'
##c=a+b
##print(c)

##method:2
##a='hello'
##b='world'
##c=''.join([a,b])
##print(c)

##method:3(if u want space in between two strings)
##a='hello'
##b='world'
##c=' '.join([a,b])
##print(c)

##16. remove duplicate characters from string.
##a='programming'
##b=''
##for i in a:
##    if i not in b:
##        b=b+i
##print(b)

##17. find frequency of each character.(frequency-how many times a letter is repeated in a word.)
##eg: hello-h-1, e-1, l-2, o-1.
##a='hello'
##b={}
##for i in a:
##    if i in b:
##        b[i]=b[i]+1
##    else:
##        b[i]=1
##print(b)

##18.count uppercase, lowercase, digits, special characters.
##a = "Hello@123World!"
##uppercase = 0
##lowercase = 0
##digits = 0
##special = 0
##for i in a:
##    if i.isupper():
##        uppercase = uppercase + 1
##    elif i.islower():
##        lowercase = lowercase + 1
##    elif i.isdigit():
##        digits = digits + 1
##    else:
##        special = special + 1
##print("Uppercase:", uppercase)
##print("Lowercase:", lowercase)
##print("Digits:", digits)
##print("Special characters:", special)
##
##19.Reverse each word in a sentence.
##a = "an apple a day keeps the doctor away"
##b = a.split()
##c = ""
##for i in b:
##    c = c + i[::-1] + " "
##print(c)

##20.find largest word in a sentence.
##a = "python is very boring"
##b = a.split()
##c = ""
##for i in b:
##    if len(i) > len(c):
##        c = i
##print("Largest word:", c)

##21.check whether two strings are anagrams.
##a = "listen"
##b = "silent"
##if sorted(a) == sorted(b):
##    print("The strings are anagrams")
##else:
##    print("The strings are not anagrams")

##method: 2
##a = "listen"
##b = "silent"
##if len(a) != len(b):
##    print("Not anagrams")
##else:
##    c = {}
##    for i in a:
##        if i in c:
##            c[i] = c[i] + 1
##        else:
##            c[i] = 1
##
##    for i in b:
##        if i in c:
##            c[i] = c[i] - 1
##        else:
##            c[i] = -1
##
##    if all(value == 0 for value in c.values()):
##        print("Anagrams")
##    else:
##        print("Not anagrams")

##22.
