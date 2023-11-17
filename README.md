# Eyesight-Check-by-gesture-recognition
## ��Ŀ���
����Ŀ��һ����������ʶ����������Web����ģ��Ϊ���� `MobileNetV2` Ԥѵ��+����ѧ�����������������Ƭѵ�����ɡ�������Ƭѵ������ `�������/dataset`������ʹ�õ�ģ�ͼ� `�������/out_file/hands_new.onnx`��
## ʹ�÷���
���� `ver1.3.ipynb`��������������д�һ������Web��������ͼ��ʾ��  
![Web_APP](pic/web_app.png)  
��߻���Ϊ�����ʵʱ��׽���ұ߻���Ϊ�Զ����յĽ�ͼ������ʶ������ָ��  
����ʱ��������վ�����������ĻԼ5m��������ʾ���������ɵõ����µ�������Χ���硰�߶Ƚ��ӡ������жȽ��ӡ��ȣ��������Ӧ���������鲥�š�
## ע������
����Ŀּ���ó���ѧ������AI�ƴ����̣�����Ϊһ���ƴ������ʵ�֣���ʵ��ҽ�ƽ����޹ء�
## Introduction
This project is a web app for eyesight checks based on gesture recognition. The model used in the process is pretrained on `MobileNetV2` then trained on a gesture dataset made by some junior high school students. The gesture dataset can be found in `�������/dataset`. The model finally used can be found in `�������/out_file/hands_new.onnx`.
## Usage
Run `ver1.3.ipynb`, and a local web app will be open in the browser, as shown below.  
![Web_APP](pic/web_app.png)    
The window on the left displays a live video stream from the camera, and the window on the right shows the image used for direction recognition captured automatically.  
When running the test, the volunteer should stand 5m away from the screen. Follow the sound instruction, and an approximate result will be generated, such as "severely short-sighted", or "moderately short-sighted", etc. Meanwhile, an audio clip of advice on protecting eyes will be played.
## Attention!
All the audio contents are in Chinese.  
This project is meant to let junior high school students experience how to apply AI to science projects. It is only made to display a scientific idea, and has nothing to do with real-life medical advice.
