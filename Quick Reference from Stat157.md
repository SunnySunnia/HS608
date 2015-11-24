```
vagrant up  
vagrant ssh 
```
```
sudo apt-get install git  
git clone https://github.com/stat157/questionnaire.git  
cd questionnaire
cp example.cfg ~/stat157.cfg 
#(in questionnaire directory)
```
```
vi ~/stat157.cfg 
#(questionnaire directory)  
```
------ By pressing the 'i' key, you can switch to insert mode.  
------ Press 'Esc' to return to command mode, and :x to save and exit  

```
sudo apt-get install python-matplotlib  
sudo apt-get install python-tornado  
sudo apt-get install python-pandas
sudo apt-get install python-scipy
```
Access ipynb:
```
ipython notebook --no-browser --ip=0.0.0.0 --pylab inline  
```
ipython notebook --no-browser --ip=0.0.0.0 --script  

```
sudo apt-get update  
sudo apt-get install r-base  
sudo pip install rpy2
```

On Ipython notebook:  
-------------------------------------------------------------------------------------------------
```
import numpy as np  
import matplotlib
import matplotlib.pyplot as plt  
import pandas as pd  
from pylab import *  
%pylab inline
```

Git Push  
---------------------  
```
cp "test form.ipynb" ~/Repo  
cd Repo  
git add "test form.ipynb"  
git commit -m "test 1"  
git push  #will ask for github name and password.
```


Useful links:  
-----------------
Matplotlib - 2D and 3D plotting in Python:  
http://nbviewer.ipython.org/urls/raw.github.com/jrjohansson/scientific-python-lectures/master/Lecture-4-Matplotlib.ipynb  

R formula: (regression)  
http://nbviewer.ipython.org/urls/raw.github.com/fperez/nipy-notebooks/master/exploring_r_formula.ipynb  

