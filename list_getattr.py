

# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer e at position i
# print: Print the list.
# remove e: Delete the first occurrence of integer e
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
#
# Initialize your list and read in the value of
# followed by lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':

    my_list = []

    N = int(input())

    # each input in a new line
    for _ in range(N):
        parts = input().split()
        cmd = parts[0]
        args = list(map(int, parts[1:]))

        if cmd == "print":
            # this is not a method, the only case
            print(my_list)
        else:
            # run command on my_list with args
            getattr(my_list, cmd)(*args)


# example input

# 12
# insert 0 5
# print
