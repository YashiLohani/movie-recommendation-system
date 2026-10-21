
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# STEP 1: Load the CSV files
movies_df = pd.read_csv("data/movies.csv")
tags_df = pd.read_csv("data/tags.csv")

print("Movies loaded:", len(movies_df))


# STEP 2: Combine all tags belonging to each movie
tags_by_movie = (
    tags_df.groupby("movieId")["tag"]
    .apply(lambda tags: " ".join(tags.astype(str)))
    .to_dict()
)

# Attach the tags to the corresponding movie
movies_df["tags"] = (
    movies_df["movieId"].map(tags_by_movie).fillna("")
)


# STEP 3: Combine genres and tags into one description
movies_df["genres"] = movies_df["genres"].fillna("").str.replace(
    "|", " ", regex=False
)

movies_df["description"] = (
    movies_df["genres"] + " " + movies_df["tags"]
)


# STEP 4: Convert descriptions into TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")

tfidf_matrix = vectorizer.fit_transform(
    movies_df["description"]
)

print("TF-IDF matrix shape:", tfidf_matrix.shape)


# STEP 5: Recommend similar movies
def recommend(movie_title, number=5):

    # Find the selected movie
    matches = movies_df[
        movies_df["title"].str.casefold()
        == movie_title.strip().casefold()
    ]

    if matches.empty:
        print("Movie not found:", movie_title)
        print("Tip: Enter the full movie title, including its year if shown.")
        return

    movie_index = matches.index[0]

    # Calculate similarity with every movie for this selection
    scores = cosine_similarity(
        tfidf_matrix[movie_index],
        tfidf_matrix
    )[0]

    # Pair each movie index with its score
    ranked_movies = list(enumerate(scores))

    # Sort from highest similarity to lowest
    ranked_movies.sort(
        key=lambda item: item[1],
        reverse=True
    )

    print("\nRecommendations for:", movies_df.loc[movie_index, "title"])
    print("-" * 45)

    count = 0

    for index, score in ranked_movies:

        # Do not recommend the selected movie itself
        if index == movie_index:
            continue

        title = movies_df.iloc[index]["title"]
        percentage = round(float(score) * 100, 2)

        print(f"{title} — {percentage}% similarity")

        count += 1

        if count == number:
            break


# STEP 6: Ask the user for a movie
if __name__ == "__main__":
    movie_title = input("Enter a movie title: ")
    recommend(movie_title)
