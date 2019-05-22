# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

# Mass unit 3 positions
xpos3 = -2
ypos3 = -1
# Mass unit 4 positions
xpos4 = 2
ypos4 = -1
# Mass unit 5 positions
xpos5 = 2
ypos5 = 2

fig, ax = plt.subplots()
ax.scatter((xpos3, xpos4, xpos5), (ypos3, ypos4, ypos5), c=('green', 'red', 'blue'))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.show()