#!/bin/python3

import sys
import pandas as pd
import matplotlib.pyplot as plt

fileA = str(sys.argv[1])
fileB = str(sys.argv[2])
t = int(sys.argv[3])

df_A = pd.read_csv(fileA)
df_B = pd.read_csv(fileB)

df_A.drop('Unnamed: 0', axis=1, inplace=True)
df_B.drop('Unnamed: 0', axis=1, inplace=True)

df_A.replace(to_replace=-3.0, value=0.5, inplace=True)
df_B.replace(to_replace=-3.0, value=0.5, inplace=True)

# Create Graphs
fig, ax = plt.subplots(1,3, figsize=(18,4))
x = df_B.index
y = df_B['confidence']

plotB = ax[0].plot(x, y, marker='o')
plotA_1 = ax[1].plot(df_A.index, df_A['confidence'], marker='o', color='green')
plotA_2 = ax[2].plot(df_A.index, df_A['mood'], marker='o', color='green')

ax[0].grid()
ax[1].grid()
ax[2].grid()

ax[0].set_xlabel('No. Iterations')
ax[1].set_xlabel('No. Iterations')
ax[2].set_xlabel('No. Iterations')

ax[0].set_ylabel('Confidence')
ax[1].set_ylabel('Confidence')
ax[2].set_ylabel('Mood Rating')

fig.legend([plotB, plotA_1, plotA_2], labels=['Robot B', 'Robot A'])

plt.savefig('graph/graph%s.png' % t, bbox_inches='tight')
plt.show()
