import numpy as np
import matplotlib.pyplot as plt
def initialize(T):
    '''
    This function will initialize the grid of the experiment

    Arguments: 
        T, threshold for changing state

    Return: 
        grid, a tensor with dimension 2*10*10 where grid[0] is state and grid[1] is counter
    '''
    grid = np.zeros((2,10,10))
    for i in range(10):
        for j in range(10):
            grid[1][i][j] = np.random.randint(0,T)
    return grid
def neighbours(pos, grid):
    '''
    This function will return their 8 neighbors value
    
    Arguments:  
        pos, array of position that we are currently at i.e. [0,2] means x[0][2]
        grid, grid containing a tensor (which is 2 matrix). grid[0] is state and grid[1] is counter
    
    Return: 
        value, a list of 8 neighbors value
    '''
    value = []
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    for i in range(max(0, pos[0] - 1), min(rows, pos[0] + 2)):
        for j in range(max(0, pos[1] - 1), min(cols, pos[1] + 2)):
            if (i, j) != pos:
                value.append(grid[i][j])
    return value
def update(grid,k,T=100):
    '''
    This function will return the updated grid after 1 iteration
    
    Arguments:  
        grid, grid containing a tensor (which is 2 matrix). grid[0] is state and grid[1] is counter
        k, a float within probability range [0,1].
        T, a threshold. Default is 100
    
    Return: 
        grid, grid containing a tensor (which is 2 matrix). grid[0] is state and grid[1] is counter
    '''
    for i in range(10):
        for j in range(10):
            grid[1][i][j] = grid[1][i][j] + 1
            for x in neighbours([i,j],grid[0]):
                grid[1][i][j] = grid[1][i][j] + (k * grid[1][i][j] * x)
            if grid[1][i][j] >= T:
                grid[0][i][j] = 1
                grid[1][i][j] = 0
            else:
                grid[0][i][j] = 0
    return grid
if __name__ == '__main__':
    k = float(input('Please enter the number of k: '))
    mode = int(input('Please enter the starting iteration: '))
    grid = initialize(100)
    fig, axs = plt.subplots(20, 20,figsize=(20,20))
    j = 0
    if mode > 1:
        for i in range(mode):
            grid = update(grid,k)
    else:
        pass
    for i in range(401):
        grid = update(grid,k)
        axs[j, i%20].matshow(grid[0])
        axs[j,i%20].axis('off')
        if i >= 20 and i%20 == 0:
            j = j + 1
    fig.tight_layout()
    fig.suptitle('Coupled Oscillators with k = '+str(k)+' with starting iteration of ' +str(mode) ,fontsize=16)
    fig.subplots_adjust(top=0.95)
    fig.savefig('Coupled Oscillators with k = '+str(k)+'.png',facecolor='white')
    print('The file is saved as "Coupled Oscillators with k = '+str(k)+'.png"')
