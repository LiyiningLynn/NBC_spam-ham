%matplotlib notebook
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from bs4 import BeautifulSoup

import re
import os, sys, stat
import email
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import csv

def loadCsv(filename):
  lines = csv.reader(open(filename,"rb"))
  dataset = list(lines)
  for i in range(len(dataset)):
    dataset[i] = [float(x) for x in dataset[i]]
  return dataset
'''
preprocess
'''
filename = 'pima-indians-diabetes.data.csv'
dataset = loadCsv(filename)
print('Loaded data file {0} with {1} rows').format(filename, len(dataset))

def read_file(filename):
