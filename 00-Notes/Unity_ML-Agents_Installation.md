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
I use Python 3.9, since I face some library issue while installing mlagent python package
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html
```
conda create -n py39 python=3.9 anaconda
```
Activate installed python env
```
conda activate py39
```
*Deactivate python env
```
conda deactivate
```

**4 Virtual Env** \
Setup Virtual Env \
https://unity-technologies.github.io/ml-agents/Using-Virtual-Environment/ \
```
md python-envs
python -m venv python-envs\sample-env
```
Activate Virtual Env
```
python-envs\sample-env\Scripts\activate
```
*Deactivate Virtual Env
```
python-envs\sample-env\Scripts\deactivate
```
Update pip
```
python.exe -m pip install --upgrade pip
```

**5 PyTorch** \
Install PyTorch (Check for latest version) \
```
pip3 install torch -f https://download.pytorch.org/whl/torch_stable.html
```

**6 ml-agent Python Package** \
cd to cloned repo mlagents folder
Install ```mlagents``` Python Package
```
cd ml-agents
cd ml-agents-envs
pip3 install -e ./
```
```
cd ..
cd ml-agents
pip3 install -e ./
```

**7 Test installation success**
```
mlagents-learn --help
```
```
mlagents-learn --ENV_Path
```
