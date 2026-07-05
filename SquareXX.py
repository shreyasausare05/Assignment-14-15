square = lambda no: no * no

def main():
    data = list(map(int,input("Enter numbers :").split()))
    print("Input Data is :",data)

    mdata = list(map(square,data))
    print("Square of elements are :",mdata)

main()