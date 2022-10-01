from flask import Flask,request,jsonify

flaskApp = Flask(__name__)

@flaskApp.route("/sound", methods=["POST"])
def sound():
    soundData = request.get_json()["sound"]
    return soundData

@flaskApp.route("/getSoundResult", methods=["GET"])
def getSoundResult():
    return "WA_SANS"

@flaskApp.route("/test", methods=["POST"])
def test():
    return "ZipGaGoSipDa"

flaskApp.run(host="0.0.0.0", debug=True, port= 80)
