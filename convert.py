import re

myinput = input("Please input the conversion you would like to do: ")
#example input: 100 miles to feet
splitext = myinput.split(" ")

number = int(splitext[0])
beginning_unit = splitext[1]
end_unit = splitext[3]

print("to clarify, you want to convert from {} {} to a certain number of {}".format(number,beginning_unit,end_unit))

