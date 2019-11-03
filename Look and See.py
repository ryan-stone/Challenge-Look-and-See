# ------------------------------------------------------------------------------------------
#   Ryan Stone
#   Look And See - Programming Challenge
#   11/01/2019
# ------------------------------------------------------------------------------------------
#           1
#          11
#          21
#         1211
#        111221
#        312211
#       13112221
#      1113213211
#           .
#           .
#           .
#
# Starting with "1" the following lines are produced by "saying what you see", so that
# line two is "one one", line three is "two one(s)", line four is "one two one one".
#
# Write a function that given a starting value as a string, returns the appropriate
# sequence as a list. The starting value can have any number of digits. The termination
# condition is a defined by the  maximum number of iterations, also supplied as an argument.
# ------------------------------------------------------------------------------------------


# look_and_see
# This function accepts a starting string and the number of iterations.
# Each iteration the function appends a new string to the list.
# Each new string to be appended is generated from the last string in the list.
# The function terminates after the number of iterations have been reached.
# The final list of strings is returned to the calling statement.
def look_and_see(the_str, iterations):
    string_list = [the_str]
    for i in range(iterations):
        new_string = change_string(string_list[-1])
        string_list.append(new_string)
    return string_list


# change_string
# This function receives a string parameter.
# The string is transformed into a new string based on the "look and see"
# definition.
# Ex. 1 -> "One one" -> 11 -> "Two ones" -> 21 -> "One two, one one" -> 1211 -> ...
# The new string is returned once the function reaches the end of the initial string.
def change_string(the_str):
    new_string = ""
    count = 0
    previous_char = the_str[0]
    for char in the_str:
        if previous_char == char:
            count += 1
        else:
            new_string += str(count)
            new_string += previous_char
            count = 1
            previous_char = char
    new_string += str(count)
    new_string += previous_char
    return new_string


# Example output
a = look_and_see("1", 10)
print("Passing the string '1' with 10 iterations.")
print(a)
print()

b = look_and_see("42", 6)
print("Passing the string '42' with 6 iterations.")
print(b)
print()

c = look_and_see("Hello, world", 3)
print("Passing the string 'Hello, world' with 3 iterations.")
print(c)
print()

