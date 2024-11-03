# In[1]:

import pandas as pd  
import numpy as np  
import glob  
import sys

#파일 Union  
all_data = pd.DataFrame()  
for f in glob.glob('IPATH'): # 예를들어 201901, 201902 로 된 파일이면 2019_*  
df = pd.read_excel(f)
all_data = all_data.append(df, ignore_index=True)

#데이터갯수확인  
print(all_data.shape)

#데이터 잘 들어오는지 확인  
all_data.head()

#파일저장  
all_data.to_excel("OPATH", header=False, index=False)