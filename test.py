def even_num(num):
    even_lst=[]
    odd_lst=[]
    
    for i in range(0,len(num)):
        if num[i]%2==0:
#             print (num[i], "Even")
            even_lst.append(num[i])
#             print(f'Even list is {even_lst}')
            #return even_lst
            
        else:
            odd_lst.append(num[i])
    print(f'Even list is {even_lst}')
    print(f'Odd list is {odd_lst}')

mylst=[2,3,5,6,7,8,9,10,11,15,22,14]

even_num(mylst)