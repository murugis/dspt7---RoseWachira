import pandas as pd
from pandas import DataFrame
from my_lambdata.ds_utilities import null

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': ['?', 2, 1, 8]},
                  index=['falcon', 'dog', 'spider', 'fish'])

print(null(df))

def date_split(df):
    df2= df.copy()
    df2['date']=pd.to_datetime(df2['date'],infer_datetime_format= True)

    df2['year'] = df2['date'].dt.year
    df2['month'] = df2['date'].dt.month
    df2['day'] = df2['date'].dt.day

    df2 = df2.drop(columns='date')

    return df2

def wage(hours,wage):
    if hours >40:
        wages =hours*wage
        pay = 40*wage + (hours - 40)*wage*1.5

        return pay
    else:
        return wages




#if __name__=="__main__":
    #data= pd.read_csv('')
    