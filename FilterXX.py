str_length = lambda a : len(a)> 5

def main():
     data = input("Enter strings :").split()
     print("Input data are :",data)

     mdata = list(filter(str_length,data))
     print("Charcters are :",mdata)

main()