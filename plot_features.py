#TChiWZ_1000_1_MC2018.pkl
#TChiWZ_800_100_MC2018.pkl
#TChiWZ_800_700_MC2018.pkl
#TChiWZ_600_1_MC2018.pkl
#TChiWZ_800_1_MC2018.pkl
#ZJetsToNuNu_HT_MC2018.pkl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def log_norm(x):
    x=map(np.log,x+0.000001)
    m=np.mean(x)
    s=np.std(x)
    return m,s,map(lambda x : (x-m)/s,x)
def norm(x):
    m=np.mean(x)
    s=np.std(x)
    return m,s,map(lambda x : (x-m)/s,x)

dfsig=  pd.read_pickle('data/TChiWZ_1000_1_MC2018.pkl')
dfbkg= pd.read_pickle('data/ZJetsToNuNu_HT_MC2018.pkl')

trans={'j1px':norm,
       'j1py':norm,
       'j1pz':norm,
       'j2px':norm,       
       'j2py':norm,
       'j2pz':norm,       
       'j3px':norm,
       'j3py':norm,       
       'j3pz':norm,
       'j4px':norm,
       'j4py':norm,
       'j4pz':norm,
       'j5px':norm,
       'j5py':norm,
       'j5pz':norm,
       'j6px':norm,
       'j6py':norm,
       'j6pz':norm,
       'j7px':norm,
       'j7py':norm,
       'j7pz':norm,
       'j8px':norm,
       'j8py':norm,
       'j8pz':norm,
       'j1e':log_norm,
       'j2e':log_norm,
       'j3e':log_norm,
       'j4e':log_norm,
       'j5e':log_norm,
       'j6e':log_norm,
       'j7e':log_norm,
       'j8e':log_norm,
       'met':log_norm
}

df = pd.concat([dfsig,dfbkg])

print df.columns

for col in df.columns[:-1]:
    plt.hist(trans[col](df[df['zlabel']==0][col].values)[-1],histtype='step',normed=True)
    plt.hist(trans[col](df[df['zlabel']==1][col].values)[-1],histtype='step',normed=True)
    plt.savefig(col+'.png')
    plt.clf()
    plt.cla()
