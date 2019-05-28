# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

G = 1e4
time_step = 0.01
AU = 1
MASS_SCALE = 1

# Calculate the gravitational forces between the masses
def calculate_force(mass3, pos3, acc3, mass4, pos4, acc4, mass5, pos5, acc5):
    # ADD DIVIDE BY ZERO CHECKS LATER
    # Calculate force between masses 3 and 4
    if (pos3[0] - pos4[0]) != 0:
        acc3[0] = -(G * mass3 * mass4) / ((pos3[0] - pos4[0]) ** 2)
    else:
        acc3[0] = 0
    if (pos3[1] - pos4[1]) != 0:
        acc3[1] = -(G * mass3 * mass4) / ((pos3[1] - pos4[1]) ** 2)
    else:
        acc3[1] = 0
    acc4[0] = -1 * acc3[0]
    acc4[1] = -1 * acc3[1]
    
    # Calculate force between masses 3 and 5
    if (pos5[0] - pos3[0]) != 0:
        acc5[0] = -(G * mass3 * mass5) / ((pos5[0] - pos3[0]) ** 2)
    else:
        acc5[0] = 0
    if (pos5[1] - pos3[1]) != 0:
        acc5[1] = -(G * mass3 * mass5) / ((pos5[1] - pos3[1]) ** 2)
    else:
        acc5[1] = 0
    acc3[0] += -1 * acc5[0]
    acc3[1] += -1 * acc5[1]
    
    # Calculate force between masses 4 and 5
    if (pos4[0] - pos5[0]) != 0:
        acc4[0] += -(G * mass4 * mass5) / ((pos4[0] - pos5[0]) ** 2)
        acc5[0] += -(G * mass5 * mass4) / ((pos5[0] - pos4[0]) ** 2)
    if (pos4[1] - pos5[1]) != 0:
        acc4[1] += -(G * mass4 * mass5) / ((pos4[1] - pos5[1]) ** 2)
        acc5[1] += -(G * mass5 * mass4) / ((pos5[1] - pos4[1]) ** 2)

# Update the positions of the masses
def update_pos(pos3, vel3, acc3, pos4, vel4, acc4, pos5, vel5, acc5):
    vel3[0] += acc3[0] * time_step
    vel3[1] += acc3[1] * time_step
    pos3[0] += vel3[0] * time_step
    pos3[1] += vel3[1] * time_step
    
    vel4[0] += acc4[0] * time_step
    vel4[1] += acc4[1] * time_step
    pos4[0] += vel4[0] * time_step
    pos4[1] += vel4[1] * time_step
    
    vel5[0] += acc5[0] * time_step
    vel5[1] += acc5[1] * time_step
    pos5[0] += vel5[0] * time_step
    pos5[1] += vel5[1] * time_step

def main():
# Mass unit 3 variable initializations
    mass3 = 3 * MASS_SCALE
    pos3 = [-2 * AU,-1 * AU]
    vel3 = [0, 0]
    acc3 = [0, 0]
    # Mass unit 4 positions
    mass4 = 4 * MASS_SCALE
    pos4 = [2 * AU, 2 * AU]
    vel4 = [0, 0]
    acc4 = [0, 0]
    # Mass unit 5 positions
    mass5 = 5 * MASS_SCALE
    pos5 = [2 * AU, -1 * AU]
    vel5 = [0, 0]
    acc5 = [0, 0]
    
    # Create the figure and graph the initial points
    fig, ax = plt.subplots()
    ax.scatter((pos3[0], pos4[0], pos5[0]), (pos3[1], pos4[1], pos5[1]), \
               c=('green', 'red', 'blue'))
    ax.set_xlim(-10 * AU, 10 * AU)
    ax.set_ylim(-10 * AU, 10 * AU)
    
    for i in range(100):
        calculate_force(mass3, pos3, acc3, mass4, pos4, acc4, mass5, pos5, acc5)
        #print('\nAcceleration ' + str(i))
        #print(list(map(lambda x: format(x, '.1e'), acc3)))
        #print(list(map(lambda x: format(x, '.1e'), acc4)))
        #print(list(map(lambda x: format(x, '.1e'), acc5)))
        
        update_pos(pos3, vel3, acc3, pos4, vel4, acc4, pos5, vel5, acc5)
        #print('\nPosition ' + str(i))
        #print(list(map(lambda x: format(x, '.1e'), pos3)))
        #print(list(map(lambda x: format(x, '.1e'), pos4)))
        #print(list(map(lambda x: format(x, '.1e'), pos5)))
    
        ax.scatter((pos3[0], pos4[0], pos5[0]), (pos3[1], pos4[1], pos5[1]), \
               c=('green', 'red', 'blue'))
    print(pos3)
    plt.show()

main()
