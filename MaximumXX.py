from functools import reduce

maximum = lambda no1 ,no2 : no1 if no1>no2 else no2

def main():
    data = list(map(int,input("Enter numbers :").split()))
    print("Input data are :",data)

    mdata = reduce(maximum,data)
    print("Maximum number is :",mdata)

main()