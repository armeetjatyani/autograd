import sys
sys.path.append("../../")
from autograd.engine import Value
import random
import math

verbose = True
lr = 0.001
epochs = 20000
x = Value(random.randint(0, 200))


def calculate_price(x):
    ''' 
    x is a multiple of 10
    '''
    x = math.ceil(x / 10)
    for xi in range(0, x + 10, 10):
        print(xi)

calculate_price(110)

# for i in range(epochs + 1):
#     # forward
#     revenue = q * (200 - q)
#     cost_1 = 100 * x
#     cost_2 = y ** 2
#     profit = revenue - cost_1 - cost_2
#     profit = -profit # we want to maximize profit so negate the entire expression

#     # backward
#     x.zero_grad()
#     y.zero_grad()
#     profit.backward()
    
#     # update params
#     x.data -= lr * x.grad
#     y.data -= lr * y.grad

#     # debugging info
#     if verbose and i % (epochs / 10) == 0:        
#         print(f"[{i}]\tx, y: {x.data} {y.data}: profit(x, y): {-profit.data}")