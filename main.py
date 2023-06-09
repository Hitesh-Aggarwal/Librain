import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

recom_books = []
# Load the dataset
books_df = pd.read_csv("data.csv")

# Create a TF-IDF vectorizer to convert the summaries into a numerical representation
tfidf = TfidfVectorizer(stop_words="english")
books_df["summary"] = books_df["summaries"].fillna("")
tfidf_matrix = tfidf.fit_transform(books_df["summary"])

# Calculate the cosine similarity between each book
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


# Define a function to recommend similar books based on a given book
def recommend_books(book_title, n, cosine_sim=cosine_sim, books_df=books_df):
    try:
        # Get the index of the book that matches the title
        idx = books_df[books_df["title"] == book_title].index[0]

        # Get the similarity scores between the book and all the others
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the books based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the top n most similar books
        sim_scores = sim_scores[1 : n + 1]

        # Get the indices of the similar books
        book_indices = [i[0] for i in sim_scores]

        # Return the top 10 similar books
        return books_df["title"].iloc[book_indices]
    except IndexError as e:
        print("Error:", e)
        return []


# Recommend books similar to any book required
def predicted_books(book_name, n):
    recom_books = []
    recomm_books = recommend_books(book_name, n)
    for i in recomm_books:
        recom_books = recom_books + [i]
    return recom_books


def main():
    book_name = sys.argv[1]
    n = int(sys.argv[2])

    try:
        idx = books_df[books_df["title"] == book_name].index[0]
    except IndexError:
        print("Book not available in library.")
        exit()

    ans = predicted_books(book_name, n)
    while ans:
        print(ans.pop())


if __name__ == "__main__":
    main()
