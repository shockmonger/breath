import scipy, numpy as np, pandas as pd, matplotlib.pyplot as plt
import matplotlib.animation as animation, seaborn as sns


#read data
df1 = pd.DataFrame.from_csv('./HackLab_Vol1_Excerpts/HackLab_Vol1_Excerpts/Vol1_P1_1_Exrpt.csv')
df2 = pd.DataFrame.from_csv('./HackLab_Vol1_Excerpts/HackLab_Vol1_Excerpts/Vol1_P2_1_Exrpt.csv')
df3 = pd.DataFrame.from_csv('./HackLab_Vol1_Excerpts/HackLab_Vol1_Excerpts/Vol1_P2_2_Exrpt.csv')
df1 = df1.reset_index(drop=True)
df2 = df2.reset_index(drop=True)
df3 = df3.reset_index(drop=True)
# cols1 = df1.keys()
# cols2 = df2.keys()
# cols3 = df3.keys()
cols = ['frog','wolf','ser6e','sve','steel','siss','fergie', 'cris', 'padrino','henry']


#separate all columns containing EMG and allocate to EMG COlumn
X_1 = df1.columns[df1.columns.str.contains('ACC X')]
Y_1 = df1.columns[df1.columns.str.contains('ACC Y')]
Z_1 = df1.columns[df1.columns.str.contains('ACC Z')]
X_1 = pd.DataFrame.dropna(X1,axis=0)
Y_1= pd.DataFrame.dropna(Y1,axis=0)
Z_1 = pd.DataFrame.dropna(Z1,axis=0)
EMG_1 = df1.columns[df1.columns.str.contains('EMG')]
X1 = df1[X_1]
X1.columns=cols
Y1 = df1[Y_1]
Y1.columns=cols
Z1 = df1[Z_1]
Z1.columns=cols
EMG1 = df1[EMG_1]
EMG1.columns=cols



X_2 = df2.columns[df2.columns.str.contains('ACC X')]
Y_2 = df2.columns[df2.columns.str.contains('ACC Y')]
Z_2 = df2.columns[df2.columns.str.contains('ACC Z')]
EMG_2 = df2.columns[df2.columns.str.contains('EMG')]
X2 = df2[X_2]
Y2 = df2[Y_2]
Z2 = df2[Z_2]
EMG2 = df2[EMG_2]
X2.columns=cols
Y2.columns=cols
Z2.columns=cols
EMG2.columns=cols


X_3 = df3.columns[df3.columns.str.contains('ACC X')]
Y_3 = df3.columns[df3.columns.str.contains('ACC Y')]
Z_3 = df3.columns[df3.columns.str.contains('ACC Z')]
EMG_3 = df3.columns[df3.columns.str.contains('EMG')]
X3 = df3[X_3]
Y3 = df3[Y_3]
Z3 = df3[Z_3]
EMG3 = df3[EMG_3]
X3.columns=cols
Y3.columns=cols
Z3.columns=cols
EMG3.columns=cols



#basic stats for all different data
X1 = pd.DataFrame.dropna(X1,axis=0)
Y1= pd.DataFrame.dropna(Y1,axis=0)
Z1 = pd.DataFrame.dropna(Z1,axis=0)



Y1diff = np.diff(Y1,axis=1)


#separate x, y, z accelometers



# line chart scrollable


#