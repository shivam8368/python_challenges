# There is a sequence of words in CamelCase as a string of letters, , having the following properties:
#
# It is a concatenation of one or more words consisting of English letters.
# All letters in the first word are lowercase.
# For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

# Given str, determine the number of words in str .




sample_string = "saveChangesInTheEditor"

def camel_case(str):
    my_arr = []
    read_stream = 0
    write_stream = 0
    temp_str = ''
    while read_stream <= len(str):

        if str[write_stream].isupper():
            read_stream = write_stream
            my_arr.append(temp_str)
            temp_str = ''
            temp_str += str[write_stream]
            write_stream += 1

        elif write_stream == (len(str)-1):
            temp_str += str[write_stream]
            my_arr.append(temp_str)
            temp_str = ''
            break
        else:
            temp_str += str[write_stream]
            write_stream += 1


    return len(my_arr)

print(camel_case(sample_string))




