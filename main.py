# A code by Fávero Santos @ Curitiba, Paraná, Brazil in 09/12/2021

import numpy as np
from matplotlib import pyplot as plt
from scipy.linalg import expm, inv
import time

def exerciseOne(m, k, b, DT, f, T, iP, iV):
    'First order Euler integration is employed in this exercise'
    '1. Assume initial condition' \
    '2. Calculate the Equation Rate' \
    '3. Integrate the time step' \
    '4. Repeat 2 and 3 as needed'

    estimationList = list()
    timeNow = 0

    tic = time.perf_counter()

    A = np.matrix([[-b / m, -k / m], [1, 0]])
    xk = np.matrix([iV, iP]).transpose()
    B = np.matrix([1 / m, 0]).transpose()
    uk = f

    while timeNow < T:
        '1. Assume initial condition'
        estimationList.append(xk)

        '2. Calculate the equation rate, R'
        R = np.dot(A,xk) + np.dot(B, uk)

        '3. Integrate the time step'
        xk = xk + R*DT

        '4. Repeat steps 2. and 3. as needed'
        timeNow = round(timeNow + DT,3)

    toc = time.perf_counter()
    print(f"Tempo de processamento do kernel do Ex1: {(toc - tic):0.4f} seconds")

    timeVector = np.arange(0, T, DT)
    positionVector = np.arange(0, T, DT)
    velocityVector = np.arange(0, T, DT)

    for index in range(len(estimationList)):
        velocityVector[index] = float(estimationList[index][0])
        positionVector[index] = float(estimationList[index][1])

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig.suptitle('System response \n 2nd Order Spring-Damper System \n First order Euler integration method')

    ax1.plot(timeVector, positionVector)
    ax1.grid()
    ax1.set_ylabel("Position (m)")

    ax2.plot(timeVector, velocityVector)
    ax2.grid()
    ax2.set_ylabel("Velocity (m/s)")
    ax2.set_xlabel("Time (s)")

    plt.show()

def exerciseTwo(m, k, b, DT, f, T, iP, iV):
    'Matrix Exponential Discretisation is employed in this exercise.'
    '1. Assume an initial condition'
    '2. Step the solution'
    '3. Repeat step 2 as needed'

    'F = e^(A*dt)'
    'G = F*[I - e^(-A*dt)]*A^(-1)*B se A^(-1) existe'
    'G = F*alfa*beta*B'
    'G ainda pode ser mais simplificado, fazendo com que a exponencial seja aproximada por uma série de Taylor e esta seja truncada nos coeficientes lineares'

    estimationList = list()
    timeNow = 0

    tic = time.perf_counter()

    A = np.matrix([[-b / m, -k / m], [1, 0]])
    xk = np.matrix([iV, iP]).transpose()
    B = np.matrix([1 / m, 0]).transpose()
    uk = f

    F = expm(A*DT)
    alfa = F - np.dot(F, expm(-A*DT))
    G1 = np.dot(alfa, inv(A))
    G = np.dot(G1, B)

    while timeNow < T:
        '1. Assume initial condition'
        estimationList.append(xk)

        '2. Step the solution'
        xk = np.dot(F, xk) + np.dot(G, uk)

        '3. Repeat step 2. as needed'
        timeNow = round(timeNow + DT, 3)

    toc = time.perf_counter()
    print(f"Tempo de processamento do kernel do Ex2: {(toc - tic):0.4f} seconds")

    timeVector = np.arange(0, T, DT)
    positionVector = np.arange(0, T, DT)
    velocityVector = np.arange(0, T, DT)

    for index in range(len(estimationList)):
        velocityVector[index] = float(estimationList[index][0])
        positionVector[index] = float(estimationList[index][1])

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig.suptitle('System response \n 2nd Order Spring-Damper System \n Discretization exponential matrix method')

    ax1.plot(timeVector, positionVector)
    ax1.grid()
    ax1.set_ylabel("Position (m)")

    ax2.plot(timeVector, velocityVector)
    ax2.grid()
    ax2.set_ylabel("Velocity (m/s)")
    ax2.set_xlabel("Time (s)")

    plt.show()


def main():
    print("Main says: aloha, everybody!")

    m = 1
    b = 1
    k = 10
    f = 1
    DT = 0.15
    T = 10
    iP = 0
    iV = 0
    exerciseOne(m, k, b, DT, f, T, iP, iV)

    exerciseTwo(m, k, b, DT, f, T, iP, iV)

    print("Main says: see you soon!")
    exit()

if __name__ == '__main__':
    main()


