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

mylst=[100,122,123,140,145,210,115,25]

even_num(mylst)