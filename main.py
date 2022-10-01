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

    resultData = resultData.lower()
    if resultData.find("on") != -1:
        if resultData.find("lg") != -1:
            if (resultData.find("drum") != -1) or (resultData.find("washer") != -1):
                # LG Washer ON
                pass
            else:
                # LG Air Purifier ON
                pass
        else:
            if (resultData.find("bubble") != -1) or (resultData.find("washer") != -1):
                # Samsung Washer ON
                pass
            else:
                # Samsung Air Conditioner ON
                pass
    elif (resultData.find("off") != -1) or (resultData.find("done") != -1):
        if resultData.find("lg") != -1:
            if (resultData.find("drum") != -1) or (resultData.find("washer") != -1):
                # LG Washer OFF
                pass
            else:
                # LG Air Purifier OFF
                pass
        else:
            if (resultData.find("bubble") != -1) or (resultData.find("washer") != -1):
                # Samsung Washer OFF
                pass
            else:
                # Samsung Air Conditioner OFF
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
