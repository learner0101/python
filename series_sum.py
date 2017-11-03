def incr(n):
    '''
    objective: Calculate sum of first n natural numbers
    input value: number of terms
    apporach: increment the value
    '''

    if(n==0):
        return 0
    else:
        return n+incr(n-1)
def addSeries(num):
    '''
    objective:Calculate sum of first n natural numbers
    input value: number of terms
    apporach: increment the value
    '''
    return incr(num)
    
def main():
    '''
    objective:Calculate sum of first n natural numbers
    input value: number of terms
    apporach: increment the value
    '''
    num=int(input('enter the number of terms'))
    res=addSeries(num)
    print("sum till",num,"is :  ",res)

if __name__=='__main__' :
    main()
