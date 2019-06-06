# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')
from matplotlib.animation import FuncAnimation
import math

# Constants
G = 1.0             #gravitational constant
time_step = 0.001   #time between each position update
AU = 1.0            #distance unit (AU because "astronomical unit")
MASS_SCALE = 1.0    #mass scale if needed
num_steps = 3000    #number of time steps used

# Set up figure, x and y axis limits
fig, ax = plt.subplots()
ax.set_xlim(-4 * AU, 4 * AU)
ax.set_ylim(-4 * AU, 4 * AU)
line, = ax.plot([], [], lw=2)

# Create the line objects
lines, line_color = [], ['green', 'blue', 'purple']
for i in range(3):
    l = ax.plot([], [], color=line_color[i])[0]
    lines.append(l)

# Position lists for each mass
pos_m3 = [[-2 * AU], [-1 * AU]]
pos_m4 = [[2 * AU], [2 * AU]]
pos_m5 = [[2 * AU], [-1 * AU]]

# Calculate the gravitational forces between the masses
def calculate_acc(mass3, pos3, acc3, mass4, pos4, acc4, mass5, pos5, acc5):
    # Calculate acceleration between masses 3 and 4
    # X component of mass 3
    acc3[0] = -(pos3[0] * G * mass4) / \
    math.sqrt(((pos3[0] - pos4[0]) **2) + ((pos3[1] - pos4[1]) **2)) **3
    # Y component of mass 3
    acc3[1] = -(pos3[1] * G * mass4) / \
    math.sqrt(((pos3[0] - pos4[0]) **2) + ((pos3[1] - pos4[1]) **2)) **3
    
    # X component of mass 4
    acc4[0] = -(pos4[0] * G * mass3) / \
    math.sqrt(((pos4[0] - pos3[0]) **2) + ((pos4[1] - pos3[1]) **2)) **3
    # Y component of mass 4
    acc4[1] = -(pos4[1] * G * mass3) / \
    math.sqrt(((pos4[0] - pos3[0]) **2) + ((pos4[1] - pos3[1]) **2)) **3
        
    
    # Calculate force between masses 3 and 5
    # X component of mass 5
    acc5[0] = -(pos5[0] * G * mass3) / \
    math.sqrt(((pos5[0] - pos3[0]) **2) + ((pos5[1] - pos3[1]) **2)) **3
    # Y component of mass 5
    acc5[1] = -(pos5[1] * G * mass3) / \
    math.sqrt(((pos5[0] - pos3[0]) **2) + ((pos5[1] - pos3[1]) **2)) **3
    
    # X component of mass 3 (added to the acceleration found in above section)
    acc3[0] += -(pos3[0] * G * mass5) / \
    math.sqrt(((pos3[0] - pos5[0]) **2) + ((pos3[1] - pos5[1]) **2)) **3
    # Y component of mass 3 (added to the acceleration found in above section)
    acc3[1] += -(pos3[1] * G * mass5) / \
    math.sqrt(((pos3[0] - pos5[0]) **2) + ((pos3[1] - pos5[1]) **2)) **3
    
    
    # Calculate force between masses 4 and 5
    # X component of mass 4 (added to the acceleration from earlier)
    acc4[0] += -(pos4[0] * G * mass5) / \
    math.sqrt(((pos4[0] - pos5[0]) **2) + ((pos4[1] - pos5[1]) **2)) **3
    # Y component of mass 4 (added to the acceleration from earlier)
    acc4[1] += -(pos4[1] * G * mass5) / \
    math.sqrt(((pos4[0] - pos5[0]) **2) + ((pos4[1] - pos5[1]) **2)) **3
    
    # X component of mass 5 (added to the acceleration from earlier)
    acc5[0] += -(pos5[0] * G * mass4) / \
    math.sqrt(((pos5[0] - pos4[0]) **2) + ((pos5[1] - pos4[1]) **2)) **3
    # Y component of mass 5 (added to the acceleration from earlier)
    acc5[1] += -(pos5[1] * G * mass4) / \
    math.sqrt(((pos5[0] - pos4[0]) **2) + ((pos5[1] - pos4[1]) **2)) **3
    

