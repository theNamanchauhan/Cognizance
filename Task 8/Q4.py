import pandas as pd
ser=pd.Series(['amrita','school','of','engineering','chennai' ,'campus'])
#Capitializing 'ser'
x=ser.str.capitalize()
for y in x:
    print(y,end=" ")