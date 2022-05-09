import csv
import random
import math
import pandas as pd

def generate_file(prob_1, prob_2):
    data = []
    for i in range(1000):
        variant = round(random.random())
        if variant == 1:
            if math.floor(random.random() * 100) > (100-prob_1):
                yes = 1
                no = 0
            else:
                yes = 0
                no = 1
        else:
            if math.floor(random.random() * 100) > (100-prob_2):
                yes = 1
                no = 0
            else:
                yes = 0
                no = 1
        data.append([variant, yes])
    return pd.DataFrame(data, columns = ['variant', 'clicked yes'])