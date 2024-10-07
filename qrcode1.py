from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode
#Getting server up and running 
#Initializing app
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
    

@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()
    print("***************************")
    data = request.form.get('link')
    print(data)
    image = qrcode.make(data)
    image.save(memory)
    memory.seek(0)
    
    base64_img = "data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii')
    print(base64_img)
    return render_template('index.html', data=base64_img)
    
