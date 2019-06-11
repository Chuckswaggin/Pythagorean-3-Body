# Pythagorean-3-Body

This is the working file for a Pythagorean 3 Body problem written in Python using Maplotlib.

The Pythagorean 3 Body Problem is a gravitational simulation of 3 masses who have masses that form a Pythagorean triple (I will be using 3, 4, 5) and are placed at distances of the same values (again 3, 4, 5). Gravitational force is calculated for each mass and positions are updated.

The current version uses Verlet integration to update positions/velocities. A distance check is used to determine when shorter time step should be used to avoid masses flying away due to the inherent limitations of numerical integrators.

Matplotlib's FuncAnimation is used to create the animation for this simulation.

Based on more sophisticated simulations I've seen, my model quickly loses accuracy, seeming to diverge after the second close encounter. Using more sophisticated integrators such as adaptive Runge-Kutta or predictor-corrector methods could improve my program greatly, so maybe I will try to implement them later.
