from bs4 import BeautifulSoup
import requests

url = "https://www.filmweb.pl/showtimes/Warszawa"
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

print("""Repertuar kin w Warszawie oraz ocena punktowa wg Filmweb:
""")

film = []
for page in soup.find_all(class_="poster fImg140"):
  i = str(page).split(">")[2].split('"')[1]
  film.append(i)

score = []
for page_score in soup.find_all(class_="space-left"):
  b = str(page_score).split(">")[1].split("<")[-2]
  score.append(b)

for x, y in zip(film, score):
  print(f'"{x}" - {y} pkt.')

