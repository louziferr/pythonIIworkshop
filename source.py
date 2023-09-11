import numpy as np

def get_hidden_array_1():
    x = np.zeros((20,170,2000), dtype=np.short)
    return x


def get_hidden_array_2():
    x = np.zeros((1,1,1,1,5000,10), dtype=float)    
    return x

def get_hidden_array_3():
    x = np.array([['ab','bb'], ['cb','db'], ['eb', 'fb'], ['gb', 'hb'],  ['ib', 'jb']])
    
    return x

def get_hidden_array_4():
    x = np.array([['ab','bb'], ['cb','db'], ['eb', 'fb'], ['gb', 'hb'],  ['ib', 'jb']])
    
    return x

def get_hidden_array_5():
    np.random.seed(42)
    x = np.random.rand(10,10)
    return x

def get_hidden_array_6():
    np.random.seed(42)
    x = np.random.randint(0,100,24).reshape((4,6))
    return x
