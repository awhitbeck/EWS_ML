import uproot
import pandas as pd

def fixed_len_arr(arr,fix_len=8):
    arr_fix=[0.]*fix_len
    for i in range(min(len(arr),fix_len)):
        arr_fix[i] = arr[i]
    return arr_fix

def concat_data(met,jpx,jpy,jpz,je):
    return [met]+jpx+jpy+jpz+je

#tree = uproot.open("/home/vhegde/Physics/EW_SUSY/RA2bTrees_V17/EW_SUSY/skims/ForFullyResolved/ZJetsToNuNu_HT_MC2018.root")["tree;1"]
#tree = uproot.open("/home/vhegde/Physics/EW_SUSY/RA2bTrees_V17/EW_SUSY/skims/ForFullyResolved/TChiWZ_800_700_MC2018.root")["tree;1"]
#tree = uproot.open("/home/vhegde/Physics/EW_SUSY/RA2bTrees_V17/EW_SUSY/skims/ForFullyResolved/TChiWZ_800_100_MC2018.root")["tree;1"]
#tree = uproot.open("/home/vhegde/Physics/EW_SUSY/RA2bTrees_V17/EW_SUSY/skims/ForFullyResolved/TChiWZ_800_1_MC2018.root")["tree;1"]
#tree = uproot.open("/home/vhegde/Physics/EW_SUSY/RA2bTrees_V17/EW_SUSY/skims/ForFullyResolved/TChiWZ_600_1_MC2018.root")["tree;1"]
tree = uproot.open("/home/vhegde/Physics/EW_SUSY/RA2bTrees_V17/EW_SUSY/skims/ForFullyResolved/TChiWZ_1000_1_MC2018.root")["tree;1"]

met = tree.array("MET")
jpt = tree.array("Jets").pt
jpx = tree.array("Jets").x[jpt>30.]
jpy = tree.array("Jets").y[jpt>30.]
jpz = tree.array("Jets").z[jpt>30.]
je = tree.array("Jets").t[jpt>30.]

jpx_fixed = map(lambda x : fixed_len_arr(x),jpx)
jpy_fixed = map(lambda x : fixed_len_arr(x),jpy)
jpz_fixed = map(lambda x : fixed_len_arr(x),jpz)
je_fixed = map(lambda x : fixed_len_arr(x),je)

data = map(lambda a,b,c,d,e: concat_data(a,b,c,d,e),met,jpx_fixed,jpy_fixed,jpz_fixed,je_fixed)

data = zip(*data)

df = pd.DataFrame({'met':data[0],
                   'j1px':data[1],
                   'j2px':data[2],
                   'j3px':data[3],
                   'j4px':data[4],
                   'j5px':data[5],
                   'j6px':data[6],
                   'j7px':data[7],
                   'j8px':data[8],
                   'j1py':data[9],
                   'j2py':data[10],
                   'j3py':data[11],
                   'j4py':data[12],
                   'j5py':data[13],
                   'j6py':data[14],
                   'j7py':data[15],
                   'j8py':data[16],
                   'j1pz':data[17],
                   'j2pz':data[18],
                   'j3pz':data[19],
                   'j4pz':data[20],
                   'j5pz':data[21],
                   'j6pz':data[22],
                   'j7pz':data[23],
                   'j8pz':data[24],
                   'j1e':data[25],
                   'j2e':data[26],
                   'j3e':data[27],
                   'j4e':data[28],
                   'j5e':data[29],
                   'j6e':data[30],
                   'j7e':data[31],
                   'j8e':data[32],
                   'zlabel':[1]*len(met)})
                   
#df = pd.DataFrame({'jpx':jpx_fixed,
#                   'jpy':jpy_fixed,
#                   'jpz':jpz_fixed,
#                   'je':je_fixed,
#                   'met':met})

#df.to_pickle('ZJetsToNuNu_HT_MC2018.pkl')
#df.to_pickle('TChiWZ_800_700_MC2018.pkl')
#df.to_pickle('TChiWZ_800_100_MC2018.pkl')
#df.to_pickle('TChiWZ_800_1_MC2018.pkl')
#df.to_pickle('TChiWZ_600_1_MC2018.pkl')
df.to_pickle('TChiWZ_1000_1_MC2018.pkl')
