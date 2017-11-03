def rightTriangle(ch):
    '''
    objective: to print a right angled triangle by using character input by the user
    input parameters: 
            character input by the user
    approach: multiple print statments for print rows of triangle
    '''
    print(ch)
    print(ch,ch)
    print(ch,ch,ch)
    print(ch,ch,ch,ch)
    print(ch,ch,ch,ch,ch)
    
def main(): 
    '''
    objective: to print a right angled triangle using character input by the user
    input parameters: 
            character input by the user
    approach: multiple print statments for print rows of triangle
    '''
    ch=input('Enter any character')
    rightTriangle(ch)
if __name__=='__main__':
    main()
    print('end of prog')
