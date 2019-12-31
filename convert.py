conversions = []

def get_data():
    table = open("table.txt","r").read()
    table_lines = table.split('\n')
    for line in table_lines:
        chunks = line.split(' ')
        #number unit = number unit
        first_number = int(chunks[0])
        first_unit = chunks[1]
        if first_unit[len(first_unit)-1] == "s":
            first_unit = first_unit[:len(first_unit)-1]
        second_number = int(chunks[3])
        second_unit = chunks[4]
        if second_unit[len(second_unit)-1] == "s":
            second_unit = second_unit[:len(second_unit)-1]
        conversions.append([{"unit":first_unit,"value":first_number},{"unit":second_unit,"value":second_number}])
get_data()

def convert(unit,value,to):
    global conversions
    for conversion in conversions:
        if [conversion[0]["unit"], conversion[1]["unit"]] == [unit, to]:
            return (value/conversion[0]["value"])*conversion[1]["value"]
            break
        if [conversion[0]["unit"], conversion[1]["unit"]] == [to, unit]:
            return (value/conversion[1]["value"])*conversion[0]["value"]
            break
    else:
        raise Exception("Conversion not found")

input = input("What conversion would you like to do? (Ex. \"10 days to years\"): ").split(" ")

input_unit = input[1]
if input_unit[len(input_unit)-1] == "s":
    input_unit = input_unit[:len(input_unit)-1]
input_value = int(input[0])
input_to = input[3]
if input_to[len(input_to)-1] == "s":
    input_to = input_to[:len(input_to)-1]
    
try:
    print("{} {}s is equivalent to {} {}s".format(input_value,input_unit,convert(input_unit, input_value, input_to),input_to))
except:
    units = {input_unit:input_value}
    found_yet = False
    while not found_yet:
        for conversion in conversions:
            if conversion[0]["unit"] in units.keys():
                units[conversion[1]["unit"]] = (units[conversion[0]["unit"]]/conversion[0]["value"])*conversion[1]["value"]
            elif conversion[1]["unit"] in units.keys():
                units[conversion[0]["unit"]] = (units[conversion[1]["unit"]]/conversion[1]["value"])*conversion[0]["value"]
        if input_to in units.keys():
            print("{} {}s is equivalent to {} {}s".format(input_value,input_unit,units[input_to],input_to))
            found_yet = True
        else:
            print(units)
