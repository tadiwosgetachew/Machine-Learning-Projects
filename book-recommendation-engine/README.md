# K-Nearest Neighbors Book Recommendation Engine

This project implements a book recommendation system using the K-Nearest Neighbors (KNN) algorithm. The goal is to recommend books based on similarity from a given book using the Book-Crossings dataset, which contains over 1.1 million ratings for 270,000 books by 90,000 users.

## Overview

In this project, we:

- Load and clean the Book-Crossings dataset.
- Use the K-Nearest Neighbors algorithm from `sklearn.neighbors` to create a recommendation system.
- Implement a function `get_recommends` that returns a list of 5 books similar to a given book title, along with their similarity scores (distances).

The `get_recommends` function takes a book title as an argument and returns the 5 most similar books, sorted by their proximity.

## Example Usage

```python
get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))")
```

This would output a list of similar books with their similarity scores:
```bash
[
  'The Queen of the Damned (Vampire Chronicles (Paperback))',
  [
    ['Catch 22', 0.793983519077301],
    ['The Witching Hour (Lives of the Mayfair Witches)', 0.7448656558990479],
    ['Interview with the Vampire', 0.7345068454742432],
    ['The Tale of the Body Thief (Vampire Chronicles (Paperback))', 0.5376338362693787],
    ['The Vampire Lestat (Vampire Chronicles, Book II)', 0.5178412199020386]
  ]
]
```

## Requirements

- Python 3.x
- scikit-learn
- pandas
- numpy
- joblib
- scipy

You can install the necessary dependencies by running:
```bash
pip install -r requirements.txt
```

## How It Works

### Data Preprocessing:
The dataset is loaded, cleaned, and transformed into a format suitable for recommendation using KNN.

### KNN Model:
The `NearestNeighbors` class from `sklearn.neighbors` is used to create a KNN model. The model identifies the nearest neighbors (most similar books) based on user ratings.

### Recommendation Function:
The function `get_recommends()` is designed to take a book title as input and return the top 5 most similar books based on the KNN model's distances.

### Dataset

The dataset used in this project is the Book-Crossings dataset, provided by freeCodeCamp. You can obtain the dataset by running the following commands:

```bash
!wget https://cdn.freecodecamp.org/project-data/books/book-crossings.zip
!unzip book-crossings.zip
```
This will extract the following files:

- `BX-Books.csv`: Contains information about books (e.g., titles, authors).
- `BX-Book-Ratings.csv`: Contains ratings for each book from different users.
- `BX-Users.csv`: Contains information about the users who provided the ratings.


## Contributing

Feel free to fork the repo, make your changes, and submit a pull request. For bug reports or feature suggestions, please open an issue.


## Acknowledgments

- scikit-learn for the KNN implementation.
- The Book-Crossings dataset for providing a rich resource for building the recommendation engine.


