# edited matter

def increament(number):
    '''
    objective: To copmpute the increament value of a number entered by a user by a increament of i
    input parameter:
                    number: The number to be increamented
    appraoch:
            increament the value by i
    '''
    
    #number=int(input('Enter the number to be increamented : '))
    increament_number=number+1
    #print('The increament number is :',increament_number)
    return increament_number

def call(number1,number2):
    '''.
    '''
    assert number1>=0
    assert number2>=0
    if number2==0:
        return number1
    else:

       
        return call(increament(number1),number2-1)
    
    

def main():
    '''
    objective: To copmpute the increament value of a number entered by a user by a increament of i
    input parameter:
        number1: The number to be increamented
        number2: The increamental value
    appraoch: increament the value by i
    '''
    num1=int(input('Enter the number to be increamented : '))
    num2=int(input('Enter the increament value :'))
    number3=call(num1,num2)
    print("The value is :",number3)

if __name__=='__main__' :
    main()
