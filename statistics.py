num = input("Enter a list of numbers seperated by commas and a space, like ', '.\n\n")
list1 = [int(i) for i in num.split(", ")]
print("Great! Now this program will give you the basic statistics of this data set, incuding mean, median,  ect.")

#Mean
print("Mean: ", sum(list1)/len(list1))
list1.sort()

#Median
if len(list1) % 2 == 0:
    print("Median: ", ((list1[len(list1) // 2] + list1[len(list1) // 2 - 1]) / 2))
else:
    print("Median: ", list1[len(list1) // 2])

#Mode
set1 = set(list1)
oc = {i:list1.count(i) for i in set1}
x = max(oc.values()) if max(oc.values()) > 1 else None
for i in oc:
    if oc[i] == x:
        print("Mode: ", i)

#Range
print("Range: ", list1[-1] - list1[0])