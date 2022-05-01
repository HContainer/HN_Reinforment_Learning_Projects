# Project 01 - Tensorflow Object Detection

[Youtube Tutorial] - Nicholas Renotte
https://www.youtube.com/watch?v=yqkISICHH-U&t=11444s

[Git Hub Tutorial]
https://github.com/nicknochnack/TFODCourse

## File Structure
Clone this repository: https://github.com/nicknochnack/TFODCourse
<br/><br/>

## Virtual Environemnet Setup - Skip this if using Colab for training
<b>Step 1.</b> Create a new virtual environment 
<pre>
python -m venv tfod
</pre> 
<br/>
<b>Step 2.</b> Activate your virtual environment
<pre>
source tfod/bin/activate # Linux
.\tfod\Scripts\activate # Windows 
</pre>
<br/>
<b>Step 3.</b> Install dependencies and add virtual environment to the Python Kernel
<pre>
python -m pip install --upgrade pip
pip install ipykernel
python -m ipykernel install --user --name=tfod
</pre>

<b>Step 4.</b> Install CUDA and cuDNN
Follow Nicholas's Tutorial

## Image Collection and Labling
### Step 1. Image Collection via Camera - Skip this if using image readily availabe
1 - Image Collection.ipynb [Jupyter Notebook]  \
https://github.com/Hilbert-HN/HN_Reinforcement_Learning_Projects/blob/master/03_Other_AI_Projects/01-Tensorflow%20Object%20Detection/1.%20Image%20Collection.ipynb
<br/><br/>

### Step 2. Image Labling
2a - Image Labeling Install.ipynb [Jupyter Notebook]  \
https://github.com/Hilbert-HN/HN_Reinforcement_Learning_Projects/blob/master/03_Other_AI_Projects/01-Tensorflow%20Object%20Detection/1.%20Image%20Collection.ipynb

2b - Nagivate to the labelmg files and run labelImg.py in Command Prompt
<pre>
cd TFODCourse\Tensorflow\labelimg
python labelImg.py
</pre>

2c - Start Labeling
![image](https://user-images.githubusercontent.com/40123599/166134242-381c64cc-1757-41ce-a502-7b5d4d0a4b9d.png)

### Step 3. Image Labling

## Trainig
