def greet(name):
    greeting = f"hello, {name}"
    return greeting

def main():
    user_name = input("enter your name: ")
    message = greet(user_name)
    print(f"the return message: {message}")

if __name__ == "__main__":
    main()

    