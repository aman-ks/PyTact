import math
import numpy
from numpy.fft import fft as fft
from scipy.fftpack import dct
from scipy.io import wavfile

numCoefficients = 13
minHz = 0
maxHz = 22.000
blockSize = 2048

def find_mfcc(signal):
    complexSpectrum = fft(signal)
    powerSpectrum = abs(complexSpectrum) ** 2
    mat = melFilterBank(len(powerSpectrum))
    print mat , mat.shape
    print powerSpectrum , powerSpectrum.shape
    filteredSpectrum = numpy.dot(melFilterBank(len(powerSpectrum)),powerSpectrum)
    logSpectrum = numpy.log(filteredSpectrum)
    dctSpectrum = dct(logSpectrum, type=2)

    return dctSpectrum

def melFilterBank(blockSize):
    numBands = int(numCoefficients)
    maxMel = int(freqToMel(maxHz))
    minMel = int(freqToMel(minHz))

    # Create a matrix for triangular filters, one row per filter
    filterMatrix = numpy.zeros((numBands, blockSize))

    melRange = numpy.array(xrange(numBands + 2))

    melCenterFilters = melRange * (maxMel - minMel) / (numBands + 1) + minMel

    # each array index represent the center of each triangular filter
    aux = numpy.log(1 + 1000.0 / 700.0) / 1000.0
    aux = (numpy.exp(melCenterFilters * aux) - 1) / 22050
    aux = 0.5 + 700 * blockSize * aux
    aux = numpy.floor(aux)
    centerIndex = numpy.array(aux, int)

    for i in xrange(numBands):
        start, centre, end = centerIndex[i:i + 3]
        k1 = numpy.float32(centre - start)
        k2 = numpy.float32(end - centre)
        up = (numpy.array(xrange(start, centre)) - start) / k1
        down = (end - numpy.array(xrange(centre, end))) / k2

        filterMatrix[i][start:centre] = up
        filterMatrix[i][centre:end] = down

    return filterMatrix

def freqToMel(freq):
    return 1127.01048 * math.log(1 + freq / 700.0)

def melToFreq(mel):
    return 700 * (math.exp(mel / 1127.01048 - 1))
    
    
sampleRate, signal = wavfile.read("output.wav")
output = find_mfcc(signal)
print output    
