import sys

while True:
  num = input("Enter a list of numbers seperated by commas and a space, like ', '.\n\n")
  list1 = [int(i) for i in num.split(", ")]
  print("Great! Now this program will give you the basic statistics of this data set, incuding mean, median,  ect.")



  #Mean
  mean = sum(list1)/len(list1)
  print("Mean: ", sum(list1)/len(list1))
  list1.sort()

  diff = [abs(mean - i) for i in list1]
  mad = sum(diff)/len(diff)
  print("The Mean Absolute Deviation is:", mad)

  user_input = input("If you want to continue, press 'a' on your keyboard.")

  if user_input == "a":
    continue
  else:
    sys.exit()