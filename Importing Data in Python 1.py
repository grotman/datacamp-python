# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 06:39:21 2017

@author: mgrotowski
"""

# =============================================================================
#                FLAT FILES using context manager
# =============================================================================

print("CONTEXT MANAGER")

# plain text file: creating connection to it, reading, closing, printing
filename = 'D:\Python_Anaconda\DataCamp\Data\some_flat_file.txt'
file = open(filename, mode='r')
print(file)
text = file.read()
print(file.closed)
file.close()
print(file.closed)
print(text[0:100])

# context manager: no need to worry about closing the file
# context managers are used for things that have some inherent clean up
# procedure like files, sockets or database connections. When one of these is
# opened then it should be closed otherwise memory leaks will happen.
# Context manager takes care of doing this clean up no matter what happens in
# the code (including exceptions)
with open(filename, 'r') as file2:
    print(file2.readline())
print(file2)
print(file2.closed)

# =============================================================================
#                FLAT FILES using NumPy
# =============================================================================
# Using NumPy to import purely numeric data: basic import, skipping headers
# importing only selected columns
print("NUMPY")
import numpy as np

filename = \
    r'D:\Python_Anaconda\DataCamp\Data\tab_delimited_numerical_values.txt'
data = np.loadtxt(filename, delimiter='\t')
print(data)

filename2 = \
    r'D:\Python_Anaconda\DataCamp\Data\tab_delimited_numerical_values_with_header.txt'
data2 = np.loadtxt(filename2, delimiter='\t', skiprows=1)
print(data2)

data3 = np.loadtxt(filename2, delimiter='\t', skiprows=1, usecols=[0, 2])
print(data3)

# Importing mixed data using Numpy and creating structured array (each row of
# the data is a single element of the array; the array is 1D ndarray)
# Letting Numpy guess data types
filename4 = r'D:\Python_Anaconda\DataCamp\Data\tab_delimited_mixed_data.txt'
data4 = np.genfromtxt(filename4, delimiter='\t', names=True, dtype=None)
print(data4)
print(data4[1])
print(data4['Var2'])

# Same effect may be achieved by using recfromtxt function (by default it
# guesses data types and assumes header line)
data5 = np.recfromtxt(filename4, delimiter='\t')
print(data5)

# =============================================================================
#                FLAT FILES using Pandas
# =============================================================================
print("PANDAS")
import pandas as pd

# importing the data from text file
dataPD_1 = pd.read_csv(filename, delimiter='\t')
print(dataPD_1.head())

# converting to NumPy array
dataPD_1_narray = dataPD_1.values
print(dataPD_1_narray)

# importing given number of rows and ignoring header line
dataPD_2 = pd.read_csv(filename2, delimiter='\t', header=1, nrows=2)
print(dataPD_2)

# handling header line
dataPD_2_with_headers = pd.read_csv(filename2, delimiter='\t', header=1,
                                    nrows=2, names = ['Var1', 'Var2', 'Var3'])
print(dataPD_2_with_headers)

# handling missing values

# =============================================================================
#                Pickled files
# =============================================================================
# These are binary files
 
import pickle
myDict = {'firstKey': 1, 'secondKey': 2}
print(myDict)

# pickling a dictionary
fName = r'D:\Python_Anaconda\DataCamp\Data\dict_dump.pkl'
with open(fName, 'wb') as file:
    pickle.dump(myDict, file, protocol=pickle.HIGHEST_PROTOCOL)

# reading from pickle
with open(fName, 'rb') as file2:
    myDict2 = pickle.load(file2)
print(myDict2)

# =============================================================================
#                Excel files
# =============================================================================
# Importing Excel files using pandas

import pandas as pd
fName = r'D:\Python_Anaconda\DataCamp\Data\creditcard_small.xlsx'
data = pd.ExcelFile(fName)
print(data.sheet_names)
sheet1 = data.parse(0)
sheet1 = data.parse('creditcard')
print(sheet1.head())

# skipping the first two rows, choosing & renaming columns
sheet2 = data.parse('creditcard', skiprows=[1, 2, 3],
                    parse_cols=[1, 2, 3], names=['Col1', 'Col2', 'Col3'])
print(sheet2.head())

# =============================================================================
#                HDF5 files
# =============================================================================

import h5py
fName = r'D:\Python_Anaconda\DataCamp\Data\ligo.hdf5'
data = h5py.File(fName, 'r')
print(type(data))

for key in data.keys():
    print(key)

for key in data['meta'].keys():
    print(key)

print(data['meta']['Description'].value)
print(data['meta']['DescriptionURL'].value)
print(data['meta']['Detector'].value)

for key in data['strain'].keys():
    print(key)

strainData = data['strain']['Strain'].value
print(type(strainData))
print(strainData)
print(np.shape(strainData))
print(strainData[:10])

# =============================================================================
#                RELATIONAL DATABASES (SQLITE)
# =============================================================================

# The examples are done using SQLite and SQLAlchemy package, as well as pandas
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
        'sqlite:///D:\\Python_Anaconda\\DataCamp\\Data\\chinook.db')

# listing the tables in the database
tables = engine.table_names()
print(tables)

# connecting and querying data
con = engine.connect()
rs = con.execute('SELECT * FROM albums')
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()
print(df.head())

rs2 = con.execute('SELECT * FROM artists')
df2 = pd.DataFrame(rs2.fetchall())
df2.columns = rs2.keys()
print(df2.head())

# closing the connection
con.close()

# Doing similar query using context manager
with engine.connect() as con:
    rs = con.execute('SELECT Title FROM albums')
    df = pd.DataFrame(rs.fetchmany(size=10))
    df.columns = rs.keys()
    print(df.head())

# Using pandas to achieve the same
df = pd.read_sql_query('SELECT Title FROM albums', engine)
print(df.head())

# Pandas and more advanced SQL (inner join)
df3 = pd.read_sql_query(
    'SELECT Title, Name FROM albums INNER JOIN artists on albums.ArtistId = artists.ArtistId', 
    engine)
print(df3.head())

# =============================================================================
#                CONTEXT MANAGERS - MORE INFO
# =============================================================================

# Technically context manager is a class with two special methods:
# * __enter__() - it returns the resource to be managed
# * __exti__() - does any clean up work and returns nothing
# Example:

print("CONTEXT MANAGER 2")


class File():
    """Redundant files context manager"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()


files = []
for f in range(10):
    with File('foo' + str(f) + '.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)
for f in files:
    print(f.closed)

# Context managers are so useful, they have a whole Standard Library module
# devoted to them. contextlib contains tools for creating and working with
# context managers. One nice shortcut to creating a context manager from a
# class is to use the @contextmanager decorator. To use it, decorate a
# generator function that calls yield exactly once. Everything before the call
# to yield is considered the code for __enter__(). Everything after is the code
# for __exit__().
# Let's rewrite the File class using this approach

from contextlib import contextmanager


@contextmanager
def File2(filename, mode):
    file2 = open(filename, mode)
    yield file2
    file2.close()


# Let's now try it
files2 = []
for f in range(10):
    with File2('boo' + str(f) + '.txt', 'w') as infile:
        infile.write('boo')
        files2.append(infile)
for f in files2:
    print(f.closed)
