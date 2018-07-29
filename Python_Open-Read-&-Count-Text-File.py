##Practice splitting, counting, formatting printout
##Given a file path:
##read file, count total words and lines

##open, read, close file
a = open("hello.txt")
content = a.read()
a.close()

##count words in file and format output with placeholder and word list count
words = content.split()
print("There are {0} words in the file.".format(len(words)))

##count lines in file and format output with placeholder and line list count
num_lines = sum(1 for line in open("hello.txt"))
print("There are {0} lines in the file.".format(num_lines))


