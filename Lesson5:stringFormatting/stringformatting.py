# this prints out a name that is a variable
nobre = "koelslaw"
print("Hello, %s!" %nobre)



#this prints out name & age also
name = "koelslaw"
age = 222
print("%s is %d years old" % (name, age))

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)


# This prints a list out
mylist = [3,2,3]
print("some random list of numbers: %s" % mylist)


#end of chapter exercise
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string + " " +"%s %s. Yor current balance is $%s" % data)