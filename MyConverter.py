import tensorflow as tf
from socket import *
class Converter:

    def tfliteConvert(self):
        model=tf.keras.models.load_model('uploads/temp2.h5')
        tflite_converter = tf.lite.TFLiteConverter.from_keras_model(model)
        tflite_model = tflite_converter.convert()
        open("downloads/converted_temp.tflite", "wb").write(tflite_model)

