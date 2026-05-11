import gensim.downloader
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn import manifold

#inizializzazioni
parola="non esiste"
model=None
vects=[]
plt.style.use('_mpl-gallery')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def hexcas():
    color="#"    
    for i in range(0, 6):
        color=color+str(np.random.randint(3, 9))
    return color



#ax.set_xlim(0, 100)
#ax.set_ylim(0, 100)
#ax.set_zlim(-100, 100)
xpoints = np.array([0])
ypoints = np.array([0])
zpoints = np.array([0])
parole=[]

#caricamento modello
print("caricamento modello")
model=gensim.downloader.load("glove-wiki-gigaword-100")

print("modello caricato")


while(True):
    while(parola):
        parola=input("parola da cercare: ")
        if parola=="" or parola==' ' or parola=="x" :
            break
        else:
            parola=parola.strip()
            parole.append(parola)
            vett_parola=model[parola] #returns array
            vects.append(vett_parola)

    vettori=np.array(vects)

    # 100D-> 2D
    tsne = TSNE(n_components=3, random_state=42, perplexity=min(5, len(vects) - 1))
    vectors_3d = tsne.fit_transform(vettori)
    origin = np.array([0, 0, 0])
    print(vettori)
    plt.plot(origin[0], origin[1], origin[2])

    global i
    i = 0
    for vettore in vectors_3d:
        print("coordinate vettore !", vettore)
        """  xpoints = np.append(xpoints, vettore[0])
        np.append(xpoints,0)
        ypoints = np.append(ypoints, vettore[1])
        np.append(ypoints,0)
        zpoints = np.append(zpoints, vettore[2])
        np.append(zpoints,0)"""
        color=hexcas()
        plt.plot(
            [0,vettore[0]],
            [0,vettore[1]], 
            [0,vettore[2]],
            label=parole[i] ,color=color ,marker='^', markersize=10, markerfacecolor=color)
        i += 1
   

    
    plt.legend()
    plt.show()