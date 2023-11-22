import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
def graficos_elbow_silhouette(X,random_state=42,intervalo_k=(2,11)):
    fig, axs = plt.subplots(ncols=2, figsize=(15, 5), tight_layout=True)

    elbow = {}
    silhouette = []
    k_range = range(*intervalo_k)


    for i in k_range:
        kmeans = KMeans(n_clusters=i, random_state=random_state, n_init=10)
        kmeans.fit(X)
        elbow[i] = kmeans.inertia_
        labels = kmeans.labels_
        silhouette.append(silhouette_score(X, labels))

    sns.lineplot(x=list(elbow.keys()), y=list(elbow.values()), ax=axs[0])
    axs[0].set_xlabel('K')
    axs[0].set_xlabel('Inertia')
    axs[0].set_title('Elbow Method')
    axs[0].plot([4,4],[350,200],'--r')
    sns.lineplot(x=list(k_range), y=silhouette, ax=axs[1])
    axs[1].set_xlabel('K')
    axs[1].set_xlabel('Silhouette Score')
    axs[1].set_title('Silhouette Method')
    axs[1].plot([5,5],[0.35,0.25],'--r')
    plt.show()

def visualizar_cluster(
    dataframe,
    colunas,
    quantidade_cores,
    centroids,
    mostrar_centroide=True, 
    mostrar_pontos=False,
    coluna_clusters=None,
):

    #Grafico em 3d
    #%matplotlib ipympl
    ax = plt.figure().add_subplot(projection='3d')
    #Deixar as cores dos demais pontos iguais as do centroide
    from matplotlib.colors import ListedColormap
    cores= plt.cm.tab10.colors[:quantidade_cores]
    cores=ListedColormap(cores)
    #Pontos do cluster
    x=dataframe[colunas[0]]
    y=dataframe[colunas[1]]
    z=dataframe[colunas[2]]
    #Escolher o que mostrar no grafico
    ligar_centroide = mostrar_centroide
    ligar_pontos= mostrar_pontos
    #Looping para ingressar os pontos no grafico
    for i, centroid in enumerate(centroids):
        #Decidir mostrar os pontos
        if ligar_centroide:
            #Pontos Centroide
            ax.scatter(*centroid,s=500,alpha=0.7)
            ax.text(*centroid, f"{i}",horizontalalignment='center', 
                    verticalalignment='center', fontsize=15)
        if ligar_pontos:
            s= ax.scatter(x,y,z,c=coluna_clusters, cmap=cores)
            ax.legend(*s.legend_elements(),bbox_to_anchor=(1.4,0.7))
    #legendas    
    ax.set_xlabel([colunas[0]])
    ax.set_ylabel([colunas[1]])
    ax.set_zlabel([colunas[2]])
    ax.set_title('Clusters')
    plt.show()