# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 06:33:42 2017

@author: mgrotowski
"""

import pandas as pd

dataFile = 'D:\Python_Anaconda\DataCamp\Data\EEA-educ-fertility-bubbles.csv'

df = pd.read_csv(dataFile)
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.info())