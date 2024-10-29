# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:11:01 2024

@author: Nick Work
"""

import numpy as np

def calculate(input: list):
    '''
    Function that takes an input list containing 9 elements, reshapes to a 
    3 x 3 matrix, and computes mean, variance, SD, max, min, and sum values
    along both long and wide axes, as well as the flattened array. Values are
    converted from numpy arrays to lists and returned as a dictionary
    '''
    if len(input) < 9:
        raise ValueError("List must contain nine numbers.") # Raise error if input shape doesn't match expected
    else:
        _data = np.reshape(input,(3,3)) # Reshape array to 3 x 3 matrix
        mean = [list(_data.mean(axis=0)), list(_data.mean(axis=1)), _data.mean()] # Calculate row mean, column mean, flattened mean
        variance = [list(np.var(_data,axis=0)),list(np.var(_data,axis=1)),np.var(_data)] # Calculate row variance, column variance, flattened variance
        std = [list(_data.std(axis=0)),list(_data.std(axis=1)),_data.std()] # Calculate row SD, column SD, and flattened SD
        data_max = [list(_data.max(axis=0)),list(_data.max(axis=1)),_data.max()] # Determine row max, column max, and max of matrix
        data_min = [list(_data.min(axis=0)),list(_data.min(axis=1)),_data.max()] # Determine row min, column min, and min of matrix
        data_sum = [list(np.sum(_data,axis=0)),list(np.sum(_data,axis=1)),np.sum(_data)] # Calculate row sum, column sum, and flattened sum
        return {'mean': mean, # Return lists of values as a dictionary
                'variance': variance,
                'standard deviation': std,
                'max': data_max,
                'min': data_min,
                'sum': data_sum}