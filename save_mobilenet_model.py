import numpy as np
from keras.models import load_model
from keras.applications.mobilenet import MobileNet

# Mobile Net
model = MobileNet(weights="imagenet")
    
# モデルの保存、モデルをロードした後予測しかしないため、include_optimizer=Falseとする
model.save('mobile_net_model.h5', include_optimizer=False)