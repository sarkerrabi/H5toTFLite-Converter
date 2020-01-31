import os
from flask import Flask, request, render_template, url_for, redirect
from flask import send_file
import MyConverter
app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('index.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    tfconvert = MyConverter.Converter()
    status = False
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            photo.save(os.path.join('uploads', "temp2.h5"))
            tfconvert.tfliteConvert()
            status = True
            return  render_template('index.html',status= status, downloadUrl= '/download')
        else:
            return redirect(url_for('fileFrontPage'))

    else:
        return redirect(url_for('fileFrontPage'))

@app.route('/download')
def downloadFile ():
    path = "downloads/converted_temp.tflite"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
   app.run(debug = True)


# model=tf.keras.models.load_model('autoencoder_final_result_32.h5')
# tflite_converter = tf.lite.TFLiteConverter.from_keras_model(model)
# tflite_model = tflite_converter.convert()
# open("converted_autoencoder_final_result_32.tflite", "wb").write(tflite_model)
