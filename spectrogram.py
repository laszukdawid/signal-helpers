"""
Example of using spectrogram.

More on the spectrogram:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html
"""
import numpy as np
import pylab as plt
from scipy.signal import chirp
from scipy.signal import spectrogram

# Define signal
dt = float(2**(-8))
time_array = np.arange(0, 4, dt)
signal = chirp(time_array, 10.0, time_array[-1], 80.0)
signal *= (np.cos(2*np.pi*time_array) + 1.2)
signal += 0.6*chirp(time_array, 90.0, time_array[-1], 40.0)

# Calculate spectrogram
fs = 1./dt
window = 'hanning'
nperseg = int(0.5*fs)  # samples per segment
noverlap = int(nperseg*0.9)  # samples overlapped

freq, t, spectr = spectrogram(signal, fs,
                                window,
                                nperseg=nperseg,
                                noverlap=noverlap,
                             )

# Display results
fig, axes = plt.subplots(2)
ax = axes[0]
ax.plot(time_array, signal)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude [arb. u.]")
ax.set_title("Original signal")

ax = axes[1]
ax.imshow(spectr, aspect='auto',
            extent=[t[0], t[-1], freq[0], freq[-1]],
            origin='lower',
            vmin=spectr.min(), vmax=spectr.max(),
            )
ax.set_xlabel("Time [s]")
ax.set_ylabel("Frequency [Hz]")
ax.set_title("Spectrogram")

plt.ylim((0, 100))
plt.tight_layout()
plt.show()
