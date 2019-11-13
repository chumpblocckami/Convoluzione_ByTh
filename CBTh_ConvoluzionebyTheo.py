
# coding: utf-8

# <h1 style="text-align:center">Convoluzione di segnali monodimensionali e bidimensionali</h1>

# <img src="data:image/png;base64,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"></img>

# Con convoluzione si intende l'applicazione di un filtro a un segnale con la volontà di alterarlo. Si utilizza sia nei segnali monodimensionali (come i suoni) per togliere determinate frequenze, o nelle serie storiche con l'obbiettivo di eliminare i pattern di stagionalità. Nei segnali bidimensionali (immagini) lo si applica per diminuire il rumore o per uniformare aree confuse. In generale lo si applica quando si ha la necessità di normalizzare un segnale.

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import copy


# <h2>Convoluzione monodimensionale</h2>

# In[2]:


class CbThMono:
    def __init__(self,segnale,filtro):
        self.segnale = list(segnale)
        self.filtro = filtro
        
    def Convolvi(self,segnale,filtro,n):
        sums = []
        for i in range(0,len(self.filtro)):
            sums.append(segnale[i+n]*self.filtro[i])
        return sum(sums)
    def ZeroPadding(self,segnale):
        tmp = copy.deepcopy(self.segnale)
        tmp.insert(0,0)
        tmp.append(0)
        return tmp
    def Convoluzione(self):
        out = [] 
        n = len(self.segnale)
        tmp = self.ZeroPadding(self.segnale)
        for i in range(0,n):
            out.append(self.Convolvi(tmp,self.filtro,i))
        return out
    def Summary(self):
        str_out = "Segnale: "+str(self.segnale)+" \n Filtro: "+str(self.filtro)+" \n Trasformata: "+str(self.Convoluzione())
        return str_out
    def Grafico(self,annotate=True):
        sns.set()
        plt.figure(dpi=420)
        plt.title("Risultato filtro")
        plt.plot(self.segnale,label="Segnale",c="black")
        plt.plot(self.Convoluzione(),label="Convoluzione",c="violet")
        if (annotate):
            x = 0
            for i in self.segnale:
                plt.annotate(str(round(i,2)),xy=(x,i+0.1),size=5)
                x = x+1
            x = 0
            for i in self.Convoluzione():
                plt.annotate(str(round(i,2)),xy=(x,i+0.1),size=5,color="violet")
                x = x+1
        plt.legend(loc="lower left")
        plt.show()


# <p>Il segnale viene preso in maniera casuale: è possibile modificarlo</p>

# In[3]:


segnale = np.random.uniform(1,10,100)
sns.set()
plt.figure(dpi=420)
plt.plot(segnale)
plt.title("Segnale considerato")
plt.show()


# In[4]:


filtro = [-1,0,1]
CbThMono(segnale,filtro).Convoluzione()
CbThMono(segnale,filtro).Summary()
CbThMono(segnale,filtro).Grafico()


# <h3>Convoluzione di una serie temporale</h3>

# In[5]:


time = pd.read_csv("MTGTimeSeries.csv",parse_dates=['Datetime'])
filtro = [1/3,1/3,1/3]
print("Numero osservazioni: ",len(time))
time.head(10)


# In[6]:


CbThMono(time.N,filtro).Grafico(annotate=False)


# ### Convoluzione di un segnale monodimensionale: file wav

# In[7]:


import IPython.display as ipd
from scipy.io import wavfile as wav


# In[8]:


violin_r, violin = wav.read("C:/Users/Matteo Mazzola/ESERCITAZIONI DSIM/audio/violin.wav")
ipd.Audio(violin,rate=violin_r)


# In[9]:


filtro = [10,0,10]
ipd.Audio(CbThMono(violin,filtro).Convoluzione(),rate=violin_r)


# Nonostante la convoluzione non porti risultati apprezzabili all'orecchio, notiamo come abbia avuto effetto nella modifica del segnale

# In[10]:


filtro = [10,0,10]
CbThMono(violin[:1000],filtro).Grafico(annotate=False)


# <h2>Convoluzione di un segnale bidimensionale</h2>

