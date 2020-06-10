import numpy as np 
from gensim.models import Doc2Vec
from gensim.models.doc2vec import LabeledSentence 
from gensim.models.doc2vec import TaggedDocument 
from gensim import utils 
from nltk.corpus import stopwords 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score
import re 
import string 
import pandas as pd 

#Preprocessing the data 
#Remove special characters, stopwords and get a comma separated data list of words for each article. 



def clean(text): 
	#using regular expression in python to remove special characters
	text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = text.lower().split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return (text)

def cleanup(text):
    text = textClean(text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text



def similarity(path):
#After text cleanup, use doc2vec to get similarities between 2 articles and saving them in an array with labels 
	labeled_titles=[]
	labeled_titles.append(TaggedDocument(title1_en[i].split(), path[path.index == i].tid1))
	labeled_titles.append(TaggedDocument(title2_en[i].split(), path[path.index == i].tid2))

	vecModel = Doc2Vec(dm = 1, min_count=1, window=10, size=150, sample=1e-4, negative=10)
	vecModel.build_vocab(labeled_titles)

	for epoch in range(5):
    	VecModel.train(labeled_questions,epochs=vecModel.iter,total_examples=vecModel.corpus_count)
    	print("Epoch #{} is complete.".format(epoch+1))


#Get cosine similarity for each article 

	score = vecModel.n_similarity(title1_en_split[i],title2_en_split[i])
	path['Similarity']=score