#!/usr/bin/env python
# coding: utf-8

# In[1]:



def chasuMan():
    import pandas as pd
    import plotly.express as px
    import os

    rawPath = os.path.abspath("IPATH")

    sample_1 = pd.read_excel(f'{rawPath}/IFILE',
                       header = 3,
                       usecols = 'A:E')
    df = sample_1.dropna()
    callChasu = int(input("파일을 생성할 차수를 입력하세요 : "))
    chasuOn = df[df['차수'] == callChasu]
    return chasuOn

# %%
