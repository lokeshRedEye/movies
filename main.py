import requests
from flask import Flask, request, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def home():
    tamilyogi_endpoint = "https://isaidub8.com/movie/tamil-dubbed-movies-download/"

    response = requests.get(url=tamilyogi_endpoint)
    response = response.text

    soup = BeautifulSoup(response, "html.parser")
    print(soup.title)

    list_of_movies = soup.select(".f > a")
    movies = []
    links = []
    for i in list_of_movies:
        movies.append(i.getText())
        links.append("https://isaidub8.com" + i['href'])
        print(i.getText())

    print(links)
    print(movies)

    movie_data = zip(movies, links)

    return render_template("index.html", movie_data=movie_data)


app.run(debug=True)