## Name
Object Classification API

## Overview
Select image and classify object using Mobile Net

## Description
It is an API that store the learning model of mobilenet implemented by keras, loads the model on the server, and classifies the object.<br>
Use flask to set up and load model on server.<br>
Go to `http://localhost:5000/` in your browser and select an image to view the classification results.<br>

## Demo
<img width="1435" alt="sample1" src="https://user-images.githubusercontent.com/38250390/55782549-7f3a8e80-5ae7-11e9-951a-c60d38124009.png">
<img width="1438" alt="sample2" src="https://user-images.githubusercontent.com/38250390/55782593-97aaa900-5ae7-11e9-86a4-dc9c801e0641.png">

## Requirement
Keras==2.2.4<br>
Keras-Applications==1.0.6<br>
Keras-Preprocessing==1.0.5<br>
tensorboard==1.12.0<br>
tensorflow==1.12.0<br>
Flask==1.0.2<br>

## Install
$ pip install -r requirement.txt

## Usage
1. $ python3 save_mobilenet_model.py
2. $ python3 server.py
3. Access `http://localhost:5000/` .
4. Select image and push submit.


## Contributing
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Licence
MIT