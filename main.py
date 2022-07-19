from flask import Flask,request,jsonify

@app.route('/soundclf', methods = ['POST'])
def soundclf():
    try:
        return 'F21VDT'       
    except Exception as e:
        print(e)
        return 'error'

@app.route('/soundval', methods = ['POST'])
def soundval():
    try:
        return 'True'
    except Exception as e:
        print(e)
        return 'error'

app.run(host='0.0.0.0', debug=True, port= 8080)
