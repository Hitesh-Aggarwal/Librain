import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer


books = pd.read_csv('DataSet.csv')

summaries = np.array(books.Summaries)

model = SentenceTransformer('distilbert-base-nli-mean-tokens')

embedding = model.encode(summaries, show_progress_bar= True)