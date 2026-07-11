# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(np.__version__)
    arr = np.array([10, 20, 30, 40, 50, 60])
'''
# Pass a list of indices [1, 4, 2] to extract elements
    indices = [1, 4, 2]
    print(arr[indices])
    print(arr[[1,4,2]])
    # Output: [20 50 30]

    #Reading a file from a database
    data = pd.read_csv("sales_data.csv")
    print(data.info())
    print(data.describe)
    print(data.columns)
    print(data.shape)
    print(data.head(10))
    print(data.tail(10))
'''

# concat
df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})
df3 = pd.DataFrame({'C': ['C0', 'C1'], 'D': ['D0', 'D1']})
df4 = pd.DataFrame({'B': ['B4', 'B5'], 'C': ['C4', 'C5']})

print(df1, '\n')
print(df2, '\n')

# Stack vertically and reset the index
result = pd.concat([df1, df2], ignore_index=True)
#print(result)

tagged_result = pd.concat([df1, df2], keys=['Batch_1', 'Batch_2'])
#print(tagged_result)

inner_result = pd.concat([df1, df4], join='inner', ignore_index=True)
#print(inner_result)

result_horizontal = pd.concat([df1, df3], axis=1)
#print(result_horizontal)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
