checkodd =lambda no: (no % 2 ==1)

def main():
    data = list(map(int,input("Enter numbers :").split()))

    print("Input data is :",data)

    Fdata =list( filter(checkodd,data))    #Fdata is name of list

    print("data after filter:",Fdata)
    
if __name__ == "__main__":
    main()