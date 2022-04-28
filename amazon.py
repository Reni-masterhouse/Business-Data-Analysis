import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

#数据清洗
df = pd.DataFrame(pd.read_csv('/Users/liling/Desktop/dataamazon/Reviews.csv'))

#查找空值
#isNA=df.isnull()
#a = df[isNA.any(axis=1)]
#print(a)

#处理数据
#求各产品的评论数
# data1 = df.groupby(by='ProductId').count().sort_values(by = 'UserId', ascending = False)[:100]['UserId']
data1 = df.groupby(by='ProductId').count().sort_values(by = 'UserId', ascending = False)[:100]['UserId'].sum()
# ['UserId']
print(data1)
exit(0)

#求各产品的平均分
#grouped = df['Score'].groupby(df['ProductId'])
#meanscore = grouped.mean()
#data2 = meanscore.sort_values(ascending = False)
#print(data2)

#求各用户的评论数
#data3 = df.groupby(by='UserId').count().sort_values(by = 'ProductId', ascending = False)[:10]['ProductId']
#print(data3)

#求各用户的平均分
#group = df['Score'].groupby(df['UserId'])
#meanuser = group.mean()
#data4 = meanuser.sort_values(ascending = False)
#print(data4)

#_x = data1.index
#_y = data1.values

#画图
#plt.figure(figsize=(10, 8), dpi = 80)
#plt.bar(range(len(_x)), _y, width = 0.5)

#plt.xticks(range(len(_x)), _x)
#plt.xlabel("UserId")
#plt.ylabel("Number of comments")
#plt.title("Top 10 UserIds with comments", size = 20)
#plt.show()
