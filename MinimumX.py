minimum= lambda no1,no2:no1 if no1 < no2 else no2
    
def main():
    value1 = int(input("Enter a first number :"))
    value2 =int(input("Enter a second number :"))
    ret =minimum(value1,value2)

    print("Minimum Value is :",ret)

if __name__ == "__main__":
    main()
