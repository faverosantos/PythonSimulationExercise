# A code by Fávero Santos @ Curitiba, Paraná, Brazil in 09/12/2021

import numpy as np
from matplotlib import pyplot as plt

def exerciseOne(m, k, b, DT, f, T, iP, iV):
    'In this exercise, first order Euler integration is employed.'
    '1. Assume initial condition' \
    '2. Calculate the Equation Rate' \
    '3. Integrate the time step' \
    '4. Repeat 2 and 3 as needed'

    estimationList = list()
    timeNow = 0

    A = np.matrix([[-b / m, -k / m], [1, 0]])
    B = np.matrix([iV, iP]).transpose()
    C = np.matrix([1 / m, 0]).transpose()
    D = f

    while timeNow < T - DT:
        '1. Assume initial condition'
        estimationList.append(B)

        '2. Calculate the equation rate, R'
        R = np.dot(A,B) + np.dot(C, D)

        '3. Integrate the time step'
        B = B + R*DT

        '4. Repeat steps 2. and 3. as needed'
        timeNow = timeNow + DT

    timeVector = np.arange(0, T, DT)
    positionVector = np.arange(0, T, DT)
    velocityVector = np.arange(0, T, DT)

    for index in range(len(estimationList)):
        velocityVector[index] = float(estimationList[index][0])
        positionVector[index] = float(estimationList[index][1])



    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig.suptitle('System response \n 2nd Order Spring-Damper System')

    ax1.plot(timeVector, positionVector)
    ax1.grid()
    ax1.set_ylabel("Position (m)")

    ax2.plot(timeVector, velocityVector)
    ax2.grid()
    ax2.set_ylabel("Velocity (m/s)")
    ax2.set_xlabel("Time (s)")


    plt.show()









def exerciseTwo():
    pass


def main():
    print("Main says: aloha, everybody!")

    m = 1
    b = 1
    k = 10
    f = 1
    DT = 0.01
    T = 10
    iP = 0
    iV = 0
    exerciseOne(m, k, b, DT, f, T, iP, iV)

    exerciseTwo()

    print("Main says: see you soon!")
    exit()

if __name__ == '__main__':
    main()


