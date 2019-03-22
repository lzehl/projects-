import pandas as df
import json
print('_' * 100)

data = df.read_csv("data.txt")
d = {data.iloc[0][0]: {data.iloc[0][1]: {data.iloc[0][2]: data.iloc[0][3], data.iloc[1][2]: data.iloc[1][3],
                                         data.iloc[2][2]: data.iloc[2][3]}},
     data.iloc[3][0]: {data.iloc[3][1]: {data.iloc[3][2]: data.iloc[3][3], data.iloc[4][2]: data.iloc[4][3],
                                         data.iloc[5][2]: [data.iloc[5][3], data.iloc[6][3]]}}}
print(data)
print(d)
print('metadata =', json.dumps(d, indent=10))
print('_' * 100)
