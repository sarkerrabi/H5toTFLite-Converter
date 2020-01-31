import tensorflow as tf

model=tf.keras.models.load_model('autoencoder_final_result_32.h5')
tflite_converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = tflite_converter.convert()
open("converted_autoencoder_final_result_32.tflite", "wb").write(tflite_model)
