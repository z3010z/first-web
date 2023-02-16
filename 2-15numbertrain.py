from keras.datasets import mnist

(X_train,Y_train),(X_test,Y_test)=mnist.load_data()

print(X_train[0])
print(Y_train[0])

import tensorflow.keras as keras
import pandas as pd
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from keras.utils.np_utils import to_categorical
(X_train,Y_train),(X_test,Y_test)=mnist.load_data()
X_train=X_train.reshape(X_train.shape[0],28,28,1)
X_train=X_train.astype("float32")
print("X_train Shape:", X_train.shape)
X_test=X_test.reshape(X_test.shape[0],28,28,1)
X_test=X_test.astype("float32")
print("X_test Shape:", X_test.shape)

X_train=X_train/255
X_test=X_test/255

Y_train=to_categorical(Y_train)
Y_test=to_categorical(Y_test)
print("Y_train Shape:",Y_train.shape)
print(Y_train[0])

model=Sequential()
model.add(Conv2D(8,kernel_size=(5,5),padding="same",
input_shape=(28,28,1),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(16,kernel_size=(5,5),padding="same",
activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(16,kernel_size=(5,5),padding="same",
activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(64,activation="relu"))
model.add(Dense(10,activation="softmax"))
model.summary()

model.compile(loss="categorical_crossentropy",optimizer="adam", metrics=["accuracy"])

history=model.fit(X_train,Y_train,validation_split=0.2,epochs=10,
batch_size=128,verbose=2)

loss,accuracy=model.evaluate(X_train,Y_train)
print("訓練資料集的準確度={:.2f}".format(accuracy))
loss,accuracy=model.evaluate(X_test,Y_test)
print("測試資料集的準確度={:.2f}".format(accuracy)) 

#匯入所須模組及套件
import tensorflow.keras as keras
import pandas as pd
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from keras.utils.np_utils import to_categorical

#載入MNIST數據集
(X_train,Y_train),(X_test,Y_test)=mnist.load_data()
#將訓練的資料轉換為浮點數
X_train=X_train.reshape(X_train.shape[0],28,28,1)
X_train=X_train.astype("float32")
#print("X_train Shape:", X_train.shape)
X_test=X_test.reshape(X_test.shape[0],28,28,1)
X_test=X_test.astype("float32")
#print("X_test Shape:", X_test.shape)
#進行正規化處理
X_train=X_train/255
X_test=X_test/255
#將標籤資料執行One-hot encoding
Y_train=to_categorical(Y_train)
Y_test=to_categorical(Y_test)
#print("Y_train Shape:",Y_train.shape)
#print(Y_train[0])
#定義模型
model=Sequential()
model.add(Conv2D(8,kernel_size=(5,5),padding="same",
input_shape=(28,28,1),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(16,kernel_size=(5,5),padding="same",
activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(16,kernel_size=(5,5),padding="same",
activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(64,activation="relu"))
model.add(Dense(10,activation="softmax"))
model.summary()

#編譯模型
model.compile(loss="categorical_crossentropy",optimizer="adam", metrics=["accuracy"])
#訓練模型
history=model.fit(X_train,Y_train,validation_split=0.2,epochs=10,
batch_size=128,verbose=2)
#評估模型
loss,accuracy=model.evaluate(X_train,Y_train)
print("訓練資料集的準確度={:.2f}".format(accuracy))
loss,accuracy=model.evaluate(X_test,Y_test)
print("測試資料集的準確度={:.2f}".format(accuracy))