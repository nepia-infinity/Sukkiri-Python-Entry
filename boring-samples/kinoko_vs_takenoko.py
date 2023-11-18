import pandas as pd

# フルパスを指定
path = r'C:\Users\nepia\OneDrive\ドキュメント\Sukkiri-Python-Entry\sukkiri-ml-codes\datafiles\KvsT.csv'

# CSVファイルの読み込み
df = pd.read_csv(path)

# 最初の3行を表示
# print(df.head(3))
print(df)
