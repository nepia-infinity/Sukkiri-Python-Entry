import pandas as pd
import sklearn
from sklearn import tree

print(sklearn.__file__)
print(pd.__file__)

# フルパスを指定
path = r'C:\Users\nepia\OneDrive\ドキュメント\Sukkiri-Python-Entry\sukkiri-ml-codes\datafiles\KvsT.csv'

# CSVファイルの読み込み
df = pd.read_csv(path)

# 最初の3行を表示
print(df.head(3))
# print(df)

# 列のみを抽出する
# print(df['派閥'])

# SELECT的な事が出来る
# col = ['身長', '体重']
# print(df[col]) 

# 学習の入力データ
columns = ['身長', '体重', '年代']
x = df[columns]
print(x)

# 正解データ（派閥）を参照して, tに代入
t = df['派閥']
print(t) 

# モデルの準備（未学習）
model = tree.DecisionTreeClassifier(random_state = 0)

# 学習の実行
model.fit(x, t)

# taroがどちらに分類されるか予測する
taro = pd.DataFrame([[170, 70, 20]], columns=['身長', '体重', '年代'])
denomination = model.predict(taro) 
print(f"taroの派閥は、{denomination[0]}です。")