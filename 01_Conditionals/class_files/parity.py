
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_Even_better(n):
    return True if n % 2 == 0 else False


def is_even_even_better(n):
    return n % 2 == 0


main()