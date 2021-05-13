def find_pairs(arr,n):
    unique=[]
    for each in arr:                
        if(each not in unique):
            unique.append(each)
    
    count_pair=[]
    
    for each in unique:             
        count_pair.append(arr.count(each)) 
    print(count_pair) 
    
    final_count=0
    
    for each in count_pair:         
        final_count+=each//2
    return final_count        
            
    


n=20
sock_list=[10,20,30,10,50,10,70,80,10,20,30,40,60,70,90,20,10,60,20,10,]       
print(find_pairs(sock_list, n))     