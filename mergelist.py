def merge_list(list1, list2):
    ''' 
        objective: To merge two sorted list into a single list
        input parameters:
                list1- first list,
                list2- second list
        return value: merged list named m_list
    '''
    #approach: Recursive approach is used for megring the list
    
    m_list=[]
    
    if list1==[] and list2==[]:
        return m_list
    
    if list1!=[] and list2==[]:
        return m_list + list1
    
    if list1==[] and list2!=[]:
        return m_list + list2
    
    if list1!=[] and list2!=[]:
        
        if list1[0]<=list2[0]:
            m_list.append(list1[0])
            m_list = m_list + merge_list(list1[1:],list2)
            
        if list2[0]<=list1[0]:
            m_list.append(list2[0]) 
            m_list = m_list + merge_list(list1,list2[1:])
        return m_list
        


list1=[5,7,9]
list2=[4,6,8]
m = merge_list(list1, list2)
print("merged list = ", m)
