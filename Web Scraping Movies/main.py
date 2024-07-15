from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com"
                            "/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")
data = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_names = [movie.text for movie in data]
j = len(movie_names) - 1
movies = list()
for _ in range(len(movie_names)):
    movies.append(movie_names[j])
    j -= 1
with open(file="Movies.txt", mode='w') as file:
    for movie in movies:
        file.write(movie)
        file.write("\n")