import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv("out.csv")

df['stars2'] = df['stars'].str[:1]
df['stars2'] = df['stars2'].astype(int)


print (df)

df.set_index('id')[['comments_count', 'stars2']].plot.bar()
plt.show()