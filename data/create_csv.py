import pandas as pd
from sklearn.neural_network import MLPRegressor
from data_function import *
import numpy as np


url = "http://www.perseus.tufts.edu/hopper/vocablist?works=Perseus%3Atext%3A2008.01.0665&works=Perseus%3Atext%3A2008.01.0590&works=Perseus%3Atext%3A2008.01.0592&works=Perseus%3Atext%3A2008.01.0591&works=Perseus%3Atext%3A2008.01.0667&works=Perseus%3Atext%3A1999.01.0001&works=Perseus%3Atext%3A1999.01.0003&works=Perseus%3Atext%3A1999.01.0005&works=Perseus%3Atext%3A1999.01.0007&works=Perseus%3Atext%3A1999.01.0011&works=Perseus%3Atext%3A1999.01.0009&works=Perseus%3Atext%3A1999.01.0013&works=Perseus%3Atext%3A1999.01.0015&works=Perseus%3Atext%3A1999.01.0017&works=Perseus%3Atext%3A1999.01.0019&works=Perseus%3Atext%3A1999.01.0021&works=Perseus%3Atext%3A1999.01.0227&works=Perseus%3Atext%3A1999.01.0231&works=Perseus%3Atext%3A1999.01.0229&works=Perseus%3Atext%3A1999.01.0253&works=Perseus%3Atext%3A2008.01.0588&works=Perseus%3Atext%3A1999.01.0023&works=Perseus%3Atext%3A1999.01.0025&works=Perseus%3Atext%3A1999.01.0027&works=Perseus%3Atext%3A1999.01.0029&works=Perseus%3Atext%3A1999.01.0031&works=Perseus%3Atext%3A1999.01.0033&works=Perseus%3Atext%3A1999.01.0035&works=Perseus%3Atext%3A1999.01.0037&works=Perseus%3Atext%3A1999.01.0039&works=Perseus%3Atext%3A1999.01.0041&sort=form&filt=100&filt_custom=&output=table&lang=greek"

table_html(url)

df = table_cleaning(table_html(url))

df.to_csv("data/csv/data.csv", index = False)