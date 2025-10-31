def main():
    n_times = get_number()
    meow(n_times)
    
    
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

    
def meow(n):
    for _ in range(n):
        print("meow")
    
    
main()