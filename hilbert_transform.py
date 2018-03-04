"""
Example of using Hilbert transform.

More information available:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html
"""
import numpy as np
import pylab as plt
from scipy.signal import hilbert, chirp

# Create a signal
dt = 0.005
time_array = np.arange(0, 2, dt)
signal = chirp(time_array, 10.0, time_array[-1], 40.0)
signal *= (np.cos(2*np.pi*time_array) + 1.2)

# Extract analytical signal through Hilbert Transform
analytic_signal = hilbert(signal)
amplitude = np.abs(analytic_signal)
phase = np.unwrap(np.angle(analytic_signal))
instant_freq = np.diff(phase)/(2*np.pi*dt)

# Present results as a figure
fig, axes = plt.subplots(3)

ax = axes[0]
ax.plot(time_array, signal)
ax.plot(time_array, amplitude, 'r')
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude [u]")
ax.set_title("chirp(10Hz -> 40Hz) ${}\cdot (1.2 + \cos(2\pi t))$")

ax = axes[1]
ax.plot(time_array, phase)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Phase [rad]")

ax = axes[2]
ax.plot(time_array[:-1], instant_freq)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Inst. Freq. [rad/s]")

plt.tight_layout()
plt.show()
