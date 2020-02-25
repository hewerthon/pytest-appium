ItemsInCard = 0

if ItemsInCard != 2:
    pass
    # raise Exception("Products Card count not matching")

assert (ItemsInCard == 0)

# try, catch

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except:
    print("Some how i reached this block because is failure in try block")

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Cleaning up resources")
