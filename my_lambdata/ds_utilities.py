import pandas as pd 

#Summary null values
def null(X):
    X = X.copy()
    null_val = X.isnull().sum()
    null_S = pd.Series(null_val)
    X = pd.DataFrame({'column': null_S.index, 'Total': null_S})
    X = X.reset_index(drop=True)
    return X

#Date split
def date_split(X, date):
    X=X.copy()
    X['day']= pd.to_datetime(X[date]).dt.day
    X['month']=pd.to_datetime(X[date]).dt.month
    X['year']=pd.to_datetime(X[date]).dt.year

    return X