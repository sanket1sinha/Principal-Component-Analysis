
# coding: utf-8

# In[4]:

import numpy as np
import scipy
import sklearn.metrics.pairwise
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from scipy.spatial.distance import cdist

fp = open('...input.in','r')

dimensions=int(fp.readline())
number_patients=int(fp.readline())
distance_metric=int(fp.readline())
x=int(fp.readline())
patients_matrix=list(fp.readlines())
patients_matrix= [x.split() for x in patients_matrix]
patient=patients_matrix[0]
patients_matrix=patients_matrix[1:]
l=[]

#Dimensionality Reduction
if(x!=-1):
  
  new_matrix= np.vstack([patient, patients_matrix])
  pca = PCA(n_components=x)
  reduced_data = pca.fit_transform(new_matrix)
  patient=reduced_data[0]
  patients_matrix=reduced_data[1:]
  explained_variance=pca.explained_variance_
  ratio=pca.explained_variance_ratio_
  cumulative_variance=explained_variance.sum()
  cumulative_ratio=ratio.sum()
  #print(reduced_data)
  #print(patient_reduced)
  #print(patient_matrix_reduced)
  
##For euclidean distance
if(distance_metric==2):
    for i in range(number_patients):
        ed=euclidean_distances([patient],[patients_matrix[i]])
        ed=ed.tolist()
        l.append(ed)
    list_new = [j for i in l for j in i]
    final_list = [j for i in list_new for j in i]
    final_list=sorted(range(len(final_list)),key=lambda x:final_list[x])
    final_list=final_list[0:5]
    for i in range(5):
        print(final_list[i]+1)
    if(x!=-1):
      print(cumulative_ratio)
      

##For Manhattan distance        
elif(distance_metric==1):
    for i in range(number_patients):
        md=manhattan_distances([patient],[patients_matrix[i]])
        md=md.tolist()
        l.append(md)
    list_new = [j for i in l for j in i]
    final_list = [j for i in list_new for j in i]
    final_list=sorted(range(len(final_list)),key=lambda x:final_list[x])
    final_list=final_list[0:5]
    for i in range(5):
        print(final_list[i]+1)
    if(x!=-1):
      print(cumulative_ratio)
      

##For Cosine similarity
elif(distance_metric==4):
    for i in range(number_patients):
        cs=cosine_similarity([patient],[patients_matrix[i]])
        cs=cs.tolist()
        l.append(cs)
    list_new = [j for i in l for j in i]
    final_list = [j for i in list_new for j in i]
    final_list = list(map(lambda x: 1-x, final_list))
    final_list=sorted(range(len(final_list)),key=lambda x:final_list[x])
    final_list=final_list[0:5]
    for i in range(5):
        print(final_list[i]+1)
    if(x!=-1):
      print(cumulative_ratio)
      

##For Supremum distance
elif(distance_metric==3):
    for i in range(number_patients):
        y = cdist([patient], patients_matrix, 'chebyshev')
    final_list=y.tolist()
    final_list = [j for i in final_list for j in i]
    final_list=sorted(range(len(final_list)),key=lambda x:final_list[x])
    final_list=final_list[0:5]
    for i in range(5):
        print(final_list[i]+1)
    if(x!=-1):
      print(cumulative_ratio)
    


# In[ ]:




# In[ ]:



