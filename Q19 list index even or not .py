def check_numbers( list1,list2):
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i=i+1
check_numbers([2,6,18,10,3,75],[6,19,24,12,3,87])


 