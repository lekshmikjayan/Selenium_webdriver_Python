file = open('demo.txt')
#print(file.readline())# read line by line
#print(file.readline())
#print(file.read())


abc = file.readline()
while abc != "":
    print(abc)
    abc = file.readline()






#for each line by line...for line infile.readlines() can be also used
#file can be open and close in one single step, ie,
        #with open('sample.text', 'r')as reader
# : 'r' depicts tat file is open in read mode
 # with open('sample.text', 'w')as writer // write mode

with open ('demo.txt') as reader:
     content = reader.readlines()
     reversed(content)

     with open('demo.txt', 'w') as writer:
         for line in reversed(content):
             writer.write(line)

file.close()