# Update the positions of the masses using Verlet integration
def verlet_pos(pos3, vel3, acc3, pos4, vel4, acc4, pos5, vel5, acc5):
    pos3[0] += (vel3[0] * time_step) + (0.5 * acc3[0] * (time_step **2))
    pos3[1] += (vel3[1] * time_step) + (0.5 * acc3[1] * (time_step **2))
    
    pos4[0] += (vel4[0] * time_step) + (0.5 * acc4[0] * (time_step **2))
    pos4[1] += (vel4[1] * time_step) + (0.5 * acc4[1] * (time_step **2))
    
    pos5[0] += (vel5[0] * time_step) + (0.5 * acc5[0] * (time_step **2))
    pos5[1] += (vel5[1] * time_step) + (0.5 * acc5[1] * (time_step **2))

# Update the velocities using Verlet integration
def verlet_vel(vel3, acc3, old_acc3, vel4, acc4, old_acc4, vel5, acc5, old_acc5):
    vel3[0] += 0.5 * (acc3[0] + old_acc3[0]) * time_step
    vel3[1] += 0.5 * (acc3[1] + old_acc3[1]) * time_step
    
    vel4[0] += 0.5 * (acc4[0] + old_acc4[0]) * time_step
    vel4[1] += 0.5 * (acc4[1] + old_acc4[1]) * time_step
    
    vel5[0] += 0.5 * (acc5[0] + old_acc5[0]) * time_step
    vel5[1] += 0.5 * (acc5[1] + old_acc5[1]) * time_step

# Used as init_func for FuncAnimation
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Animation function that FuncAnimation will call
def animate(i):
    lines[0].set_data(pos_m3[0][:i], pos_m3[1][:i])
    lines[1].set_data(pos_m4[0][:i], pos_m4[1][:i])
    lines[2].set_data(pos_m5[0][:i], pos_m5[1][:i])
    return lines
    

# Mass unit 3 variable initializations
mass3 = 3 * MASS_SCALE
pos3 = [-2 * AU,-1 * AU]
vel3 = [0, 0]
acc3 = [0, 0]
old_acc3 = [0, 0]
# Mass unit 4 positions
mass4 = 4 * MASS_SCALE
pos4 = [2 * AU, 2 * AU]
vel4 = [0, 0]
acc4 = [0, 0]
old_acc4 = [0, 0]
# Mass unit 5 positions
mass5 = 5 * MASS_SCALE
pos5 = [2 * AU, -1 * AU]
vel5 = [0, 0]
acc5 = [0, 0]
old_acc5 = [0, 0]

calculate_acc(mass3, pos3, acc3, mass4, pos4, acc4, mass5, pos5, acc5)
for i in range(num_steps):
    # Update positions of the masses
    verlet_pos(pos3, vel3, acc3, pos4, vel4, acc4, pos5, vel5, acc5)
    # Add new positions to the positions lists
    pos_m3[0].append(pos3[0])
    pos_m3[1].append(pos3[1])
    pos_m4[0].append(pos4[0])
    pos_m4[1].append(pos4[1])
    pos_m5[0].append(pos5[0])
    pos_m5[1].append(pos5[1])
    #print('\nPosition ' + str(i))
    #print(list(map(lambda x: format(x, '.1e'), pos3)))
    #print(list(map(lambda x: format(x, '.1e'), pos4)))
    #print(list(map(lambda x: format(x, '.1e'), pos5)))
    
    # Set old acclerations to the current values in acceleration lists before
    # they are updated
    old_acc3[0] = acc3[0]
    old_acc3[1] = acc3[1]
    old_acc4[0] = acc4[0]
    old_acc4[1] = acc4[1]
    old_acc5[0] = acc5[0]
    old_acc5[1] = acc5[1]
    # Update the accelerations
    calculate_acc(mass3, pos3, acc3, mass4, pos4, acc4, mass5, pos5, acc5)
    #if i % 300 == 0:
    #    print('\nAcceleration ' + str(i))
    #    print(list(map(lambda x: format(x, '.1e'), acc3)))
    #    print(list(map(lambda x: format(x, '.1e'), acc4)))
    #    print(list(map(lambda x: format(x, '.1e'), acc5)))
    
    # Update velocities
    verlet_vel(vel3, acc3, old_acc3, vel4, acc4, old_acc4, vel5, acc5, old_acc5)

# Create the animation    
anim = FuncAnimation(fig, animate, init_func=init, frames=num_steps,
                     blit=True, interval=2)

# Use these for regular plots instead of animation
#ax.plot(pos_m3[0], pos_m3[1], c='green')
#ax.plot(pos_m4[0], pos_m4[1], c='red')
#ax.plot(pos_m5[0], pos_m5[1], c='blue')
#plt.show()
