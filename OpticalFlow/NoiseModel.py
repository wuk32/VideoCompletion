# coding=utf8
import numpy as np
import math

class GaussianMixture(object):
    def __init__(self, nchannels=0):
        self.nchannels = nchannels
        self.alpha = []
        self.sigma = []
        self.beta = []
        self.sigma_square = []
        self.beta_square = []
        for i in range(nchannels):
            self.alpha.append(0.95)
            self.sigma.append(0.05)
            self.beta.append(0.5)

        self.square()

    def square(self):
        for i in range(self)
            self.sigma_square.append(self.sigma[i] ** 2)
            self.beta_square.append(self.beta[i] ** 2)


    def Guassian(x, i, k):
        if i == 0:
            return np.exp(-x / (2 * self.sigma_square[k])) / (2 * math.PI * self.sigma[k])
        else:
            return np.exp(-x / (2 * self.sigma_square[k])) / (2 * math.PI * self.sigma[k])
        