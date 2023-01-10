name = "better"
# no {} in if else...rather give a ':' and write after a tab from starting
if name == "better":
        print("yess")
else:
    print("nooo")
#seperate code can be given by starting from first point
print("i dont belong to if or else")

# for loop = give 'for' and 'in' and a ':'
obj = [1,2,4,5]
for i in obj :
    print(i)

sum = 0
for i in range(1,7):
    sum = sum + i
print(sum)

for q in range (17):
    print(q)

ab = 16

while ab>1:
    if ab == 14:
        ab = ab - 1
        continue

    if ab == 9:
        break
    print(ab)
    ab = ab - 1

def Addition(a,b):
    return (a + b)

print (Addition(29,55))