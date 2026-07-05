largest= lambda no1,no2,no3:no1 if no1 > no2 and no1> no2 else (no2 if no2 > no3 else no3)
    
def main():
    value1 = int(input("Enter a first number :"))
    value2 =int(input("Enter a second number :"))
    value3 = int(input("Enter a third number"))
    ret =largest(value1,value2,value3)

    print("Largest Value is :",ret)

if __name__ == "__main__":
    main()
