import numpy as np
import pandas as pd
import string

#调用数据
df = pd.read_csv('text.csv', encoding='gbk')

#以score项分组
score_group = df.groupby('Score')

#进行词频分析
lines = []
for score, g in score_group:
    print('Score', score)
    word_count = {}
    def add_word(w):
        if w not in word_count:
            word_count[w] = 0
        word_count[w] += 1
    
    total = 0
    for s in g['Summary']:
        try:
            words = s.translate(str.maketrans('', '', string.punctuation)).strip().split()
            for w in words:
                if w.isalpha():
                    add_word(w.lower())
            total += 1
        except:
            pass
    
    sorted_words = sorted(word_count.items(), key= lambda kv: kv[1], reverse=True)
    for word, count in sorted_words[:50]:
        lines.append(f'{word},{count},{score},{count*1.0/total}\n')

#生成csv文件        
with open('word.csv', 'w') as f:
    f.writelines(lines)

