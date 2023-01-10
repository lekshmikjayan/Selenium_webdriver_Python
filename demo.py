print("take care")

# variables...no return type...no int..automatic calculation of data type
#datatypes are present but not expressed explicitly
a = 7
print(a)

b = "Welcome home"
print(b)
# spacing is required(no spacing won't cause any error)
c, d, e, f = 92, 47, 56, "apple"
print(e)
print(d)
# concatenating string and integers...we cant concatenate 2 diff datatypes, so we do this by below format method
print("{} {} {}".format("value of f and d is ", f, d))
# for same datatypes we can concatenate by +
print(d,e)
print(type(f))
print(type(e))

#numeric datatypes  = int, float, complex...

values = [1,2,3,4, "dhbej"] #List is the DT that allows multiple values and of diff DT
print(values[2])

print(values[-1]) #returns last index of values

print(values[1:3]) #returns subindex values:  from index 1 to 3 and not the value in index 3

#how to insert values of list DT - using insert
values.insert(4, "fygewif")
print(values)

#how to add values at the end - using append
values.append(("last"))
print(values)

#how to update values - by index number
values[2] = 7
print(values)

#how to delete values in the list - using del
del values[3]
print(values)

#LIST datatype is mutable ie, can be changed later, in LIST we use []

#TUPLE = immutable (values once declared  cant be changed again once declared), here we use ()
val = (1,2,3,4,5,6,7,8)
print(val)

#Dictionary = key:value pair in {}, either key or value if any one of them is string then it shud be in ""

abc = {1: 12, 2:"ewui", 3: "qwuygeu", "vd": 43}
print(abc[2]) # prints the value of respective key mentioned
print(abc["vd"])
abc[3] = "euhfu"

print(len(abc))

#how to add key:value pair to empty dictionary
dict = {}
dict[1] = "apple"
dict[2]  ="mango"
dict[3] = "grapes"

print(dict)