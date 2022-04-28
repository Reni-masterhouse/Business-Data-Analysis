import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

#数据清洗
df = pd.DataFrame(pd.read_csv('/Users/liling/Desktop/dataamazon/text.csv', encoding='gbk'))
summary = df['Summary']
df.groupby('Score')

print(summary)
