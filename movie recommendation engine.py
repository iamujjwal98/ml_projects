#import the libraries
import pandas as pd

#reading the dataset
df=pd.read_csv('movie_dataset.csv')

#taking the features matrix
features=['genres','keywords','cast','director']

#removing the exceptions by fillig the NaN with empty string
for feature in features:
  df[feature]=df[feature].fillna('')



#helper functions
def get_title_from_index(index):
  return df[df.index==index]['title'].values[0]

def get_index_from_title(title):
  return df[df.title==title]['index'].values[0]
   

#segregating the features matrix from entire data set
def combined_features(row):
  try:
    return row['genres']+" "+row['keywords']+" "+row['cast']+" "+row['director']
  except:
    print(row)
#df=df.apply(everythingtolowercase,axis=1)
df["combined_features"]=df.apply(combined_features,axis=1)



#since features matrix is ready now apply to find the similairty between each
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
Count_matrix=cv.fit_transform(df["combined_features"]).toarray()

#calculate the similairty btw the movies
from sklearn.metrics.pairwise import cosine_similarity
cosine_sim=cosine_similarity(Count_matrix)

#take the input from the user about his choice of movie
movie_user_likes=input("tell me a name of the movie i will suggest you a list of recommendations")
index=get_index_from_title(movie_user_likes)
print(index)
#enumerate,sort the movies of required index in order of decending oredre of similarity
similar_movies=list(enumerate(cosine_sim[index]))
sorted_sim_movies=sorted(similar_movies,key=lambda x:x[1], reverse=True)

i=0
for movies in sorted_sim_movies:
  print(get_title_from_index(movies[0]))
  print(movies[1])
  i+=1
  if i>10:
    break