from flask import Flask ,render_template ,request
from io import BytesIO
import base64, json
import numpy as np
from PIL import Image
from datetime import datetime

app= Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/DigitRecognition',methods=['GET','POST'])
def Execpy():
    result = {"predict_digit" :"!", "detect_img" :"", "centering_img" :"", "prob" :{}}
    if request.method == 'POST' :
        # retrive the image
        postImg = BytesIO(base64.urlsafe_b64decode(request.form['img']))

        #save digits 
        '''
        postImg = Image.open(postImg)
        postImg.save("./saveImage/{}_save.png".format(datetime.now().strftime('%m-%d_%H.%M.%S')))
        '''
    return json.dumps(result)
    

if __name__== '__main__':
    app.run(debug=True)