##Write a function that takes password input from user and
##returns an encrypted password (cypher text) using a circular Caesar cipher for
##each character based on user shifting input.
##
##The Caesar cipher is one of the earliest known and simplest ciphers. It is a
##type of substitution cipher in which each character in the plaintext is
##'shifted' a certain number of places down the alphabet. For example, with
##a shift of 1, A would be replaced by B, B would become C, and so on.
##
##If a character is shifted off the end of the ascii Characterlist,
##it goes back to the beginning of the list. For example, the letter
##‘y’ shifted 3 to the right becomes the letter ‘b’.

#########IMPORTS################
import string

#########Variabes/Inputs#######
password = input("Type in the password you want encrytpted: ")
shift = int(input('How many shifts would you like? '))

########Functions##############
def ceaser_ch(Character,shift):
    Characterlist = string.printable
    ##Above is the character refernce variable, which uses all ascii characters
    ##allows the program to compare each character, in the password to be
    ##encrypted, to a list with a character POSITION in the list.
    ##That way, the program has a refernce point for the shift
    ix = Characterlist.find(Character)
    ##Find the character listed above in
    ##the ascii Characterlist
    newix = (ix + shift) % 95
    ##tell program: once you find the character & its numerical position, shifts
    ##the number of spaces indicated
    ##roll around if you get to end of ascii Characterlist
    ##--ascii has 95 characters
    cypher = Characterlist[newix]
    ##New variable, cypher, which is the encrypted message
    return cypher

def encrypted_password(password,shift):
    '''encrypts password, character by character for side by side comparison'''
    print("Password character shifts are below:")
    for Character in password:
        ##basic for loop
        ##tell program to go through the password, character by character,
        ##and do the below per character
        print(Character,ceaser_ch(Character,shift))
        ##print the original letter and the new encrypted Letter side by side

def ceaser_W(password,shift):
    '''uses ceaser_ch(Character,shift) to return an encrypted word'''
    print("Your password in plaintext is:",password)
    encrypted_password(password,shift)
    cypher = ''
    ##Sets up empty string 'container' to build individual Characterlist
    ##from above into a completed, encrypted password
    for Letter in password:
        cypher += ceaser_ch(Letter,shift)
    return cypher

##############Calls############
print("Your password encrypted is:",ceaser_W(password,shift))
