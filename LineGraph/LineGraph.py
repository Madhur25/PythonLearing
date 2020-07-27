import pandas as pd
import matplotlib.pyplot as plt
#read excel
df = pd.read_excel (r'Counts2.xlsx', sheet_name='sheet_name')
plt.plot(df.Month,df.EbayCounts,color='green', marker='o',label='E Counts')
plt.plot(df.Month,df.GSPCounts,color='olive', marker='o',label='G Counts')
plt.xlabel('Month')
plt.ylabel('Counts')
# To display the label on graph
plt.legend()
plt.show()