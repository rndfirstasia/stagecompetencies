import pandas as pd
import numpy  as np
import math
import seaborn as sns

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

### -- Def Funcs --

dim_fac_pick    = []
level_pick      = []

def browseFiles():
    global path
    path = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                     filetypes = (("CSV files","*.csv"),("all files","*.*")))
    
    path_label.configure(text=path)

def add_crit():
    dim_fac_pick.clear()
    level_pick.clear()

    dim_fac_lst = [dropdown_dim_fac1.get(),dropdown_dim_fac2.get(),dropdown_dim_fac3.get(),dropdown_dim_fac4.get(),dropdown_dim_fac5.get(),dropdown_dim_fac6.get(),dropdown_dim_fac7.get(),dropdown_dim_fac8.get(),dropdown_dim_fac9.get(),dropdown_dim_fac10.get(),dropdown_dim_fac11.get(),dropdown_dim_fac12.get(),dropdown_dim_fac13.get(),dropdown_dim_fac14.get(),dropdown_dim_fac15.get(),dropdown_dim_fac16.get(),dropdown_dim_fac17.get(),dropdown_dim_fac18.get(),dropdown_dim_fac19.get(),dropdown_dim_fac20.get(),dropdown_dim_fac21.get(),dropdown_dim_fac22.get(),dropdown_dim_fac23.get(),dropdown_dim_fac24.get(),dropdown_dim_fac25.get(),dropdown_dim_fac26.get(),dropdown_dim_fac27.get(),dropdown_dim_fac28.get()]
    dim_fac_lst = pd.DataFrame(data=dim_fac_lst).dropna()
    len_dim     = range(0,len(dim_fac_lst))

    level_lst   = [dropdown_lvl1.get(),dropdown_lvl2.get(),dropdown_lvl3.get(),dropdown_lvl4.get(),dropdown_lvl5.get(),dropdown_lvl6.get(),dropdown_lvl7.get(),dropdown_lvl8.get(),dropdown_lvl9.get(),dropdown_lvl10.get(),dropdown_lvl11.get(),dropdown_lvl12.get(),dropdown_lvl13.get(),dropdown_lvl14.get(),dropdown_lvl15.get(),dropdown_lvl16.get(),dropdown_lvl17.get(),dropdown_lvl18.get(),dropdown_lvl19.get(),dropdown_lvl20.get(),dropdown_lvl21.get(),dropdown_lvl22.get(),dropdown_lvl23.get(),dropdown_lvl24.get(),dropdown_lvl25.get(),dropdown_lvl26.get(),dropdown_lvl27.get(),dropdown_lvl28.get()]
    level_lst   = pd.DataFrame(data=level_lst).dropna()
    len_lvl     = range(0,len(level_lst))

    for i in len_dim:
        if dim_fac_lst.iloc[i,0]=='':
            pass
        else:
            dim_fac_pick.append(dim_fac_lst.iloc[i,0])

    for i in len_lvl:
        if level_lst.iloc[i,0]=='':
            pass
        else:
            level_pick.append(level_lst.iloc[i,0])

def stage_comp_check():
    ## Input DataFrame ##
    path_val = path.replace('/','\\')
    t_data0 = pd.read_csv(path_val,sep = ";")
    t_data = t_data0.iloc[: , 0:-1]

    ## Def Functions & Score Matrix ##
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
    forpadanan      = zip(dim_fac_pick,level_pick)

    for i,o in forpadanan:
        temp = score_matrix[score_matrix['dimension_facet'].isin([i]) & score_matrix['level'].isin([o])] #note isin()
        padanan.append(temp)
    
    ## Tscore data to Cluster data ##
    cluster_data = t_data.map(t_to_cluster)

    ## Cluster data clean ##
    cluster_data2 = cluster_data.loc[:,dim_fac_pick]

    ## Cluster to score ##
    col_num         = range(0,len(dim_fac_pick))
    zipped          = zip(col_num,dim_fac_pick)

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
    rename_col_name     = dict(zip(dim_fac_pick,col_name_dim))
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
    final_data['categories']  = final_data.iloc[:,1].map(sten_to_cat)

    ### for graph
    global old_data,new_data
    old_data        = t_data0.iloc[:,[-1]]
    new_data        = final_data.iloc[:,[-1]]

    oldCat         = ['VL','L','M','H','VH']
    oldCat_count   = []
    oldCat_info    = []

    newCat         = ['VL','L','M','H','VH']
    newCat_count   = []
    newCat_info    = []

    for i in newCat:
        oldtemp    = sum(old_data.iloc[:,0] == i)
        oldCat_count.append(oldtemp)

        newtemp    = sum(new_data['categories'] == i)
        newCat_count.append(newtemp)

    while len(newCat_info) < len(newCat):
        newCat_info.append('New')
        oldCat_info.append('Old')

    df0 = pd.DataFrame(data={'categories':oldCat,'count':oldCat_count,'info':oldCat_info})
    df1 = pd.DataFrame(data={'categories':newCat,'count':newCat_count,'info':newCat_info})

    global compiled_data
    compiled_data = pd.concat([df0,df1])

    print(compiled_data)

    ### create frame and pack for graph
    grpfrm = tk.Frame(main_window)
    grpfrm.place(x=710,y=110)
    
    fig = create_graph() #nyambung sama function create_graph()

    canvas = FigureCanvasTkAgg(fig,master=grpfrm)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def create_graph():
    sns.set_theme(style="whitegrid")

    figure, ax  = plt.subplots(figsize=(5,5))

    sns.barplot (
    data=compiled_data,
    x="categories", y="count", hue="info",
    palette="Set1", alpha=.8, ax=ax).set(title="Distribusi Kategori Sebelum dan Sesudah Perubahan Padanan")

    return figure

