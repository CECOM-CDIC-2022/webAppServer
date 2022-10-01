import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM, Conv2D, MaxPooling1D, AveragePooling1D, MaxPooling2D, Dropout, BatchNormalization, Activation, Flatten
from keras.activations import relu, sigmoid
from tensorflow.keras import activations
from tensorflow.keras.optimizers import Adam
import librosa
import pandas as pd
import numpy as np

import os

class ConvBlock(tf.keras.layers.Layer):
    def __init__(self, in_channels, out_channels, pool_size=(2, 2), **kwargs):
        super(ConvBlock, self).__init__()
        #self.t, self.t1 = in_channels, out_channels
        self.in_channels=in_channels
        self.out_channels=out_channels
        self.conv1 = Conv2D(self.out_channels, 3, padding='same')
        self.conv2 = Conv2D(self.out_channels, 3, padding='same')

        self.bn1 = BatchNormalization()
        self.bn2 = BatchNormalization()
        self.pool_size = pool_size
        self.mxpool = MaxPooling2D(pool_size=self.pool_size)
    def call(self, input_tensor):

        x = self.conv1(input_tensor)

        x = self.bn1(x)
        x = relu(x)
        x = self.conv2(input_tensor)
        x = self.bn2(x)
        x = relu(x)


        x = self.mxpool(x)
        return x

    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'in_channels': self.in_channels,
            'out_channels': self.out_channels,
            'pool_size': self.pool_size
        })
        return config

    
class AverageBlock(tf.keras.layers.Layer):
    def __init__(self, axis, **kwargs):
        super(AverageBlock, self).__init__()
        self.axis=axis

    def call(self, input_tensor):
        input_tensor = tf.reduce_mean(input_tensor, 1)
        return input_tensor

    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'axis': self.axis
        })
        return config

class Pool1dBlock(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(Pool1dBlock, self).__init__()
        self.pool1 = MaxPooling1D(3, strides=1, padding='same')
        self.pool2 = AveragePooling1D(3, strides=1, padding='same')

    def call(self, input_tensor):

        return self.pool1(input_tensor)+self.pool2(input_tensor)

def getModel__(num_labels, model_path='cnn_modelaug1_win1sec_noise_epoch1000', batch_size=4):
        
    cnn_model = Sequential()

    cnn_model.add(ConvBlock(1, 64, pool_size=(2, 2)))
    cnn_model.add(Dropout(0.2))
    cnn_model.add(ConvBlock(64, 128, pool_size=(2, 2)))
    cnn_model.add(Dropout(0.2))
    cnn_model.add(ConvBlock(128, 256, pool_size=(2, 2)))
    cnn_model.add(Dropout(0.2))
    cnn_model.add(ConvBlock(256, 512, pool_size=(2, 2)))
    cnn_model.add(Dropout(0.2))
    cnn_model.add(ConvBlock(512, 1024, pool_size=(2, 2)))
    cnn_model.add(Dropout(0.2))
    cnn_model.add(ConvBlock(1024, 2048, pool_size=(1, 1)))
    cnn_model.add(Dropout(0.2))
    cnn_model.add(AverageBlock(1))

    cnn_model.add(Pool1dBlock())

    cnn_model.add(Dense(2048, activation='relu'))
    cnn_model.add(Dropout(0.5))
    cnn_model.add(Dense(512, activation='relu'))
    cnn_model.add(Dropout(0.5))
    cnn_model.add(Flatten())
    cnn_model.add(Dense(256, activation='sigmoid'))
    cnn_model.add(Dense(num_labels, activation='sigmoid'))
    
    input_shape = (batch_size, 64, 276, 1)
    input_shape
    cnn_model.build(input_shape)
    print(cnn_model.summary())
        
    filename = os.path.join(model_path, 'cnn_model_checkpoint.h5')

    cnn_model = tf.keras.models.load_model(filename,
                                          custom_objects={
                                                    "ConvBlock":ConvBlock,
                                                    "AverageBlock":AverageBlock,
                                                    "Pool1dBlock":Pool1dBlock
                                                    })
    
def getModel(model_path='cnn_modelaug1_win1sec_noise_epoch1000', batch_size=4):
    sample_rate=44100
    wav_files = os.listdir("dataset/media")
    meta_files = os.listdir("dataset/metadata")
    files = [f.split('.')[0] for f in wav_files]

    cut_data = []
    label_data = []
    for file in files:
        y,__=librosa.load("dataset/media/"+file+".wav", sr=sample_rate)

        x = pd.read_csv("dataset/metadata/"+file+".txt", names=['start', 'end', 'label'], header=None, delimiter  = '\t')
        for i in x.index:
            start_ = int(x['start'][i]*sample_rate)
            end_ = int(x['end'][i]*sample_rate)
            cut_data.append(y[start_:end_])
            label_data.append(x["label"][i])

    label_data+=["noise"]
    label_data

    label_data = np.sort(np.unique(label_data))
    num_labels = len(label_data)
    return label_data, getModel__(num_labels, model_path, batch_size) 
