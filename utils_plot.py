import matplotlib.pyplot as plt
import numpy as np
import pandas as  pd
from mpl_toolkits import mplot3d

def get_3d_scatter(alpha_param, result_df):
    fig = plt.figure(111, figsize=(12,6))

    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('Number of Topics')
    ax.set_ylabel('Chunk Size')
    ax.set_zlabel('Number of Passes', labelpad=-1)

    for i in range(len(result_df)): 
        x = result_df.iloc[i]["Number of Topics"]
        y = result_df.iloc[i]["Chunk Size"]
        z = result_df.iloc[i]["Number of Passes"]

        coh_score = round(result_df.iloc[i]["Coherence Score"],3)
        coh_sqr = (5*coh_score) ** 8

        ax.scatter(x, y, z, s=coh_sqr)
        ax.text(x, y, z,  
                '%s' % (str(coh_score)), 
                size=16, 
                zorder=5000,  
                color='#0f167d') 
    
    ax.set_xticks([8,9,10,11,12])
    plt.title(f"Coherence Score (Alpha: {alpha_param})")

    plt.show()


def get_3d_scatter_cmap(alpha_param, result_df):
    x = result_df["Number of Topics"]
    y = result_df["Chunk Size"]
    z = result_df["Number of Passes"]
    c_score = result_df["Coherence Score"]
    coh_sqr = result_df["Coherence Score"].apply(lambda x:(5*x)**8)

    fig = plt.figure(figsize=(16,9))

    ax = fig.add_subplot(projection='3d')
    my_cmap = plt.get_cmap('viridis')

    sctt = ax.scatter3D(x, y, z,
                        s=coh_sqr,
                        alpha = 0.8,
                        c = c_score, 
                        cmap = my_cmap)
    fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
    
    

    for i in range(len(result_df)): 
        x = result_df.iloc[i]["Number of Topics"]
        y = result_df.iloc[i]["Chunk Size"]
        z = result_df.iloc[i]["Number of Passes"]

        coh_score = round(result_df.iloc[i]["Coherence Score"],3)

        ax.text(x, y, z,  
                '%s' % (str(coh_score)), 
                size=16, 
                zorder=5000,  
                color='#0f167d') 

    ax.set_xticks([8,9,10,11,12])

    plt.title(f"Coherence Score (Alpha: {alpha_param})", fontweight ='bold',size=18)

    ax.set_xlabel('Number of Topics', fontweight ='bold') 
    ax.set_ylabel('Chunk Size', fontweight ='bold') 
    ax.set_zlabel('Number of Passes', fontweight ='bold')


    plt.show()