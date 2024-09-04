# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:06:09 2024

@author: Dragana Majstorovic
"""
import math
import random

# simulates accessing the element of the list
def access(list, index):
    return list[index]


# Secretary Problem Phase
def secretary_problem(list, access_frequency):
    n = len(list)
    threshold = int(n/math.e)
    least_accessed = 0
    
    for i in range(threshold):
        if access_frequency[list[i]] < access_frequency[list[least_accessed]]:
            least_accessed = i
            
    for i in range(threshold, n):
        if access_frequency[list[i]] > access_frequency[list[least_accessed]]:
            list[i], list[least_accessed] = list[least_accessed], list[i]
            

# Metropolis-Hastings Phase
def metropolis_hastings(list, access_frequency, iterations):
    for _ in range(iterations):
        
        n = len(list)
        # Randomly choose an element to move
        i = random.randint(int(n/math.e), n - 1)
        j = random.randint(int(n/math.e), n - 1)
        
        if i == j:
            continue
        if i > j:
            i, j = j, i
        
        # Calculate the acceptance probability
        freq_i = access_frequency[list[i]]
        freq_j = access_frequency[list[j]]
        
        if freq_i == 0:
            if freq_j == 0:
                alpha = 0.5
            else:
                alpha = 1
        else:
            alpha = min(1, (freq_j / freq_i))

        # Accept or reject the proposed move
        if random.uniform(0, 1) < alpha:
            # Swap elements at positions i and j
            list[i], list[j] = list[j], list[i]
            

def self_organizing_list(list, access_frequency):
    
    secretary_problem(list, access_frequency)

    # Could be adjusted according to our needs
    iterations = 1000
    
    metropolis_hastings(list, access_frequency, iterations)
    

if __name__ == '__main__':
    
    list = []
    
    # Generates a list of 100 (or any other number) elements
    for i in range(1,101):
        list.append("element " + str(i))
    
    n = len(list)

    # Dictionary to keep track of access frequencies
    access_frequency = {element_i: 0 for element_i in list}
    
    # Simulates access to randomly chosen elements
    # Could be adjusted according to our needs
    for _ in range(5000):
        element = access(list, random.randint(0, n-1))
        access_frequency[element] += 1
        self_organizing_list(list, access_frequency)
        
    for i in range(0, len(list)):
        print(list[i] + " - " + str(access_frequency.get(list[i])))
            
            