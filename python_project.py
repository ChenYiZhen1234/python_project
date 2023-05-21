#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #引入Pandas模組 as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_rows", 1000)    #設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000) #設定最大能顯示1000columns
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams['axes.unicode_minus'] = False


# In[5]:


df=pd.read_csv(r'C:\Users\User\Desktop\三下\whp.csv') #讀取AQI.csv


# In[7]:


filt = (df['Continent'] == 'as')#讀取亞洲
print(df.loc[filt])


# In[10]:


#只在乎此三列(亞洲部分)
filt = (df['Continent'] == 'as')
print(df.loc[filt, ['RANK', 'Country', 'Happiness score']])


# In[11]:


#計算提出資料共有幾筆(結論:亞洲有43個國家)
asiaCount=df['Continent'] == 'as'
df[asiaCount].shape


# In[6]:


#篩選Happiness score前幾名並印出結果
import pandas as pd
def filter_top_values(csv_file, column_name, num_values, selected_columns):
    # 讀取 CSV 檔案
    df = pd.read_csv(csv_file)
    
    # 按數值欄位排序
    sorted_df = df.sort_values(by=column_name, ascending=False)
    
    # 篩選前幾大的資料
    filtered_df = sorted_df.head(num_values)
    
    # 只取特定行(column)的資料
    filtered_data = filtered_df[selected_columns]
    
    return filtered_data

# 設定檔案路徑、欄位名稱、要篩選的前幾大數值、要印出的特定行(column)
csv_file = 'C:/Users/User/Desktop/三下/whp.csv'
column_name = 'Happiness score'
num_values = 5
selected_columns = ['RANK', 'Continent','Country', 'Happiness score']

# 執行篩選並印出特定行(column)的結果
filtered_data = filter_top_values(csv_file, column_name, num_values, selected_columns)
print(filtered_data)


# In[15]:


df.dtypes #顯示資料類型


# In[2]:


#篩選Happiness score大於某值並印出結果
import pandas as pd
def filter_csv_by_value(csv_file, column_name, threshold):
    # 讀取 CSV 檔案
    df = pd.read_csv(csv_file)
    
    # 篩選出數值大於某值的資料
    filtered_df = df[df[column_name] > threshold]
    
    return filtered_df

# 設定檔案路徑、欄位名稱和門檻值
csv_file = 'C:/Users/User/Desktop/三下/whp.csv'
column_name = 'Happiness score'
threshold = 7.7

# 執行篩選並輸出結果
filtered_data = filter_csv_by_value(csv_file, column_name, threshold)
print(filtered_data)


# In[5]:


#篩選Happiness score大於某值並印出特定行(column)的結果
import pandas as pd
def filter_csv_by_value(csv_file, column_name, threshold, selected_columns):
    # 讀取 CSV 檔案
    df = pd.read_csv(csv_file)
    
    # 篩選出數值大於某值的資料
    filtered_df = df[df[column_name] > threshold]
    
    # 只取特定行(column)的資料
    filtered_data = filtered_df[selected_columns]
    
    return filtered_data

# 設定檔案路徑、欄位名稱、門檻值和要印出的特定行(column)
csv_file = 'C:/Users/User/Desktop/三下/whp.csv'
column_name = 'Happiness score'
threshold = 7.0

selected_columns = ['RANK', 'Continent','Country', 'Happiness score']

# 執行篩選並印出特定行(column)的結果
filtered_data = filter_csv_by_value(csv_file, column_name, threshold, selected_columns)
print(filtered_data)


# In[7]:


#選出為asia5中前五大的資料
import pandas as pd
def filter_top_values_with_condition(csv_file, column_name, num_values, condition_column, condition_value, selected_columns):
    # 讀取 CSV 檔案
    df = pd.read_csv(csv_file)
    
    # 篩選符合條件的資料
    filtered_df = df[df[condition_column] == condition_value]
    
    # 按數值欄位排序
    sorted_df = filtered_df.sort_values(by=column_name, ascending=False)
    
    # 篩選前幾大的資料
    filtered_data = sorted_df.head(num_values)
    
    # 只取特定行(column)的資料
    filtered_data = filtered_data[selected_columns]
    
    return filtered_data

# 設定檔案路徑、數值欄位名稱、要篩選的前幾大數值、條件列名稱、條件值、要印出的特定行(column)
csv_file = 'C:/Users/User/Desktop/三下/whp.csv'
column_name = 'Happiness score'
num_values = 5
condition_column = 'Continent'
condition_value = 'as'
selected_columns = ['RANK', 'Continent','Country', 'Happiness score']

# 執行篩選並印出特定行(column)的結果
filtered_data = filter_top_values_with_condition(csv_file, column_name, num_values, condition_column, condition_value, selected_columns)
print(filtered_data)


# In[ ]:




