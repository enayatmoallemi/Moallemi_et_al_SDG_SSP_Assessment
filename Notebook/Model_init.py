
# coding: utf-8

# In[1]:


import sys
sys.path.append(r'C:\Users\moallemie\EMAworkbench-master')


# In[2]:


from ema_workbench.connectors.vensim import VensimModel
directory = 'C:/Users/moallemie/GitHub/SSPs_SDGs_Assessment/Model/'
vensimModel = VensimModel("FelixSDGsModel", wd=directory, model_file=r'FeliX3_SDGs_v45.vpmx')
