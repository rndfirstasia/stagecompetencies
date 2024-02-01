# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd
import numpy  as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from io import StringIO

st.header('STAGE Competencies Checker App')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    t_data0 = pd.read_csv(uploaded_file, sep =';')
    t_data  = t_data0.iloc[: , 0:-1] 
    st.dataframe(t_data0, height = 200)

###

select_dimfac   = ['','S','S1','S2','S3','S4','T','T1','T2','T3','T4','T5','A','A1','A2','A3','A4',\
               'G','G1','G2','G3','G4','E','E1','E2','E3','E4','E5','E6']

select_level    = ['','--','-','=','+','++']

pick_container = st.container(height=400)
col1, col2 = pick_container.columns(2)

with col1:
    select_dimfac1 = st.selectbox('Dimensi / Facet 1', select_dimfac)
    select_dimfac2 = st.selectbox('Dimensi / Facet 2', select_dimfac)
    select_dimfac3 = st.selectbox('Dimensi / Facet 3', select_dimfac)
    select_dimfac4 = st.selectbox('Dimensi / Facet 4', select_dimfac)
    select_dimfac5 = st.selectbox('Dimensi / Facet 5', select_dimfac)
    select_dimfac6 = st.selectbox('Dimensi / Facet 6', select_dimfac)
    select_dimfac7 = st.selectbox('Dimensi / Facet 7', select_dimfac)
    select_dimfac8 = st.selectbox('Dimensi / Facet 8', select_dimfac)
    select_dimfac9 = st.selectbox('Dimensi / Facet 9', select_dimfac)
    select_dimfac10 = st.selectbox('Dimensi / Facet 10', select_dimfac)
    select_dimfac11 = st.selectbox('Dimensi / Facet 11', select_dimfac)
    select_dimfac12 = st.selectbox('Dimensi / Facet 12', select_dimfac)
    select_dimfac13 = st.selectbox('Dimensi / Facet 13', select_dimfac)
    select_dimfac14 = st.selectbox('Dimensi / Facet 14', select_dimfac)
    select_dimfac15 = st.selectbox('Dimensi / Facet 15', select_dimfac)
    select_dimfac16 = st.selectbox('Dimensi / Facet 16', select_dimfac)
    select_dimfac17 = st.selectbox('Dimensi / Facet 17', select_dimfac)
    select_dimfac18 = st.selectbox('Dimensi / Facet 18', select_dimfac)
    select_dimfac19 = st.selectbox('Dimensi / Facet 19', select_dimfac)
    select_dimfac20 = st.selectbox('Dimensi / Facet 20', select_dimfac)
    select_dimfac21 = st.selectbox('Dimensi / Facet 21', select_dimfac)
    select_dimfac22 = st.selectbox('Dimensi / Facet 22', select_dimfac)
    select_dimfac23 = st.selectbox('Dimensi / Facet 23', select_dimfac)
    select_dimfac24 = st.selectbox('Dimensi / Facet 24', select_dimfac)
    select_dimfac25 = st.selectbox('Dimensi / Facet 25', select_dimfac)
    select_dimfac26 = st.selectbox('Dimensi / Facet 26', select_dimfac)
    select_dimfac27 = st.selectbox('Dimensi / Facet 27', select_dimfac)
    select_dimfac28 = st.selectbox('Dimensi / Facet 28', select_dimfac)

with col2:
    select_level1 = st.selectbox('Level 1',select_level)
    select_level2 = st.selectbox('Level 2',select_level)
    select_level3 = st.selectbox('Level 3',select_level)
    select_level4 = st.selectbox('Level 4',select_level)
    select_level5 = st.selectbox('Level 5',select_level)
    select_level6 = st.selectbox('Level 6',select_level)
    select_level7 = st.selectbox('Level 7',select_level)
    select_level8 = st.selectbox('Level 8',select_level)
    select_level9 = st.selectbox('Level 9',select_level)
    select_level10 = st.selectbox('Level 10',select_level)
    select_level11 = st.selectbox('Level 11',select_level)
    select_level12 = st.selectbox('Level 12',select_level)
    select_level13 = st.selectbox('Level 13',select_level)
    select_level14 = st.selectbox('Level 14',select_level)
    select_level15 = st.selectbox('Level 15',select_level)
    select_level16 = st.selectbox('Level 16',select_level)
    select_level17 = st.selectbox('Level 17',select_level)
    select_level18 = st.selectbox('Level 18',select_level)
    select_level19 = st.selectbox('Level 19',select_level)
    select_level20 = st.selectbox('Level 20',select_level)
    select_level21 = st.selectbox('Level 21',select_level)
    select_level22 = st.selectbox('Level 22',select_level)
    select_level23 = st.selectbox('Level 23',select_level)
    select_level24 = st.selectbox('Level 24',select_level)
    select_level25 = st.selectbox('Level 25',select_level)
    select_level26 = st.selectbox('Level 26',select_level)
    select_level27 = st.selectbox('Level 27',select_level)
    select_level28 = st.selectbox('Level 28',select_level)

###

if st.button('Hitung dan Tampilkan'):
    
    dim_fac_pick      = []
    level_pick        = []
    dim_fac_pick_c    = []
    level_pick_c      = []

    dimfacvar = [select_dimfac1, select_dimfac2, select_dimfac3, select_dimfac4, select_dimfac5, select_dimfac6, select_dimfac7, select_dimfac8, select_dimfac9, select_dimfac10, select_dimfac11, select_dimfac12, select_dimfac13, select_dimfac14, select_dimfac15, select_dimfac16, select_dimfac17, select_dimfac18, select_dimfac19, select_dimfac20, select_dimfac21, select_dimfac22, select_dimfac23, select_dimfac24, select_dimfac25, select_dimfac26, select_dimfac27, select_dimfac28]
    levelvar  = [select_level1, select_level2, select_level3, select_level4, select_level5, select_level6, select_level7, select_level8, select_level9, select_level10, select_level11, select_level12, select_level13, select_level14, select_level15, select_level16, select_level17, select_level18, select_level19, select_level20, select_level21, select_level22, select_level23, select_level24, select_level25, select_level26, select_level27, select_level28]
    zipped1 = zip(dimfacvar,levelvar)
    for i,o in zipped1:
        dim_fac_pick.append(i)
        level_pick.append(o)

    zipped2 = zip(dim_fac_pick,level_pick)
    for i,o in zipped2:
        if i == '' or o == '':
            pass
        else:
            dim_fac_pick_c.append(i)
            level_pick_c.append(o)    

    padanan = pd.DataFrame(data={'dim_fac':dim_fac_pick_c,'level':level_pick_c})
    st.write('Berikut Padanan yang dipilih:')
    st.write(padanan)

    ## CALC ##
    #TScore to Cluster
    def t_to_cluster(score):
        if score < 34:
            return 'a'
        elif score > 33 and score < 45:
            return 'b'
        elif score > 44 and score < 56:
            return 'c'
        elif score > 55 and score < 66:
            return 'd'
        else:
            return 'e'
        
    #Final average competency score to STEN
    def score_to_sten(score,mean,std):
        sten    = ((((score-mean)/std))*2)+5.5
        return sten
    
    #STEN to Final Categories
    def sten_to_cat(score):
        if score < 3:
            return 'VL'
        elif score > 2 and score < 5:
            return 'L'
        elif score > 4 and score < 7:
            return 'M'
        elif score > 6 and score < 9:
            return 'H'
        else:
            return 'VH'

    #Cluster to Score Matrix
    dim_fac = ['S','S1','S2','S3','S4','T','T1','T2','T3','T4','T5','A','A1','A2','A3','A4',\
               'G','G1','G2','G3','G4','E','E1','E2','E3','E4','E5','E6']
    level   = ['--','-','=','+','++']
    cluster = ['a','b','c','d','e']

    dim_fac_spread  = []
    level_spread    = []
    cluster_spread  = []

    for a in dim_fac:
        for b in level:
            for c in cluster:
                dim_fac_spread.append(a)
                level_spread.append(b)
                cluster_spread.append(c)

    df                      = pd.DataFrame(data = {'cluster_core':[80,70,50,30,20,90,80,60,40,30,50,60,80,60,50,30,40,60,80,90,20,30,50,70,80]})
    cluster_score           = df.iloc[:,-1]
    cluster_score_spread    = []

    while len(cluster_score_spread) < 700:
        for o in cluster_score:
            cluster_score_spread.append(o)

    score_matrix = pd.DataFrame(data={"dimension_facet":dim_fac_spread,"level":level_spread,"cluster":cluster_spread,"score":cluster_score_spread})

    ## Padanan for Matching ##
    padanan         = [] #list with dataframe for matching
    forpadanan      = zip(dim_fac_pick_c,level_pick_c)

    for i,o in forpadanan:
        temp = score_matrix[score_matrix['dimension_facet'].isin([i]) & score_matrix['level'].isin([o])] #note isin()
        padanan.append(temp)
    
    ## Tscore data to Cluster data ##
    cluster_data = t_data.map(t_to_cluster)

    ## Cluster data clean ##
    cluster_data2 = cluster_data.loc[:,dim_fac_pick_c]

    ## Cluster to score ##
    col_num         = range(0,len(dim_fac_pick_c))
    zipped          = zip(col_num,dim_fac_pick_c)

    score_data      = pd.DataFrame()
    col_name_dim    = []

    for i,o in zipped:
        tempcol     = cluster_data2.iloc[:,[i]]
        tempdata    = padanan[i]
            
        tempscore   = pd.merge(left=tempcol,right=tempdata,left_on=o,right_on='cluster',how='left')
        tempscore   = tempscore.iloc[:,[-1]]

        score_data[o] = tempscore

        col_name_dim.append(o[0])

    ## Dimension Averages ##
    # Rename Columns
    rename_col_name     = dict(zip(dim_fac_pick_c,col_name_dim))
    score_data2         = score_data.rename(columns=rename_col_name) #renamed columns dataframe
    col_name_set        = set(col_name_dim)
    # Averages (score_data3)
    score_data3         = pd.DataFrame()
    for i in col_name_set:
        score_data3[i]  = score_data2.loc[:,[i]].apply(np.average,axis=1).apply(np.round)
    
    ## Final Data ##
    # Rename to avg_score
    average_score_data  = score_data3.apply(np.average,axis=1)
    final_data          = pd.DataFrame(data={'avg_score':average_score_data})
    #Convert and Add sten score column
    mean_avgscore       = final_data.apply(np.average,axis=0)
    mean_avgscore       = float(mean_avgscore.iloc[0])
    std_avgscore        = final_data.apply(np.std,axis=0)
    std_avgscore        = float(std_avgscore.iloc[0])
    final_data['sten']  = final_data.map(score_to_sten, mean = mean_avgscore, std = std_avgscore).map(int).map(math.floor)

    # Convert and Add categories column
    final_data['categories_old']  = t_data0.iloc[: , [-1]]
    final_data['categories_new']  = final_data.iloc[:,1].map(sten_to_cat)

    # show_data
    show_data = final_data.iloc[:,[2,3]]

    st.write('Berikut Hasil Perubahan Padanan:')
    st.write(show_data)

    #for data graph
    categories   = ['VL','L','M','H','VH']
    oldCat_count = []
    oldCat_info  = []
    newCat_count = []
    newCat_info  = []

    for i in categories:
        oldtemp    = sum(show_data.iloc[:,0] == i)
        oldCat_count.append(oldtemp)

        newtemp    = sum(show_data.iloc[:,1] == i)
        newCat_count.append(newtemp)
    
    while len(newCat_info) < len(categories):
        newCat_info.append('New')
        oldCat_info.append('Old')

    df0 = pd.DataFrame(data={'categories':categories,'count':oldCat_count,'info':oldCat_info})
    df1 = pd.DataFrame(data={'categories':categories,'count':newCat_count,'info':newCat_info})
    compiled_data = pd.concat([df0,df1])

    #figure
    fig = plt.figure()

    #graph
    sns.set_theme(style="whitegrid")
    sns.barplot (data=compiled_data, x="categories", y="count", hue="info", palette="Set1", alpha=.8).set(title="Distribusi Kategori Sebelum dan Sesudah Perubahan Padanan")

    #display graph
    st.write('Berikut Grafik Hasil Perubahan Padanan:')
    st.pyplot(fig)
