# Movie data: Movie name as key, a dictionary with 'min_age' and 'available_seats' as values
movies = {
    "Movie 1": {"min_age": 18, "available_seats": 10},
    "Movie 2": {"min_age": 15, "available_seats": 5},
    "Movie 3": {"min_age": 12, "available_seats": 0},
    "Movie 4": {"min_age": 10, "available_seats": 20}
}

#display the movies available with the seats
def display_movies():
    print("Available movies:")
    for movie in movies:
        print(f"- {movie} (Min Age: {movies[movie]['min_age']}, 
              Available Seats: {movies[movie]['available_seats']})")

def book_movie():
    display_movies()
    selected_movie = input("Enter the name of the movie you want to watch: ")
    
    if selected_movie not in movies:
        print("Sorry, that movie is not available.")
        return
    
    