divisible = lambda no : no % 3==0 and no % 5 ==0

def main():
     data = list(map(int,input("Enter numbers :").split()))
     print("Input data are :",data)

     mdata = list(filter(divisible,data))
     print("Divisible by 3 and 5 are :",mdata)

main()
