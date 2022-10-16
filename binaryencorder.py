from sklearn.preprocessing import LabelEncoder, OneHotEncoder
binaryle = LabelEncoder()

count=0
for col in df1.columns[1:]:
    if df1[col].dtype == 'object':
      if len(list(df1[col].unique())) <=2:
        binaryle.fit(df1[col])
        df1[col]=binaryle.transform(df1[col])
        count += 1

print('{} columns formatted.'.format(count))
