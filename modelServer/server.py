import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib.pyplot as plt
#import seaborn as sns
import soundfile
import librosa
#import librosa.display
from scipy.fftpack import fft

from Model import getModel
from Features import getFeatures

import os

def socket_write(input_str):
    client.send( bytes(input_str+'\n', 'utf-8'))

model_path='cnn_modelaug1_win1sec_noise_epoch1000'

labelData, model=getModel(model_path)


app = Flask(__name__)


@app.route('/', methods = ['POST'])
def soundclf():
    try:
        sound = request.get_data()
        
        sound_data=np.array(list(map(float,sound.rstrip(',').split(','))))
        
        feats = getFeatures(sound_data)
        
        preds = model.predict(feats)

        pred = labelData(np.argmax(preds, axis=1))


        if client:
            socket_write(preds)
            
        return table[claass[0]]
    except Exception as e:
        print(e)
        return 'error'
    else:
        return 'done'

import socket
import time
from _thread import *
import atexit
client=''

def threaded():
    global client
    while True:
        client, addr = s.accept()
        print("new connection established!!")
        #client.settimeout(5)
        if not client.recv(1024):
            print("disconnect!!!")
            client.close()

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('0.0.0.0', 8585 ))
#s.listen(1)
#start_new_thread(threaded,tuple())

def handleExit():
    global s,client
    print("EXIT")
    if client:
        client.close()
    s.close()
#atexit.register(handleExit)

app.run(host='0.0.0.0', port= 9999, ssl_context='adhoc')
