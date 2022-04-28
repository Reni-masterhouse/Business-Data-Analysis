import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

#数据清洗
df = pd.DataFrame(pd.read_csv('/Users/liling/Desktop/dataamazon/A3OXHLG6DIBRW8.csv', encoding='gbk'))
print(df)

#求各分数的评论次数
data1 = df.groupby(by='score').count().sort_values(by = 'number', ascending = False)[:10]['number']
print(data1)