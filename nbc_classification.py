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

def read_file(filename):
