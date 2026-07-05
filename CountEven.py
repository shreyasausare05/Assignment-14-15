even = lambda no : no % 2 == 0

def main():
     data = list(map(int,input("Enter numbers :").split()))
     print("Input data are :",data)

     mdata = len(list(filter(even,data)))
     print("Count of even number are :",mdata)

main()