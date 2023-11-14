import pandas as pd

data = {
    'employee_001': [160, 187], # 松田の1か月の労働時間
    'employee_002': [165, 175]  # 浅木の1か月の労働時間
}

df = pd.DataFrame(data)
print(df)
print(df.shape) # 行数や列数を調べるメソッド