# In[11]:


class CbThBi:
    def __init__(self,segnale,filtro):
        self.segnale = segnale
        self.filtro = filtro
        
    def Convolvi(self,segnale,filtro,y,x,lfilter,hfilter):
        sums = []
        #per ogni elemento della colonna del filtro
        for h in range(0,hfilter):
            #per ogni elemento della riga del filtro
            for l in range(0,lfilter):
                #prodotto del valore della matrice iesima con il valore del filtro della posizione jesima
                #y e x n on sono altro che i valori che permettono di spostarsi in avanti la matrice (il fitro non si muove)
                sums.append(segnale.item(h+y,l+x)*filtro.item(h,l))
        #print(sums)
        if ((sum(filtro)).sum() != 0): #controllo per il denominatore diverso da 0
            return (sum(sums))*(1/(sum(filtro)).sum()) #dividiamo per i valori del filtro per "standardizzare"
        else:
            return (sum(sums)) #se il denominatore è zero non possiamo dividere, quindi prendiamo il valore e basta
    
    def ZeroPadding(self):
            l = self.filtro.shape[0]
            h = self.filtro.shape[1]
            tmp = copy.deepcopy(self.segnale)
            tmp = np.pad(tmp,(l-2,h-2),"constant") #qua si aggiungono zeri pari alla grandezza del filtro -2 (3x3 = 1 zero, 4x4 = 2 zero)
            return tmp

    def Convoluzione(self):
        out = [] 
        #prendere il numero di colonne del filtro
        hfiltro = self.filtro.shape[0]
        #prendere il numero di righe del filtro
        lfiltro = self.filtro.shape[1]
        #prendere il numero di colonne della matrice
        hh = self.segnale.shape[0]
        #prendere il numero di righe della matrice
        ll = self.segnale.shape[1]
        #applichiamo zero padding (per un filtro 3x3 basta aggiungere 1 zero, per altri filtri bisogna considerare + zeri)
        tmp = self.ZeroPadding()
        #per ogni elemento di ogni colonna della matrice
        for h in range(0,hh):
            #per ogni elemento di ogni riga della matrice
            for l in range(0,ll):
                #si applica la convoluzione utilizzando il filtro e gli elementi coincidenti della matrice
                #si passa la matrice sotto zeropadding, il valore di colonna, il valore di riga, e le grandezze del filtro
                out.append(self.Convolvi(tmp,self.filtro,h,l,hfiltro,lfiltro))
        #ritorna la matrice di grandezza uguale alla prima
        return np.asmatrix(out).reshape(hh,ll)

    def Grafico(self):
        #sns.set(style="darkgrid")
        plt.figure(dpi=420)
        plt.subplot(2,2,1)
        sns.heatmap(self.segnale)
        plt.subplot(2,2,2)
        sns.heatmap(self.Convoluzione())
        plt.show()
    
    def Image(self): #non funzina imshow in ambiente diverso da dism
        plt.figure(dpi=420)
        confronto = np.concatenate((self.segnale,self.Convoluzione()), axis = 1)
        plt.imshow(confronto,cmap='gray')
        
    def Summary(self):
        print("Segnale:\n",self.segnale,"\nFiltro:\n",filtro, "\nConvoluzione:\n",self.Convoluzione())


# ### Convoluzone segnale bidimensionale 

# <p>Definiamo una funzione che ci permette di creare una matrice randomica. Utilizziamo una matrice plottandola come una heatmap, dove ogni valore del campo della matrice è considerato un pixel <br> Come filtro utilizzeremo una matrice 3x3 average</p>

# In[12]:


def randomMatrix(columns,row,lmin=0,lmax=2):
    matrix = []
    for i in range(0,columns):
        matrix.append(np.random.randint(lmin,lmax,row))
    return np.matrix(matrix)


# Creiamo una matrice con valori casuali. Ogni valore della matrice identifica un pixel. 

# In[13]:


base = randomMatrix(50,50,0,100)
plt.title("Immagine di partenza")
sns.heatmap(base)
plt.show()


