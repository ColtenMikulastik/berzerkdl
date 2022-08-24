
import requests
from bs4 import BeautifulSoup
import os


def main():
    url = "https://readberserk.com/chapter/berserk-chapter-a0/"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    images = soup.find_all('img')
    
    print(images)
    i = 1
    for image in images:
        name = "image_" + str(i)
        i += 1
        link = image["src"]
        print(name)
        print(link)
        with open(name + ".jpg", "wb") as f:
            im = requests.get(link)
            f.write(im.content)


if __name__ == "__main__":
    main()
