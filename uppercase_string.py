# change first letter after empty space to uppercase, except if
# it is already uppercase
# starts with a number - do nothing


def cap(s):

    s_lst = list(s)

    for i in range(len(s_lst)):
        # first letter
        if (i == 0) and (s_lst[i] == s_lst[i].lower()) and (s_lst[i].isalpha()):
            s_lst[i] = s_lst[i].upper()

        elif (
            (s_lst[i - 1].isspace())
            and (s_lst[i] == s_lst[i].lower())
            and (s_lst[i].isalpha())
        ):
            s_lst[i] = s_lst[i].upper()

    s_new = "".join(s_lst)

    return s_new


s = "hello  world"
s_cap = cap(s)
print(s_cap)
