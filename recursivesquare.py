
import matplotlib.pyplot as plt
def square(x, y , size, count=0):
    '''Objective: To plot squares under square
    Input Parameters: x, y - lists of x coordinates and ycoordinates respectively
    size: size of the square
    count: variable for changing the coordinates
    Return Value: None
    '''
    #approach: recursive approach
    
    x=[count,size,size,count,count]
    y=[count,count,size, size,count]

    plt.plot(x, y, 'bo--')
    if(x[0]<=x[1]):
        size=size-1
        count=count+1
        square(x,y,size,count)
    

    

def main():
    '''
    Objective: To plot a square based on user input
    Input Parameter: None
    Return Value: None
    '''
    size = int(input('Enter size of the square: '))
    x = [0, size, size, 0, 0]
    y = [0, 0, size, size, 0]
    square(x,y,size)
    plt.title('Square')
    plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
