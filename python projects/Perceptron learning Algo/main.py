import matplotlib.pyplot as plt
import random

color_list = ['r-', 'm-', 'y-', 'c-', 'b-', 'g-']
color_index = 0

def show_learning(w):
    global color_index
    print('w0 =', '%5.2f' % w[0], ',w1 =', '%5.2f' % w[1], ',w2 =', '%5.2f' % w[2])

    if color_index ==0:
        plt.plot([1.0], [1.0], 'b_', markersize=12)
        plt.plot([-1.0, 1.0, -1.0], [1.0, -1.0, -1.0], 'r+', markersize=12)
        plt.axis([-2, 2, -2, 2])
        plt.xlabel('x1')
        plt.ylabel('x2')
        x = [-2.0 , 2.0]

        if abs(w[2]) < 1e-5:
            y = [-w[1]/(1e-5)*(-2.0)+(-w[0]/(1e-5)),
                 -w[1]/(1e-5)*(2.0)+(-w[0]/(1e-5))]
        else:
            y = [-w[1]/w[2]*(-2.0)+(-w[0]/w[2]),
                 -w[1]/w[2]*(2.0)+(-w[0]/w[2])]

        plt.plot(x,y,color_list[color_index])
        if color_index <(len(color_list)-1):
            color_index += 1

random.seed(7)

LEARNING_RATE = 0.1
index_list = [0, 1, 2, 3]

x_train = [(1.0, -1.0, -1.0),(1.0, -1.0, 1.0,),
           (1.0, 1.0, -1.0), (1.0, 1.0, 1.0)]
y_train = [1.0, 1.0, 1.0, -1.0]

w = [0.2, -0.6, 0.25]

show_learning(w)
