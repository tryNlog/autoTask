#!/usr/bin/env python
# coding: utf-8

# In[1]:

def chasuMail():
    import pandas as pd
    import plotly.express as px
    sample_1 = pd.read_excel('IFILE',
                       header = 0,
                       usecols = 'A:H')
    df = sample_1.dropna()
    callChasu = int(input("메일을 발송할 차수를 입력하세요 : "))
    chasuSel = df.loc[(df['차수']  == callChasu)]
    chasuAdd = chasuSel['e-mail']
    return chasuAdd

# In[2]:

chasuMail().values
# %%

