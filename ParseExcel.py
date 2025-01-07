import json

import pandas as pd

df = pd.read_excel('./resource/test.xlsx')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(df[['编号', '标题']])
print(df.iloc[[0]])

for i in df.index:
    for j in df.columns:
        print(df.loc[i, j])

login_case_type = df[df["请求接口类型"] == "登录"]
print(login_case_type)

login_case_data = login_case_type["输入数据"][0]
print(json.loads(login_case_data))