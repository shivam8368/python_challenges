# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each
# letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front
# of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING str
#  2. INTEGER num


def caesar_cypher(str, num):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets_list = []

    # changing alphabet string into indexed list
    for i in alphabets:
        alphabets_list.append(i)

    encrypted_str = ""

    for i in range(len(str)):

        if str[i].lower() in alphabets_list:
            index_str = alphabets_list.index(str[i].lower())
            # checking the condition if the rotation exceeds 26 letters times it should stay in bound and starts over
            # from a, b, c....
            if (index_str + num) > (len(alphabets_list) - 1):
                if str[i].isupper():
                    encrypted_str += alphabets_list[(index_str + num) % 26].upper()

                else:
                    encrypted_str += alphabets_list[(index_str + num) % 26]
            else:
                if str[i].isupper():
                    encrypted_str += alphabets_list[index_str + num].upper()
                else:
                    encrypted_str += alphabets_list[index_str + num]
        else:
            encrypted_str += str[i]

    return encrypted_str
