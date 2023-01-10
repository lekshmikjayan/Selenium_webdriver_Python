#raise exception

items = 0
if items != 3:
    assert (items == 0)
  #  raise Exception("wrong")

#assertion = if condtn is not true then test will be failed; condntn shud b alwys true

x = "puppy"

assert x == "puppy"

#try, catch

try:
    with open('demo.txt', r) as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning ongoing")
#finally will be executed no matter what whether there is error or not, clean up resources