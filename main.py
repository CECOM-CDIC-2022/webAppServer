from flask import Flask,request,jsonify

flaskApp = Flask(__name__)

@flaskApp.route("/sound", methods=["POST"])
def test():
    return "WA_SANS"

@flaskApp.route("/test", methods=["POST"])
def test():
    return "ZipGaGoSipDa"

flaskApp.run(host="0.0.0.0", debug=True, port= 80)
