from sklearn.datasets import load_wine

dataset = load_wine()
dataset

dataset.data

dataset.feature_names

import pandas as pd
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df.head()

dataset.target

# categoryを追加
df['category'] = dataset.target
df.head()

# データ数の確認
df.shape

# サンプルデータの分割
x = dataset.data
y = dataset.target

from sklearn.model_selection import train_test_split

train_test_split(x, y, test_size=0.3, random_state=5)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=5)

print(x.shape, x_train.shape, x_test.shape, y_train.shape, y_test.shape)

#予測モデルのインスタンス化
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=3)

# 予測モデルの学習
model.fit(x_train, y_train)

# 予測モデルの評価
y_pred = model.predict(x_test)
y_pred

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

