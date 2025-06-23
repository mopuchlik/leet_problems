# The first line of input contains the original string.
# The next line contains the substring.

# Each character in the string is an ascii character.

# Output the integer number indicating the total
# number of occurrences of the substring in the original string.

# %%


def count_substring(string, sub_string):

    count = 0

    n_substr = len(sub_string)
    # n_str = len(sub)

    for i, _ in enumerate(string):
        if string[i : i + n_substr] == sub_string:
            count += 1

    return count


# %%
string = "ininini"
sub_string = "ini"

x = count_substring(string, sub_string)
print(x)

string = "ABCDCDC"
sub_string = "CDC"
x = count_substring(string, sub_string)
print(x)
