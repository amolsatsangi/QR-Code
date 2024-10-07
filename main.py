from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

# Initializing app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        memory = BytesIO()
        data = request.form.get('link')  # Getting the input from form
        if data:  # Check if data is not empty
            image = qrcode.make(data)
            image.save(memory)
            img_io = BytesIO()
            image.save(img_io, 'PNG')
            memory.seek(0)
            base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
            return render_template('index.html', data=base64_img)
    # For GET request or if no data is provided, render the form without QR code
    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
