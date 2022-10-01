import librosa
import numpy as np

def getFeatures(data, sample_rate=44100):
    if len(data)<sample_rate:
        data = np.pad(data, (0, sample_rate-len(data)), 'constant', constant_value=0)
    rdata = []
    for i in range(0, len(data), sample_rate):
        S = librosa.feature.melspectrogram(data[i:i+sample_rate], sr=sample_rate, n_fft=1024, n_mels=64, hop_length=320, win_length=None)
        log_S = librosa.power_to_db(S, ref=np.max)
        rdata.append(log_S)
        
    return rdata
