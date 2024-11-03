import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib

df = pd.read_csv(r"C:\Users\328ma\OneDrive\デスクトップ\侍エンジニア\機械学習\sample_pandas_6.csv")
category_df = pd.read_csv(r"C:\Users\328ma\OneDrive\デスクトップ\侍エンジニア\機械学習\category.csv")

df = pd.merge(df, category_df[['商品番号', 'カテゴリー']], how='inner', on='商品番号')

count = df['カテゴリー'].value_counts()

count.plot(kind='bar')

plt.title("Frequency of each category")
plt.xlabel("category")
plt.ylabel("frequency")
plt.show()

order = df.groupby('商品番号')['注文数'].describe()
print(order)