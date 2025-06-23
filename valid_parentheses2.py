# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# %%


def isValid(s):

    for i in range(len(s) - 1):
        for i in range(len(s) - 1):
            if (
                (s[i] == "(" and s[i + 1] == ")")
                or (s[i] == "[" and s[i + 1] == "]")
                or (s[i] == "{" and s[i + 1] == "}")
            ):
                s = "".join(
                    [char for j, char in enumerate(s) if (j != i) and (j != (i + 1))]
                )
            break
    if len(s) == 0:
        flag_valid = True
    else:
        flag_valid = False
    return flag_valid


# %%
s = "[}{}{}{}()"
# s = "()[]{}"
# s = "(]"
# s = "(){}"
# s = "()"
# s = list(s)

a = isValid(s)
print(a)
