from flask import Flask,request,jsonify

@app.route('/soundclf', methods = ['GET','POST'])
def postJsonHandler_class():
    if request.method == 'POST':
        try:
            return 'F21VDT'
            
        except Exception as e:
            print(e)
            #print(request.data)
            return 'error'
        
    else:
        return 'clf: not Post'

@app.route('/soundval', methods = ['GET','POST'])
#@inflate
def postJsonHandler():
    if request.method == 'POST':
        try:
            return 'True'

        except Exception as e:
            print(e)
            #print(request.data)
            return 'error'
            
    else:
        return 'val: not Post'

#여기는 알잘딱깔센
app.run(host='0.0.0.0', debug=True, port= 9999)
