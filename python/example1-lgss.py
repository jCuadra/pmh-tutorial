# State estimation in a LGSS model using particle and Kalman filters

from __future__ import print_function, division
import matplotlib.pylab as plt
import numpy as np

from helpers.dataGeneration import generateData
from helpers.stateEstimation import particleFilter, kalmanFilter

# Set the random seed to replicate results in tutorial
np.random.seed(10)

# Define the model
# x[t + 1] = phi * x[t] + sigmav * v[t],    v[t] ~ N(0, 1)
# y[t] = x[t] + sigmae * e[t],              e[t] ~ N(0, 1)

# Set the parameters of the model theta=(phi, sigmav, sigmae), T, x_0
parameters = np.zeros(3)
parameters[0] = 0.75
parameters[1] = 1.00
parameters[2] = 0.10
noObservations = 250
initialState = 0

# Generate data
state, observations = generateData(parameters, noObservations, initialState)

# Plot data
plt.subplot(3, 1, 1)
plt.plot(observations, color='#1B9E77', linewidth=1.5)
plt.xlabel("time")
plt.ylabel("measurement")

plt.subplot(3, 1, 2)
plt.plot(state, color='#D95F02', linewidth=1.5)
plt.xlabel("time")
plt.ylabel("latent state")

# State estimation using particle filter with 100 particles
xHatPF, _ = particleFilter(observations, parameters, 100, initialState)

# State estimation using the Kalman filter
xHatKF = kalmanFilter(observations, parameters, initialState, 0.01)

# Plot state estimate
plt.subplot(3, 1, 3)
plt.plot(xHatKF[1:noObservations] - xHatPF[0:noObservations-1], color='#7570B3', linewidth=1.5)
plt.xlabel("time")
plt.ylabel("difference in estimate")

plt.show()