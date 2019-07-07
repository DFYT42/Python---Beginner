##Practice splitting, counting, formatting printout
##Given a file path:
##read file, count total words and lines

##Pulls/Imports
    ##open, read, close file
a = open("hello.txt") ##puth path to your text file
content = a.read()
a.close()

##Definitions:
    ##count words in file and format output with placeholder and word list count
def wordcount(a):
    words = content.split()
    print("There are {0} words in the file.".format(len(words)))

    ##count lines in file and format output with placeholder and line list count
def linecount(a):
    num_lines = sum(1 for line in open("hello.txt"))
    print("There are {0} lines in the file.".format(num_lines))

    ##count characters in file
def count_characters(content):
    words = content.split()
    counter = 0
    for i in words:
        counter = counter + len(i)
    print("There are {0} characters in the file.".format(counter))
    

##Calls
wordcount(a)
linecount(a)
count_characters(content)
