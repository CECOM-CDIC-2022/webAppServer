from flask import Flask,request,jsonify
import requests
import os

flaskApp = Flask(__name__)

@flaskApp.route("/sound", methods=["POST"])
def sound():
    soundData = request.get_json()["sound"]
    
    resultURL = os.environ["MODEL_SERVER_ADDR"]
    resultData = requests.post(resultURL, soundData).text
    # resultData = "noise,noise,noise,noise"

    dataFile = open("SOUND_DATA", "r")
    tempData = eval(dataFile.readline())
    dataFile.close()

    resultData = resultData.lower()

    print(resultData)

    if resultData.find("on") != -1:
        if resultData.find("lg") != -1:
            if (resultData.find("drum") != -1) or (resultData.find("washer") != -1):
                # LG Washer ON
                tempData["LG_WASHER"] = True
            else:
                # LG Air Purifier ON
                tempData["LG_AIRPURIFIER"] = True
        else:
            if (resultData.find("bubble") != -1) or (resultData.find("washer") != -1):
                # Samsung Washer ON
                tempData["SAMSUNG_WASHER"] = True
            else:
                # Samsung Air Conditioner ON
                tempData["SAMSUNG_AIRCONDITIONER"] = True
    elif (resultData.find("off") != -1) or (resultData.find("done") != -1):
        if resultData.find("lg") != -1:
            if (resultData.find("drum") != -1) or (resultData.find("washer") != -1):
                # LG Washer ON
                tempData["LG_WASHER"] = False
            else:
                # LG Air Purifier ON
                tempData["LG_AIRPURIFIER"] = False
        else:
            if (resultData.find("bubble") != -1) or (resultData.find("washer") != -1):
                # Samsung Washer ON
                tempData["SAMSUNG_WASHER"] = False
            else:
                # Samsung Air Conditioner ON
                tempData["SAMSUNG_AIRCONDITIONER"] = False

    resultFile = open("SOUND_DATA", "w")
    resultFile.write(str(tempData))
    resultFile.close()

    return soundData

@flaskApp.route("/getSoundResult", methods=["GET"])
def getSoundResult():
    targetDevice = request.args.get("devID")

    resultFile = open("SOUND_DATA", "r")
    resultData = eval(resultFile.readline())
    resultFile.close()

    if targetDevice in resultData:
        return str(resultData[targetDevice])

    return str(False)

@flaskApp.route("/test", methods=["POST"])
def test():
    return "ZipGaGoSipDa"

flaskApp.run(host="0.0.0.0", debug=True, port= 80)
