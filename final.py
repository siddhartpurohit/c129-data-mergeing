#Importing all the modules we need.
import pandas as pd

df = pd.read_csv('dwarf_stars.csv')
df.head()

df = df.dropna()

df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]

df.head()

df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.head()
df.reset_index(drop=True,inplace=True)
df.to_csv("brightest_stars.csv")
