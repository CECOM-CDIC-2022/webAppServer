from flask import Flask,request,jsonify
from librosa import resample
flaskApp = Flask(__name__)

@flaskApp.route("/sound", methods=["POST"])
def sound():
    soundData = request.get_json()["sound"]
    soundData = resample(soundData, orig_sr=len(soundData)/4, target_sr=22050)
    return soundData

@flaskApp.route("/getSoundResult", methods=["GET"])
def getSoundResult():
    resultFile = open("SOUND_DATA", "r")

    resultData = resultFile.readline()

    resultFile.close()
    return resultData

@flaskApp.route("/test", methods=["POST"])
def test():
    return "ZipGaGoSipDa"

flaskApp.run(host="0.0.0.0", debug=True, port= 80)
