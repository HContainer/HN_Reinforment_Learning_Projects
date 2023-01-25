# Unity ML-Agents

## Unity ML-Agents Toolkit
![image](https://user-images.githubusercontent.com/40123599/165355949-0f3fc8f2-90f8-43d4-885e-6a55fe948d95.png)
https://unity.com/products/machine-learning-agents


**[Important Documents]** \
**Git-Hub - Main Page** \
https://github.com/Unity-Technologies/ml-agents
 
**Git-Hub - Unity ML-Agents Toolkit Documentation** \
https://github.com/Unity-Technologies/ml-agents/tree/main/docs
 
**Git-Hub - Getting Started Guide** \
https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Getting-Started.md
 
**Git-Hub  - Agents** \
https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Design-Agents.md
 
**Git-Hub - Training Configuration** \
https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-Configuration-File.md

## Installation Step (Window)
Detail Procedure shall refer to the offical documentations \
https://unity-technologies.github.io/ml-agents/Installation/

However, belows are some key steps / alternative way which work for me when I fail to follow in the step described in the offical pages

1-Install Unity Hub \
https://unity.com/download \
2-Activate Your Unity License \
3-Install Unity Editor

4-Clone the ML-Agents Toolkit Repository \
```git clone --branch release_20 https://github.com/Unity-Technologies/ml-agents.git``` \
5-Install Unity Package (com.unity.ml-agents) by local installation \
6-Install Unity Package (com.unity.ml-agents.extensions) (Optional for me) by local installation

7-Upgrade Python to 3.8.13 to 3.10.x (You might need to setup seperate env) \
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html \
8-Activate installed python env \
```conda activate $myenv```

9-Setup Virtual Env \
https://unity-technologies.github.io/ml-agents/Using-Virtual-Environment/ \
10-Activate Virtual Env

11-Install PyTroch \
https://pytorch.org/get-started/locally/ \
12-Install ```mlagents``` Python Package



## Unity ML-Agents - Basic Tutorial
**Unity - Using Machine Learning in Unity** \
https://www.youtube.com/watch?v=zPFU30tbyKs \
![image](https://user-images.githubusercontent.com/40123599/165357207-b20ef1ee-1a02-4f4f-b26e-09968485e4f8.png)

**ML-Agents 1.0+ | Create your own A.I. | Full Walkthrough | Unity3D** \
https://www.youtube.com/watch?v=2Js4KiDwiyU \
![image](https://user-images.githubusercontent.com/40123599/165357345-3f90d972-cc33-46ae-8712-697f09d6eaec.png)

**Unity ML-Agents For Beginners | Crash Course - Part 1** \
https://www.youtube.com/watch?v=HyDTboA_9pQ&list=PL6pMSU6TNEM19YvOkx2A6Tc3Shpgw9-Nc&index=18&t=196s \
![image](https://user-images.githubusercontent.com/40123599/165357414-bcee0809-2fe0-4562-88cf-aebe9f991976.png)

**How To Park A Car With Unity Machine Learning ML-Agents (Part 1)** \
https://www.youtube.com/watch?v=IcatcC9Rikk&list=PL6pMSU6TNEM19YvOkx2A6Tc3Shpgw9-Nc&index=5&t=377s \
![image](https://user-images.githubusercontent.com/40123599/165357644-7b5364d7-c28a-4fb2-992f-cdd829a0869c.png)


## How to make RL faster
**Training your agents 7 times faster with ML-Agents** \
https://blog.unity.com/technology/training-your-agents-7-times-faster-with-ml-agents \

**5 Hacks to speed up ML-Agents Training in Unity3D** \
https://www.youtube.com/watch?v=ifBXOmG9xmw&list=PL6pMSU6TNEM19YvOkx2A6Tc3Shpgw9-Nc&index=7&t=9s \
![image](https://user-images.githubusercontent.com/40123599/165358008-80176102-c40c-4b7f-8125-1fd2e4d359c3.png)

**[Hyperparameter Tuning]** \
Hyperparameter Tuning for Unity ML-Agents \
https://www.youtube.com/watch?v=ZKzXAVp8bC8&list=PL6pMSU6TNEM19YvOkx2A6Tc3Shpgw9-Nc&index=5 \
![image](https://user-images.githubusercontent.com/40123599/165358096-647fdc41-7227-473a-b4cd-4950e804c322.png)

**[Curriculum Learning]** \
Curriculum Learning | Unity ML-Agents \
https://www.youtube.com/watch?v=S0nciyOTh88&list=PL6pMSU6TNEM19YvOkx2A6Tc3Shpgw9-Nc&index=19&t=707s \
![image](https://user-images.githubusercontent.com/40123599/165358331-80a3c0ce-9331-4762-a8a2-4b8fe6397a7d.png)

**[Curriculum for Reinforcement Learning]** \
https://lilianweng.github.io/lil-log/2020/01/29/curriculum-for-reinforcement-learning.html \
![image](https://user-images.githubusercontent.com/40123599/165358422-85970fa0-34ad-44e7-8882-0ecf13187a61.png)

**[Imitation Learning]** \
Teach your AI! Imitation Learning with Unity ML-Agents! \
https://www.youtube.com/watch?v=supqT7kqpEI&list=PL6pMSU6TNEM19YvOkx2A6Tc3Shpgw9-Nc&index=11 \
![image](https://user-images.githubusercontent.com/40123599/165358491-ca6e598c-f657-4b8b-af37-c7325b98ea70.png)

Unity ML-agent with Demonstration as part of the training \
https://gamedevacademy.org/unity-machine-learning-training-tutorial/
![image](https://user-images.githubusercontent.com/40123599/165358632-bb69da19-1708-412c-ace5-b220963e271f.png) \
_Remark:_ \
_in config file, demo shall be demo_path_

**[Curiosity]** \
Curiosity Killed the AI Airplane (Unity ML-Agents) \
https://www.youtube.com/watch?v=WXDyjxWUcKI&t=128s \
![image](https://user-images.githubusercontent.com/40123599/165359002-071258aa-48a4-42bd-94ba-9ca7bf72cdc6.png)

**[Solving sparse-reward tasks with Curiosity]** \
https://blog.unity.com/technology/solving-sparse-reward-tasks-with-curiosity
![image](https://user-images.githubusercontent.com/40123599/165359062-f897f519-7bf6-4de8-a667-cc36543fb75d.png)

