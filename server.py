from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np
from keras.models import load_model
from keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from keras.preprocessing.image import img_to_array, load_img
import os
import tensorflow as tf

app = Flask(__name__)

# モデルの読み込み
def load_mobilenet_model():
    global model
    model = load_model('./mobile_net_model.h5')
    global graph
    graph = tf.get_default_graph()


def img_pred(image):

    # 読み込んだ画像を行列に変換
    img_array = img_to_array(image)
    
    # 3次元を4次元に変換
    img_dims = np.expand_dims(img_array, axis=0)

    # Top3のクラスの予測
    with graph.as_default():
            preds = model.predict(preprocess_input(img_dims))

    # imagenet_class_index.json をダウンロードし、その中から認識結果を表示
    results = decode_predictions(preds, top=3)[0]
    
    # resultsを整形
    result = [result[1] + " : " +"{:.2%}".format(result[2]) for result in results]
    return result


@app.route('/')
def index():
    return render_template('./flask_api_index.html')

@app.route('/result', methods=['POST'])
def result():
    # submitした画像が存在したら処理する
    if request.files['image']:
        # 画像の読み込み, 224 * 224にリサイズ
        image_load = load_img(request.files['image'], target_size=(224,224))

        # クラスの予測をする関数の実行
        predict_Confidence = img_pred(image_load)

        # render_template('./result.html')
        return render_template('./result.html', title='予想クラス', predict_Confidence=predict_Confidence)

# CSSのキャッシュを無くす
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':
    load_mobilenet_model()
    app.debug = True
    app.run(host='localhost', port=5000)