greeting = "Good Morning"

if greeting == "Good Morning":
    print("This correct: " + greeting)


# for loop

obj = [0,1,2,3,4,5]

for i in obj:
    print(i*2)
print("**********")
# sum of First Natural numbers 1 + 2 + 3 + 4 + 5 + 6 = 21
summation = 0
for j in range(1, 6):   # range(i, j -> i to j-1
    summation = summation + j
print(summation)

print("**********")

for k in range(1, 10, 2):
    print(k)
