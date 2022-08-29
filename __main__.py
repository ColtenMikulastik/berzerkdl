
import requests
from bs4 import BeautifulSoup
import os
import time
import threading


# I need to:
# 1: encapsulate the download_web_imgs func into smaller functions
# 2: then implemnet queueing
# 3: then implement threading
# 
# bug list: if you run in restart mode, it will delete every last file and redownload it

def get_img_list(url): 
    # grab the html
    r = requests.get(url)

    #parse the html
    soup = BeautifulSoup(r.text, "html.parser")
    
    # find all images
    images = soup.find_all('img')
    return images


def download_web_images(url, direc):
    
    # call teh html parser to get img on web page
    images = get_img_list(url)

    # start index for img download
    start_img = 0
    
    # defining my indexr early
    i = 1

    # make the directory
    try:
        os.mkdir(direc)
    except FileExistsError:
        # we are going to look for some remnents
        print("File already made, looking for remains...")
        
        # change to the dir rq
        os.chdir(direc)
        # we need to find the last image
        done_img = os.listdir()

        # make array to store numbers
        img_num = []
        for img in done_img:
            # get num val from file name
            img_num.append(int(img[6:9]))
            
        # change the start img to whatever the last existing img is...
        i = max(img_num)
        start_img = i - 1

        # so dont forget to delete the last img, cause it's very likely courrupted
        os.remove("image_" + str(i).zfill(3) + ".jpg")

        # go back
        os.chdir("..")


    # loop through all the images
    os.chdir(direc)
    real_img_lst = []
    # loop and download 
    for image in images[start_img:]:
        # get the image section
        link = image["src"]
        
        # attempt to download http content
        try:
            # ask nicely for the jpg
            im = requests.get(link)
            real_img_lst.append(im)
            # if rude try again
        except OSError:
            print("failed on " + name)
            time.sleep(3)
            im = requests.get(link)
            real_img_lst.append(im)
    
    # loop the images and save them in files
    for real_img in real_img_lst:
        # create the syntax for the file
        name = "image_" + str(i).zfill(3)
        i += 1
        print("writing " + link + " to file: " + name)
        # write it to a file
        with open(name + ".jpg", "wb") as f:
            f.write(real_img.content)
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
