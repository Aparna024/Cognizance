import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
a=ser.str.capitalize()
for i in a:
    print(i,end=' ')