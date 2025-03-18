import random

def get_random_number(n):
    return random.randint(1, n)

def get_random_word():
    words = ["apple", "banana", "orange"]
    return random.choice(words)

if __name__ == '__main__':
    print(get_random_number(10))
    print(get_random_word())
