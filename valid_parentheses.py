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

# %% naive as it only counts whether parentheses match in number
#  works if ([)] --> wrong

# def isValid(s):

#     # s = list(s)
#     n = len(s)

#     # initialize counters
#     brac_norm = 0
#     brac_curly = 0
#     brac_sq = 0

#     for i in range(n):
#         if s[i] == "(":
#             brac_norm += 1
#         elif s[i] == ")":
#             brac_norm -= 1
#         elif s[i] == "{":
#             brac_curly += 1
#         elif s[i] == "}":
#             brac_curly -= 1
#         elif s[i] == "[":
#             brac_sq += 1
#         elif s[i] == "]":
#             brac_sq -= 1
#         else:
#             continue

#     if brac_norm == 0 and brac_curly == 0 and brac_sq == 0:
#         result = True
#     else:
#         result = False

#     return result

# %%


def isValid(s):

    s = list(s)

    del_flag = 1

    while len(s) > 1 and del_flag == 1:

        for pos in range(len(s) - 1):
            if (
                (s[pos] == "(" and s[pos + 1] == ")")
                or (s[pos] == "{" and s[pos + 1] == "}")
                or (s[pos] == "[" and s[pos + 1] == "]")
            ):
                del s[pos]
                del s[pos]

                del_flag = 1
                break
            else:
                if pos == len(s) - 2:
                    del_flag = 0
                continue

    if len(s) > 0:
        return False
    else:
        return True


# %%
s = "[}{}{}{}()"
# s = "()"
s = list(s)
# %%
a = isValid(s)
print(a)

# %%
