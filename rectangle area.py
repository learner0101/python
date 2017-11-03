def areaRectangle(length,breadth):
    '''
    objective: to compute the area of rectangle
    input parameters: 
                length of rectangle
                breadth of rectangle
    approach: multiply length and breadth
    return value: area of rectangle
    '''
    area = length*breadth
    return area
    
def main(): 
    '''
    objective: to compute the area of rectangle
    input parameters: 
                   length of rectangle
                    breadth of rectangle
    approach: multiply length and breadth
    return value: area of rectangle
    '''
    length = int(input('enter the length of triangle '))
    breadth = int(input('enter the breadth of triangle '))
    print('length is ',length)
    print('breadth is ',breadth)
    print('area is ',areaRectangle(length,breadth))
    
if __name__=='__main__':
    main()
    print('program terminated ')
