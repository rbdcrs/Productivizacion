#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import wikipedia
import re
from stop_words import get_stop_words


# In[ ]:


stop_words = get_stop_words('es')
len(stop_words)


# In[ ]:


print(wikipedia.languages())
#fijamos el idioma a español
wikipedia.set_lang("es")


# In[ ]:


print(wikipedia.search("Python"))
print(wikipedia.search("Python", results = 3))
print(wikipedia.suggest("Madriz"))


# In[ ]:


# Que página queremos descargar
wiki = wikipedia.page('Python')


# In[ ]:


# Sacamos el texto de la página
text = wiki.content


# In[ ]:


# Sacamos el texto de la página
text = wiki.content


# In[ ]:


# Clean text
text = re.sub(r'==.*?==+', '', text) # eliminamos los headers
text = text.replace('\n', '') # eliminamos los saltos de línea


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# Creamos una función para generar el gráfico
def plot_cloud(wordcloud):
    # fijamos el tamaño
    plt.figure(figsize=(40, 30))
    # plot de la imagen
    plt.imshow(wordcloud)
    # sin ejes
    plt.axis("off");


# In[ ]:


# Importamos el paquete para hacer la nube de palabras
from wordcloud import WordCloud


# In[ ]:


# Genaramos la nube
wordcloud = WordCloud(width = 3000, height = 2000,
random_state=1,
background_color='white',colormap='viridis',
collocations=False, stopwords = stop_words +
["Python", "puede", "pueden"]).generate(text)
plot_cloud(wordcloud)


# In[ ]:


def crear_nube (x) :
    wikipedia.set_lang("es")
    wiki = wikipedia.page(x)
    text = wiki.content
    text = re.sub(r'==.*?==+', '', text) # eliminamos los headers
    text = text.replace('\n', '') # eliminamos los saltos de línea
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1,
    background_color='white',colormap='viridis',
    collocations=False, stopwords = stop_words + [x]).generate(text)
    nube = plot_cloud(wordcloud)
    return(nube)


# In[ ]:


crear_nube("getafe")


# In[ ]:


crear_nube("Toledo")

