def permu(string, prefix=""):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            new_prefix = prefix + string[i]
            remaining = string[:i] + string[i+1:]
            permu(remaining, new_prefix)

user_input = input()
permu(user_input)
