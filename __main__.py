
import requests
from bs4 import BeautifulSoup
import os
import time


def download_web_images(url, direc):
 
    # grab the html
    r = requests.get(url)

    #parse the html
    soup = BeautifulSoup(r.text, "html.parser")
    
    # find all images
    images = soup.find_all('img')
    
    # start index for img download
    start_img = 0

    # make the directory
    try:
        os.mkdir(direc)
    except FileExistsError:
        # we are going to look for some remnents
        print("File already made, looking for remains...")
        # we need to find the last image
        done_img = os.listdir()

        # change the start img to whatever the last img is
        start_img = 


    # loop through all the images
    os.chdir(direc)
    i = 1

    for image in images[start_img:]:
        name = "image_" + str(i).zfill(3)
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
    os.chdir("..")



def main():
    main_url = "https://readberserk.com/"

    # so first we are going to go to the first web-page that stores all the web pages
    req = requests.get(main_url)
    soup = BeautifulSoup(req.text, "html.parser")
    pages = soup.find_all("tr")
    # because we are getting randome bs
    pages.pop(0)
    # look for all the important information
    all_name_date_link = []
    for page in pages:
        name_date_link = []
        for td in page.find_all("td"):
            name_date_link.append(td) 

        # get the name
        name_date_link[0] = name_date_link[0].text.replace(" ", "_")
        # get the date
        name_date_link[1] = name_date_link[1].text
        # get the link
        name_date_link[2] = name_date_link[2].div.a["href"]
        all_name_date_link.append(name_date_link)
    
    print(all_name_date_link)
    for name_date_link in all_name_date_link:
        download_web_images(name_date_link[2], name_date_link[0])
    
    # this is the url for the page I want to take
    url = "https://readberserk.com/chapter/berserk-chapter-a0/"
    
    directory = "Episode_One"
    # download_web_images(url, directory)

if __name__ == "__main__":
    main()
