import pandas as pd 

#Summary null values
def summary(X):
    ''' This Function will return the columns names as index,null_value_count,any unique character we specify & its percentage of occurance per column.'''
    null_values = X.apply(lambda x:X.isnull().sum())
    blank_char = X.apply(lambda x:X.isin(['?']).sum())
    percent_blank_char =X.apply(lambda x:round((X.isin(['?']).sum()/X.shape[0])*100, 2))
    unique_values = X.apply(lambda x:len(X.unique()))
    return pd.DataFrame({'null_values':null_values,
                         '? Values':blank_char,'% ? Values':percent_blank_char
                        ,'unique_values':unique_values})

#Date split
def date_split(X, date):
    X=X.copy()
    X['day']= pd.to_datetime(X[date]).dt.day
    X['month']=pd.to_datetime(X[date]).dt.month
    X['year']=pd.to_datetime(X[date]).dt.year

    return X