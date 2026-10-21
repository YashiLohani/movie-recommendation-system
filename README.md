# Movie Recommendation System 🎬

A content-based movie recommendation system built using Python, Pandas, and Scikit-learn. The project uses movie genres and user-generated tags from the MovieLens dataset to recommend movies with similar content.

## 📌 Project Overview

Finding movies that match our interests can be difficult when there are thousands of options available. This project explores how machine learning techniques can help recommend similar movies based on their content.

The system takes a movie title as input and suggests other movies with similar genres and tags.

## ✨ Features

- Loads movie information from CSV files.
- Combines movie genres and tags into a single description.
- Converts text descriptions into numerical representations using TF-IDF.
- Calculates similarity between movies using cosine similarity.
- Displays the top 5 recommended movies along with their similarity scores.
- Handles movie titles without regard to capitalization.

## 🛠️ Technologies Used

- **Python** — core programming language
- **Pandas** — data loading and manipulation
- **Scikit-learn** — TF-IDF vectorization and cosine similarity
- **MovieLens Dataset** — movie titles, genres, and tags

## ⚙️ How It Works

The recommendation system follows these steps:

1. **Load the dataset:** Read movie details and tags from CSV files using Pandas.
2. **Combine tags:** Group tags by `movieId` and combine them into a single string for each movie.
3. **Create descriptions:** Combine each movie's genres and tags into one text description.
4. **Apply TF-IDF:** Convert the descriptions into numerical vectors using `TfidfVectorizer`.
5. **Calculate similarity:** Use cosine similarity to compare the selected movie's vector with the vectors of other movies.
6. **Rank recommendations:** Sort movies by similarity score and display the top 5, excluding the selected movie itself.

## 📂 Project Structure

```text
movie-recommendation-system/
├── main.py
├── README.md
├── .gitignore
└── data/
    ├── movies.csv
    └── tags.csv
```

The `data/` directory contains the dataset files and is excluded from Git tracking. Download the dataset separately before running the project.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd movie-recommendation-system
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Install dependencies

```bash
python -m pip install pandas scikit-learn
```

### 3. Download the dataset

Download the **MovieLens Latest Small** dataset from:

https://grouplens.org/datasets/movielens/latest/

Extract the ZIP file and place `movies.csv` and `tags.csv` inside a folder named `data/` in the project root.

Your folder structure should look like this:

```text
movie-recommendation-system/
├── main.py
└── data/
    ├── movies.csv
    └── tags.csv
```

### 4. Run the project

```bash
python main.py
```

Enter a movie title when prompted. For example:

```text
Enter a movie title: Toy Story (1995)
```

The system will display the most similar movies and their similarity scores.

## 🧠 Concepts Learned

This project provides hands-on practice with:

- Reading and processing CSV files using Pandas
- Grouping data with `groupby()`
- Mapping values using `map()`
- Text preprocessing
- TF-IDF vectorization
- Sparse matrices
- Cosine similarity
- Sorting and ranking results
- Writing Python functions and handling user input
- Using Git and GitHub for version control

## 🔮 Future Improvements

- Add a graphical user interface or web application.
- Improve movie-title searching and handle duplicate titles.
- Incorporate movie ratings into recommendations.
- Explore collaborative filtering.
- Allow users to receive recommendations from partial title searches.

## 📊 Dataset

This project uses the MovieLens Latest Small dataset provided by GroupLens Research.

Dataset page: https://grouplens.org/datasets/movielens/latest/

## 👩‍💻 Author

Developed as a beginner-friendly project to explore Python, machine learning, and content-based recommendation systems.
