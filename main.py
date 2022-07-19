from flask import Flask,request,jsonify

flaskApp = Flask(__name__)

@flaskApp.route('/soundclf', methods = ['POST'])
def soundclf():
    try:
        return 'F21VDT'       
    except Exception as e:
        print(e)
        return 'error'

@flaskApp.route('/soundval', methods = ['POST'])
def soundval():
    try:
        return 'True'
    except Exception as e:
        print(e)
        return 'error'

flaskApp.run(host='0.0.0.0', debug=True, port= 80)
