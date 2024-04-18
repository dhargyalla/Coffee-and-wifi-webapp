import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_content = response.text

movie_tag = BeautifulSoup(web_content, "html.parser")
title_tag = movie_tag.find_all("h3", class_="title")
movie_name = []
movie_rank = []

for item in title_tag:
    text = item.getText()
    if ')' in text:
        movie_title = text.split(')')
        movie_name.append(movie_title[1].strip())
        movie_rank.append(int(movie_title[0]))
    elif ':' in text:
        movie_title = text.split(':')
        movie_name.append(movie_title[1].strip())
        movie_rank.append(int(movie_title[0]))

# Combine the two lists into a list of tuples (title, rank)
final_movie_list = list(zip(movie_rank,movie_name))
# Sort the list of tuples based on rank (ascending order)
final_movie_list.sort()

# Write the sorted movie titles along with their ranks to a text file
with open('movies.txt', 'w', encoding='utf-8') as file:
    for rank, title in final_movie_list:
        file.write(f"{rank}) {title}\n")

print("Movies list generated successfully!")