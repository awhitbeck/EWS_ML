#TChiWZ_1000_1_MC2018.pkl
#TChiWZ_800_100_MC2018.pkl
#TChiWZ_800_700_MC2018.pkl
#TChiWZ_600_1_MC2018.pkl
#TChiWZ_800_1_MC2018.pkl
#ZJetsToNuNu_HT_MC2018.pkl

import pandas as pd
import matplotlib.pyplot as plt
dfsig=  pd.read_pickle('TChiWZ_1000_1_MC2018.pkl')
dfbkg= pd.read_pickle('ZJetsToNuNu_HT_MC2018.pkl')

df = pd.concat([dfsig,dfbkg])

print df.columns

for col in df.columns[:-1]:
    plt.hist(df[df['zlabel']==0])
    plt.hist(df[df['zlabel']==1])
    break

plt.show()
