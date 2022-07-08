import pandas as pd
import collections
import logging
import os
import pathlib
import re
import string
import sys
import time

import numpy as np
import matplotlib.pyplot as plt

import tensorflow_datasets as tfds
import tensorflow as tf
import tensorflow as text
from transformers import BertTokenizer, BertModel
import transformers

 
df = pd.read_csv("data/csv/data.csv", encoding= "utf-8")

print(df)




bert_tokenizer_params=dict(lower_case=True)
gk_tokenizer = transformers.BertTokenizer(df["Word"], **bert_tokenizer_params)
en_tokenizer = transformers.BertTokenizer(df["Definition"], **bert_tokenizer_params)