#Dictionary:
##a={'name':'karthiga'}
##b={'name':'karthiga','age':'20','course':'python','year':'2026'}
##print(a)
##print(b)

#1.write a Python script to add a key to a dictionary.
##a={'name':'karthiga'}
##b={'age':'20','course':'python','year':'2026'}
##b.update(a)
##print(b)

##2. Write a Python script to concatenate the following dictionaries to 
##create a new one.
##Sample Dictionary :
##Dic1={1:10,2:20}
##Dic2={3:30,4:40}
##Dic3={5:50,6:60}
##Dic1.update(Dic2)
##Dic1.update(Dic3)
##print(Dic1)

##3. Write a Python program to iterate over dictionaries using for loops.
##Dic1={1:10,2:20,3:30,4:40}
##for keys in Dic1:
##    print(keys)
##for values in Dic1:
##    print(values)
##for keys,values in Dic1:
##    print(keys,values)

##4. Write a Python script to print a dictionary where the keys are 
##numbers between 1 and 15 (both 
##included) and the values are the square of the keys.
##Sample Dictionary(output)
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 
##12: 144, 13: 169, 14: 196, 15: 225}.
##d={}
##for i in range (1,16):
##    d[i]=i*i #d[i]--denotes key value(here is the key) and i*i is the value.
##print(d)

##5. Write a Python script to merge two Python dictionaries.
##a={'name':'karthiga'}
##b={'name':'karthiga','age':'20','course':'python','year':'2026'}
##a.update(b)
##print(a)

##6. Write a Python program to sum all the values in a dictionary.
##a={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
##b=0
##for i in a.values():
##    b=b+i
##print(b)

##7.Write a Python program to map two lists into a dictionary.
##keys=["name","age","course"]
##values=["Karthiga",20,"Python"]
##d=dict(zip(keys, values))
##print(d)

##8. Write a Python program to remove duplicates from the dictionary.
##d={"a": 10,"b": 20,"c": 10,"d": 30,"e": 20}
##new_d={}
##for key, value in d.items():
##    if value not in new_d.values():
##        new_d[key] = value
##print(new_d)

##9. Write a Python program to get the key, value and item in a dictionary.
##d={"a": 10,"b": 20,"c": 10,"d": 30,"e": 20}
##print(d.keys())
##print(d.values())
##print(d.items())
