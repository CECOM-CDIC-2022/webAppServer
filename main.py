from flask import Flask,request,jsonify
import requests
import os

flaskApp = Flask(__name__)

@flaskApp.route("/sound", methods=["POST"])
def sound():
    soundData = request.get_json()["sound"]
    
    resultURL = os.environ["MODEL_SERVER_ADDR"]
    # resultData = requests.post(resultURL, soundData).text
    resultData = "noise,noise,noise,noise"

    dataFile = open("SOUND_DATA", "r")
    tempData = eval(resultFile.readline())
    dataFile.close()

    if resultData.find("ON") != -1:
        pass
    elif (resultData.find("OFF") != -1) or (resultData.find("DONE") != -1):
        pass

    resultFile = open("SOUND_DATA", "w")
    resultFile.write(resultData)
    resultFile.close()

    return soundData

@flaskApp.route("/getSoundResult", methods=["GET"])
def getSoundResult():
    targetDevice = request.args.get("devID")

    resultFile = open("SOUND_DATA", "r")

    resultData = resultFile.readline()

    resultFile.close()
    return resultData

@flaskApp.route("/test", methods=["POST"])
def test():
    return "ZipGaGoSipDa"

flaskApp.run(host="0.0.0.0", debug=True, port= 80)
