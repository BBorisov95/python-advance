def movie_organizer(*args):
    library = {}
    for movie, gen in args:
        if gen not in library:
            library[gen] = []
        library[gen].append(movie)
    library = sorted(library.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''

    for collection in library:
        result += f'{collection[0]} - {len(collection[1])}\n'
        movies = sorted(collection[1], key=lambda k: k)
        for movie in movies:
            result += f'* {movie}\n'

    return result




print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))