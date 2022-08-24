
import requests
from bs4 import BeautifulSoup
import os
import time

def main():
    # this is the url for the page I want to take
    url = "https://readberserk.com/chapter/berserk-chapter-a0/"
    
    # grab the html
    r = requests.get(url)

    #parse the html
    soup = BeautifulSoup(r.text, "html.parser")
    
    # find all images
    images = soup.find_all('img')
    
    # loop through all the images
    i = 1
    os.chdir("ep1")
    for image in images:
        name = "image_" + str(i)
        i += 1
        # get the image section
        link = image["src"]
        print(name)
        print(link)
        try:
            # ask nicely for the jpg
            im = requests.get(link)
            # if rude try again
        except OSError:
            print("failed on " + name)
            time.sleep(3)
            im = requests.get(link)

        # write it to a file
        with open(name + ".jpg", "wb") as f:
            f.write(im.content)


if __name__ == "__main__":
    main()
