addition = lambda no1,no2 : no1 + no2

def main():
    value1 = int(input("Enter first number :"))
    value2 = int(input("Enter second number :"))
    ret1 = addition(value1,value2)

    print(f"Addition of {value1} and {value2} is {ret1}")

if __name__== "__main__":
    main()
