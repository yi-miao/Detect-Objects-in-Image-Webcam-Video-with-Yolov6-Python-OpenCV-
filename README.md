Detect Objects in Image/Webcam/Video with Yolov6 (Python, OpenCV)

Many years ago, I did my PhD research in London UK on Intelligent Agent, 
a branch of AI, with the tools like prolog. With the inputs of facts and rules, 
you kicked off inference engine and get the results. It sounds like "Stone Age" story.
After working as consultant on Data Analysis in Financial Industry about 20 years, 
I have chances to review some great tools developed in recent years like 
Tensorflow, Keras and Yolo.

I learned Yolov6 [Ref 1] and found it is significantly improved to 
Yolov3 which I played just in the early of this year 2022. In this project,
I share and report how I use Yolov6 to detect objects in image files,
video files and webcam with different ways, some simple scripts from 
Yolov6, some modified addressing my own interests.

System Environments
1. CPU only
2. MS Windows 11
3. Python 3.9.7
4. OpenCV 4.5.5
4. Jupyter Notebook

Instructions
- Step 1 - Clone yolov6 at YOLOv6 [Ref 1]:  
git clone https://github.com/rkuo2000/YOLOv6
cd YOLOv6
- Step 2 - Install required packages [Ref 1]:  
pip install -r requirements.txt
- Step 3 - Download Model weights [Ref 1]:  
wget https://github.com/meituan/YOLOv6/releases/download/0.1.0/yolov6n.pt
create a new directory cfg  
move the weights file there, i.e. YOLOv6/cfg/yolov6n.pt 
- Step 4 - Download imageInference.py (modified) [Ref 2]:  
create a new directory yolov6_vc under YOLOv6, i.e. YOLOv6/yolov6_vc
- Step 5 - Copy your test files  
copy your image files and video files to the directory of YOLOv6/data/images  
I use street.mp4 [Ref 3] as example
- Step 6 - Modified the settings in code (jupyter nb) 
Some Examples:  
  source: test image and video files (yolov6: imnage1.jpg etc.)  
  indir: the directory with test files (yolov6: data/images)  
  outdir: the output files (yolov6: runs/inference/exp)  
  weights: model weight file  
  device: cpu, gpu etc.  
Step 7 - Run the scripts and check the results.  

- [Ref 1] https://github.com/meituan/YOLOv6
- [Ref 2] https://github.com/RATHOD-SHUBHAM/DeepLearning/tree/e203e7c4942fee6860e2c340ce0973663e73d4ca/Object%20Detection%20Using%20Yolov6/ObjDet_yolov6
- [Ref 3] This is a free sample mp4 file downloaded from web, but I could not remember the URL. Many thanks to them to provide this video!
