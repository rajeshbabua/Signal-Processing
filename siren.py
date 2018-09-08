from scipy.io.wavfile import write
from numpy import arange, pi, sin, int16



#################the process of defining a signal
####carrier signal is a modulated signal which contains message signal..
####modulaition is a process of varying carrier a signal with modulatiing signal that contains information to be transferred

def f(t, f_c, f_m, beta):
    # t    = time
    # f_c  = carrier frequency
    # f_m  = modulation frequency
    # beta = modulation index
    return sin(2*pi*f_c*t - beta*sin(2*f_m*pi*t))

def to_integer(signal):
    # Take samples in [-1, 1] and scale to 16-bit integers,
    # values between -2^15 and 2^15 - 1.
    return int16(signal*(2**15 - 1))

N = 48000 # samples per second
x = arange(3*N) # three seconds of audio

################time t=x/N
############varying the frequency of the signal one can get different signals
data = f(x/N, 1500, 2, 100)
write("slow.wav", N, to_integer(data))

data = f(x/N, 1500, 8, 100)
write("fast.wav", N, to_integer(data))
