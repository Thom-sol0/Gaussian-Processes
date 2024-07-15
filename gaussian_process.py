import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd
from typing import Union, List, Callable


class GaussianProcess:
    def __init__(self, 
                 mean_function: Callable = lambda x: 0, 
                 covariance_function: Union[str, Callable] = "exp"):
        self.m = mean_function
        if type(covariance_function) == str:
            if covariance_function == "exp":
                covariance_function = lambda x, y: np.exp(-np.linalg.norm(x - y))
            else:
                raise ValueError("Invalid covariance function")
        else:
            self.k = covariance_function
    
    def select_random(self, values_set: np.ndarray):
        