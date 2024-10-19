import numpy as np
import matplotlib.pyplot as plt


def least_square_solve(X, t):
    w = np.linalg.solve(X.T @ X, X.T @ t)
    return w

def transofrm(x):
    return (x-np.mean(x))/np.std(x)


def polynomial (x, maxorder):
    X = np.vander(x,N=maxorder,increasing=True)
    return(X) 


def lin_reg_poly(x, y, maxorder):
    X = polynomial(x, maxorder)
    w = least_square_solve(X, y)
    return w


def rbf (x, center, width):
    X = np.zeros((x.shape[0],center.shape[0]))
    for index,k in enumerate(center):
        res = np.exp((-(x-k)**2)/(2*(width)))
        X[:,index] = res
    return X

def lin_reg_rbf(x, center, width ,y):
    X = rbf(x,center,width)
    w = least_square_solve(X, y)
    return w


def poly_pipeline(x, y, maxorder):
    w_poly = lin_reg_poly(x, y, maxorder)
    x_test = np.linspace(min(x), max(x), 100)
    X_test_poly = polynomial(x_test, maxorder)
    f_test = X_test_poly @ w_poly
    plt.plot(x_test, f_test, linewidth=3)
    plt.plot(x, y, "ro")
    plt.show()

def rbf_pipeline(x, y, center, width):
    w_rbf = lin_reg_rbf(x, center, width, y)
    x_test = np.linspace(min(x), max(x), 100)
    X_test_rbf = rbf(x_test, center, width)
    f_test = X_test_rbf @ w_rbf
    plt.plot(x_test, f_test, linewidth=3)
    plt.plot(x, y, "ro")
    plt.show()


if __name__ == "__main__":
    values = np.loadtxt('src/results.csv', delimiter=',', skiprows=1)
    x = values[:, 0]
    y = values[:, 1]

    size = np.arange(len(x))
    number_of_random_points = int(input("Enter the number of random points (positive integer): "))
    random_indecies = np.random.choice(size, size=number_of_random_points, replace = False)
    x = transofrm(x[random_indecies])
    y = y[random_indecies]

    pipeline_type = input("Enter the type of pipeline (poly or rbf): ")

    if pipeline_type == "poly":
        maxorder = int(input("Enter maxorder (positive integer): "))
        poly_pipeline(x, y, maxorder)
    elif pipeline_type == "rbf":
        center_size = int(input("Enter the number of rbf functions (positive integer): "))
        center = np.random.choice(x, size=center_size, replace=False)
        width = float(input("Enter the width (positive float/int): "))
        rbf_pipeline(x, y, center, width)
    else:
        print("Invalid pipeline type")

