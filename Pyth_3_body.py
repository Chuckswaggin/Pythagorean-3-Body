# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')
import math

G = 6.67e-11
time_step = 86400
AU = 1.496e11
MASS_SUN = 1.989E30
#MASS_EARTH = 5.972e24

# Calculate the gravitational forces between the masses
def calculate_acc(e_pos, e_acc, sun, s_pos):
    # ADD DIVIDE BY ZERO CHECKS LATER
    # Calculate force between masses 3 and 4
    if (e_pos[0] - s_pos[0]) != 0:
        e_acc[0] = -(e_pos[0] * G * sun) / \
        math.sqrt(((e_pos[0] - s_pos[0]) **2) + ((e_pos[1] - s_pos[1]) **2)) **3
    else:
        e_acc[0] = 0
    if (e_pos[1] - s_pos[1]) != 0:
        e_acc[1] = -(e_pos[1] * G * sun) / \
        math.sqrt(((e_pos[0] - s_pos[0]) **2) + ((e_pos[1] - s_pos[1]) **2)) **3
    else:
        e_acc[1] = 0
    #s_acc[0] = -1 * e_acc[0]
    #s_acc[1] = -1 * e_acc[1]

# Update the positions of the masses
def verlet_pos(e_pos, e_vel, e_acc):
    e_pos[0] += (e_vel[0] * time_step) + (0.5 * e_acc[0] * (time_step **2))
    e_pos[1] += (e_vel[1] * time_step) + (0.5 * e_acc[1] * (time_step **2))

# Update the velocity using velocity Verlet equation
def verlet_vel(e_vel, e_acc, old_acc):
    e_vel[0] += 0.5 * (e_acc[0] + old_acc[0]) * time_step
    e_vel[1] += 0.5 * (e_acc[1] + old_acc[1]) * time_step

def main():
    # Mass unit 3 variable initializations
    e_pos = [1 * AU, 0]
    e_vel = [0, 3e4]
    e_acc = [0, 0]
    old_acc = [0, 0]
    positions = [[1 * AU], [0]]
    # Mass unit 4 positions
    sun = MASS_SUN
    s_pos = [0, 0]
    
    # Create the figure and graph the initial points
    fig, ax = plt.subplots()
    #plt.ion()
    #ax.scatter((e_pos[0], s_pos[0]), (e_pos[1], s_pos[1]), \
    #           c=('green', 'blue'))
    #ax.plot(x_positions, y_positions, c='green')
    #ax.scatter(s_pos[0], s_pos[1], c='red')
    #fig.canvas.draw()
    #ax.set_xlim(-2 * AU, 2 * AU)
    #ax.set_ylim(-2 * AU, 2 * AU)
    
    calculate_acc(e_pos, e_acc, sun, s_pos)
    
    for i in range(365):
        #print('\nAcceleration ' + str(i))
        #print(list(map(lambda x: format(x, '.1e'), e_acc)))
        #print(list(map(lambda x: format(x, '.1e'), s_acc)))
        
        verlet_pos(e_pos, e_vel, e_acc)
        positions[0].append(e_pos[0])
        positions[1].append(e_pos[1])
        #print('\nPosition ' + str(i))
        #print(list(map(lambda x: format(x, '.1e'), e_pos)))
        #print(list(map(lambda x: format(x, '.1e'), s_pos)))
        
        old_acc[0] = e_acc[0]
        old_acc[1] = e_acc[1]
        calculate_acc(e_pos, e_acc, sun, s_pos)
        verlet_vel(e_vel, e_acc, old_acc)
    
        #ax.scatter((e_pos[0], s_pos[0]), (e_pos[1], s_pos[1]), \
        #       c=('green', 'blue'))
        #ax.clear()
        #ax.plot(x_positions, y_positions, c='green')
        #ax.scatter(s_pos[0], s_pos[1], c='red')
        #fig.canvas.draw()
    print(e_pos)
    ax.plot(positions[0], positions[1], c='green')
    ax.scatter(s_pos[0], s_pos[1], c='red')
    plt.show()
    
main()
