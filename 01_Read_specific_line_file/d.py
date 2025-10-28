
#read a specific line from a file

filename = input("File :" )
line_number = int(input("Line: "))

file = open(filename, "r")
lines = file.readlines()   #read by index 
file.close()


#the output prints a extra newline
#to stop this use rstrip('\n')
line = lines[line_number -1].rstrip('\n')
print(line)


total_lines = len(lines)


if line_number > total_lines:
	print(str(total_lines) + " file lines.")
	print("can't read line" + str(line_number) + "!")
else:
	line = lines[line_number -1].rstrip('\n')
	print(line)

