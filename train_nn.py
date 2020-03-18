import pandas as pd
print(pd.__version__)
import numpy  as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras import Sequential
from keras.layers import Dense
import tensorflow as tf
from sklearn.utils import class_weight

df_sig_800 = pd.read_pickle('TChiWZ_1000_1_MC2018.pkl')
df_sig_1000 = pd.read_pickle('TChiWZ_800_1_MC2018.pkl')
df_sig_600 = pd.read_pickle('TChiWZ_600_1_MC2018.pkl')
df_bkg = pd.read_pickle('ZJetsToNuNu_HT_MC2018.pkl')
#df_bkg=df_bkg.sample(frac=.005).reset_index(drop=True)

df = pd.concat([df_sig_1000,df_sig_800,df_sig_600,df_bkg])
df = df.sample(frac=1).reset_index(drop=True)
#print df

X, y = df.values[:, :-1], df.values[:, -1]

print X[:10]
print y[:10]

# ensure all data are floating point values
X = X.astype('float32')
# encode strings to integer
y = LabelEncoder().fit_transform(y)

print y[:10]

# split into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
                
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# determine the number of input features
n_features=X_train.shape[1]

# define model
model = Sequential()
model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(10, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(10, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(1, activation='sigmoid'))

class_weights = class_weight.compute_class_weight('balanced',
                                                 np.unique(y_train),
                                                 y_train)

# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

# fit the model
model.fit(X_train, y_train, epochs=20, batch_size=5000, verbose=1,callbacks=[],validation_data=(X_test,y_test),class_weight=class_weights)

res=model.predict(X_test)
#print res[:100]
bkg_acc=0
bkg_trials=0
sig_acc=0
sig_trials=0
for r,t in zip(res,y_test):
    if t==1:
        sig_trials+=1
        sig_acc+=int(r[0]>0.5)
    else :
        bkg_trials+=1
        bkg_acc+=int(r[0]<=0.5)
print 'sig_acc:',sig_acc,'/',sig_trials
print 'bkg_acc:',bkg_acc,'/',bkg_trials

# evaluate the model
loss, acc = model.evaluate(X_test, y_test, verbose=1)
print('Test Accuracy: %.3f' % acc)

# make a prediction
#row = [1,0,0.99539,-0.05889,0.85243,0.02306,0.83398,-0.37708,1,0.03760,0.85243,-0.17755,0.59755,-0.44945,0.60536,-0.38223,0.84356,-0.38542,0.58212,-0.32192,0.56971,-0.29674,0.36946,-0.47357,0.56811,-0.51171,0.41078,-0.46168,0.21266,-0.34090,0.42267,-0.54487,0.18641,-0.45300]
#yhat = model.predict([row])
#print('Predicted: %.3f' % yhat)
