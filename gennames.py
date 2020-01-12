from random import randint

def generate_random_name(length):
    alpha="abcde"
    temp=""
    for x in range(length):
        temp+=alpha[randint(0, len(alpha)-1)]
    return temp

def limit_names(data):
    return data[:3]
