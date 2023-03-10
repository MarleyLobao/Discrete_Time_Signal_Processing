import numpy as np
import matplotlib.pyplot as plt

# initial point of the signal
t0 = 0
# final point of the signal
tf = 1

# frequencies of input signal
f1 = 2000
f2 = 730

# sampling frequency
Fs = 6000

# sampling rate
T = 1/Fs

# signal definition
t = np.arange(t0, tf, T)
signal = np.sin(2*np.pi*f1*t) + 0.5*np.cos(2*np.pi*f2*t)

# frequencies for spectrum
fft_freq = np.fft.fftfreq(Fs, T)
# taking only positive part for x axis
frequencies = fft_freq[:Fs//2]

# Fast Fourier Transform
fft_signal = np.fft.fft(signal)
# taking only positive part for y axis
fft_amp = np.abs(fft_signal)[:Fs//2]
# normalizating
fft_norm = fft_amp*(1/Fs)

plt.figure()
plt.plot(frequencies, fft_norm)
plt.title("FFT")
plt.xlabel("Hz")
plt.ylabel("Amplitude/Fs")
plt.show()

print("ALIASING:")
print("First case (sampling_rate >= 2*f):")
print("There is no aliasing, because the frequency components that pass through the low-pass filter belong to the original signal.")
print("Second case (sampling_rate < 2*f):")
print("There is aliasing, because the frequency components that pass through the low-pass filter do not belong to the original signal will actually be harmonic components.")