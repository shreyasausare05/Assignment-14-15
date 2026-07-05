from functools import reduce

product = lambda no1,no2 : no1 * no2

def main():
    data = list(map(int,input("Enter numbers :").split()))
    print("Input data are :",data)

    mdata = reduce(product,data)
    print("Product of all elements are :",mdata)

main()