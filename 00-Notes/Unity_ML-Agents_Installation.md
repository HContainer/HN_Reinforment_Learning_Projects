## Installation Step (For Window)
Detail Procedure shall refer to the offical documentations \
https://unity-technologies.github.io/ml-agents/Installation/

However, belows are some key steps / alternative way which work for me when I fail to follow in the step described in the offical pages

**1 Unity** \
Install Unity Hub \
https://unity.com/download \
Activate Your Unity License \
Install Unity Editor

**2 ML-Agents Package** \
Clone the ML-Agents Toolkit Repository
```
git clone --branch release_20 https://github.com/Unity-Technologies/ml-agents.git
```
Install Unity Package (com.unity.ml-agents) by local installation \
Install Unity Package (com.unity.ml-agents.extensions) by local installation (Optional for myself)

**3 Python Version** \
Upgrade Python to 3.8.13 to 3.10.8 (You might need to setup seperate env) \
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html
```
conda create -n py310 python=3.10.8 anaconda
```
Activate installed python env
```
conda activate py310
```
*Deactivate python env
```
conda deactivate
```

**4 Virtual Env** \
Setup Virtual Env \
https://unity-technologies.github.io/ml-agents/Using-Virtual-Environment/ \
Activate Virtual Env
```
python-envs\sample-env\Scripts\activate
```
*Deactivate Virtual Env
```
python-envs\sample-env\Scripts\deactivate
```

**5 PyTorch** \
Install PyTorch (Check for latest version) \
```
pip3 install torch~=1.13.1 -f https://download.pytorch.org/whl/torch_stable.html
```

https://pytorch.org/get-started/locally/

**6 ml-agent Python Package** \
cd to cloned repo mlagents folder
Install ```mlagents``` Python Package
```
cd ml-agents-envs
pip3 install -e ./
cd ..
cd ml-agents
pip3 install -e ./
```
python -m pip install mlagents==0.30.0

Test installation success
```
mlagents-learn --help
```
