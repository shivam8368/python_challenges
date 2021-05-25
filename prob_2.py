# Louise joined a social networking site to stay in touch with her friends.
# The signup page required her to input a name and a password. However, the password
# must be strong. The website considers a password to be strong if it satisfies the following criteria:
#
# Its length is at least 6.
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character.
# The special characters are: !@#$%^&*()-+
# She typed a random string of length  in the password field but wasn't sure if it was strong.
# Given the string she typed, can you find the minimum number of characters she must add to make her password
# strong?




sample_password = "Ab1"


def strong_password(password):
    special_characters = set("!@#$%^&*()-+")

    criteria_unchecked = 0

    digit = 0
    upper = 0
    lower = 0
    sym = 0

    for i in password:
        if i.isdigit():
            digit += 1
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i in special_characters:
            sym += 1

    if digit == 0:
        criteria_unchecked += 1
    if upper == 0:
        criteria_unchecked += 1
    if lower == 0:
        criteria_unchecked += 1
    if sym == 0:
        criteria_unchecked += 1

    return max(criteria_unchecked, 6-len(password))


print(strong_password(sample_password))