def saveFile():
    path_ex     = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("csv files", "*.csv"),("All Files", "*.*") ))

    df = pd.DataFrame()
    df['old_data']    = old_data.iloc[:,0]
    df['new_data']    = new_data.iloc[:,0]

    path_ex_conv = path_ex.replace('/','\\')
    df.to_csv(path_ex_conv,index=False)

    export_label.configure(text='Save data (.csv): File Saved')

def _quit():
    main_window.quit()
    main_window.destroy() 

### -- App Interface --
    
main_window = tk.Tk()
main_window.protocol("WM_DELETE_WINDOW", _quit)
main_window.title('STAGE Competencies Checker')
main_window.geometry('1450x900+50+50')  

title               = ttk.Label(main_window,text='STAGE Competencies Checker',
                               font=('Roboto',18)).place(x=10,y=10)

fileSelect_label    = ttk.Label(main_window,text='Silakan pilih file anda (.csv)',
                                font=('Roboto',12),anchor=tk.W,foreground='white',
                                background='blue').place(x=10,y=70)

select_label        = ttk.Label(main_window,text='Current File: ',
                                font=('Roboto',9),anchor=tk.W,foreground='white',background='black')

select_label.place(x=110,y=110)

path_label          = ttk.Label(main_window,text='',font=('Roboto',9),anchor=tk.W,foreground='white',background='black',width=60)
path_label.place(x=110,y=140)

add_file_button     = tk.Button(main_window,text='Pilih file',command=browseFiles).place(x=10,y=110)

###

col1=ttk.Label(main_window,text='Index',font=('Roboto',14),anchor=tk.W).place(x=25,y=180)
col2=ttk.Label(main_window,text='Dimensi',font=('Roboto',14),anchor=tk.W).place(x=180,y=180)
col3=ttk.Label(main_window,text='Level',font=('Roboto',14),anchor=tk.W).place(x=390,y=180)

### -- scrollable frame
frm = ctk.CTkScrollableFrame(main_window,width=450,height=380)
frm.place(x=10,y=180)

### -- Kompetensi & Level Label
grid_index = range(0,28)
label_add  = range(1,29)

zipped     = zip(grid_index,label_add)

for i,o in zipped:
    ctk.CTkLabel(frm,text='Kompetensi & Level '+str(o) ,font=('Roboto',12),
                 anchor='w').grid(row = i,column = 0, pady=6)

### ### -- dropdown dim_fac
dropdown_content  = ['','S','S1','S2','S3','S4',
                        'T','T1','T2','T3','T4','T5',
                        'A','A1','A2','A3','A4',
                        'G','G1','G2','G3','G4',
                        'E','E1','E2','E3','E4','E5','E6']
selected_name = []
dropdown_name = []
num_dropdown  = range(1,29)
row_num       = range(0,28)
for i in num_dropdown:
    selected_name.append('selected_dimfac'+str(i))
    dropdown_name.append('dropdown_dim_fac'+str(i))

zipped = zip(selected_name,dropdown_name,row_num)
for i,o,p in zipped:
    globals()[i] = tk.StringVar()

    globals()[o] = ttk.Combobox(frm, textvariable = globals()[i],
                                values=dropdown_content,state='readonly')
    
    globals()[o].grid(row=p,column=1,padx=8)

### ### -- dropdown lvl
dropdown_content1 = ['','--','-','=','+','++']
selected_name1 = []
dropdown_name1 = []
for i in num_dropdown:
    selected_name1.append('selected_lvl'+str(i))
    dropdown_name1.append('dropdown_lvl'+str(i))

zipped1        = zip(selected_name1,dropdown_name1,row_num)
for a,b,c in zipped1:
    globals()[a] = tk.StringVar()
    globals()[b] = ttk.Combobox(frm, textvariable = globals()[a],
                                values=dropdown_content1,state='readonly')
    globals()[b].grid(row=c,column=2,padx=8)

###

add_crit_button = tk.Button(main_window,text='Tambah Padanan',
                            command=add_crit).place(x=10,y=730)

calc_button     = tk.Button(main_window,text='Hitung dan Tampilkan',
                            command=stage_comp_check).place(x=150,y=730)

###

export_label        = ttk.Label(main_window,text='Save data (.csv):',font=('Roboto',12),anchor=tk.W,foreground='white',background='blue')
export_label.place(x=10,y=800)
path_ex_button      = tk.Button(main_window,text='Pilih file',command=saveFile).place(x=10,y=840)

###

graphout_label    = ttk.Label(main_window,text='Grafik perbandingan:',font=('Roboto',12),anchor=tk.W,foreground='white',background='blue').place(x=710,y=70)

###

main_window.mainloop()