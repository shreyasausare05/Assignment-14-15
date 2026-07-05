def chkGreater(no1,no2):
    if no1 > no2:
        print("Greater number is : ",no1)

    else:
        print("Greater number is :",no2)

def main():
    value1 = int(input("Enter a first number :"))
    value2 =int(input("Enter a second number :"))
    chkGreater(value1,value2)

if __name__ == "__main__":
    main()