# Definiamo il filtro 3x3 da utilizzare. In base al filtro utilizzato cambierà l'applicazione che andremo ad effettuare sull'immagine (blurring/sharpening)

# In[14]:


def chooseFilter(nomeFiltro,annotate=False): 
        if(str.lower(nomeFiltro)=="prewitt-dx"):
            filtro = np.asmatrix(np.array([[0,1,1],[-1,0,1],[-1,-1,0]]))
            if (annotate):
                plt.title("Filtro utilizzato")
                sns.heatmap(filtro,annot=True)
                plt.show()
            return filtro
        elif(str.lower(nomeFiltro)=="prewitt-sx"):
            filtro = np.asmatrix(np.array([[-1,-1,0],[-1,0,1],[0,1,1]]))
            if(annotate):
                plt.title("Filtro utilizzato")
                sns.heatmap(filtro,annot=True)
                plt.show()
            return filtro
        elif(str.lower(nomeFiltro)=="sobel-dx"):
            filtro = np.asmatrix(np.array([[0,1,2],[-1,0,1],[-2,-1,0]]))
            if (annotate):
                plt.title("Filtro utilizzato")
                sns.heatmap(filtro,annot=True)
                plt.show()
            return filtro
        elif(str.lower(nomeFiltro) == "sobel-sx"):
            filtro = np.asmatrix(np.array([[-2,-1,0],[-1,0,1],[0,1,2]]))
            if (annotate):
                plt.title("Filtro utilizzato")
                sns.heatmap(filtro,annot=True)
                plt.show()
            return filtro
        elif(str.lower(nomeFiltro) == "average"):
            filtro = np.asmatrix(np.array([[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3]]))
            if(annotate):
                plt.title("Filtro utilizzato")
                sns.heatmap(filtro,annot=True)
                plt.show()
            return filtro
        else:
            #se nessun filtro è stato chiamato, ritorna un filtro a caso 3x3
            filtro = randomMatrix(0,10,0,2)
            if(annotate):
                plt.title("Filtro utilizzato")
                sns.heatmap(filtro,annot=True)
                plt.show()
            return filtro


# In[15]:


filtro = chooseFilter("sobel-sx",annotate=True)


# Applichiamo i vari tipi di convoluzione sulla matrice

# In[16]:


CbThBi(base,chooseFilter("sobel-sx",annotate=False)).Grafico()


# In[17]:


CbThBi(base,chooseFilter("sobel-dx",annotate=False)).Grafico()


# In[18]:


CbThBi(base,chooseFilter("prewitt-sx",annotate=False)).Grafico()


# In[19]:


CbThBi(base,chooseFilter("prewitt-dx",annotate=False)).Grafico()


# In[20]:


CbThBi(base,chooseFilter("average",annotate=False)).Grafico()


# Notiamo come il rumore della matrice è stato 'appiattito' in base al valore dei pixel vicini (quindi vi sono meno punti scuri (valori alti) e punti chiari (valori bassi)). Utilizzando diversi filtri si hanno risultati diversi.

# ### Convoluzione segnale bidimensionale: file png

# In[21]:


from skimage import io
from skimage import filters
import ipywidgets as widgets
import copy
im = io.imread("C:/Users/Matteo Mazzola/Desktop/Picture/Ho-Oh_Debut.png",as_gray=True) 
plt.imshow(im, cmap='gray');plt.show()


# In[26]:


CbThBi(np.asmatrix(im),chooseFilter("average",annotate=False)).Image()


# In[27]:


CbThBi(np.asmatrix(im),chooseFilter("prewitt-dx",annotate=False)).Grafico()


# In[28]:


CbThBi(np.asmatrix(im),chooseFilter("prewitt-sx",annotate=False)).Grafico()


# Utilizzando la convoluzione si osserva come i dettagli vengono per lo piu' evidenziati in base alla manovra del filtro (utilizzando un prewitt-sx si notano piu' i dettagli tendenti verso sinistra, mentre al contrario con un filtro prewitt-dx si osservano i dettagli sulla destra, si noti la ala sulla metà dell'immagine). Con una convoluzione di tipo 'average' invece l'immagine si sfuoca.
