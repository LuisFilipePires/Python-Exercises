
#read a specific line from a file
#how tum run
''' 
python3 d2.py 
File :file.txt
Line: 4'''


def read_line(fname, lnum):
	try:
		file = open(fname, "r")
		lines = file.readlines()   #read by index 
		file.close()
	except:
		print("*" * 8 + " error reading file" + "*" * 8)
		return # to stop the function
		
	total_lines = len(lines)
	
	if lnum > total_lines:
		print(str(total_lines) + " file lines.")
		print("can't read line" + str(lnum) + "!")
	else:
		line = lines[lnum -1].rstrip('\n')
		print(line)

filename = input("File :" )
line_number = int(input("Line: "))

read_line(filename, line_number)

print("*" * 8)
read_line("file.txt", 2)
read_line("file.txt", 5)
read_line("bad_file.txt", 5)

