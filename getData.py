

from urllib.request import urlopen
from bs4 import BeautifulSoup
import gzip
import json



class getData:


    def __init__ (self, url):
        print ("Getting the data..")
        self.url = url
        self.movies_links = []
        self.dict = {}

# will dowload page source
    def getMovies (self):
        print ("Gathering the list of movies..")
        data = urlopen(self.url).read()
        data = gzip.decompress(data).decode()
        soup = BeautifulSoup(data, "html.parser")    
# will extract the links for the movies        
        line = 0
        for links in soup.findAll("a"):
            if line > 23 and line < 324:    
                link = links["href"]
                movie_url = "https://www.csfd.cz/"+ link
                self.movies_links.append(movie_url)
            line += 1
        
# will go to each page, gather actors, fill dictionary
    def getActors (self):
        print ("Working on the actors..")
        decompress_err = 0
# open each link
        for i in self.movies_links:
            data = urlopen(i).read()
            try:
                data = gzip.decompress(data)
            except:
                decompress_err += 1
                continue
            soup = BeautifulSoup(data.decode("utf-8"), "html.parser")
            soup = soup.get_text().splitlines()
# look for the actors
            no_lines = 0
            for line in soup:
                no_lines += 1
                if "Hrají:" in line:
                    break 
# put actors in the list
            actors = list(soup[no_lines + 1].split(","))
# get the movie name
            movie_name = soup[8].rstrip(" | ČSFD.cz")
# put the movie : actors into the dict
            self.dict[movie_name] = actors
        # print ("Decompress errors: {}".format(decompress_err))
# save the dict in JSON file
    def saveData (self):
        print ("Saving the data..")
        with open('outcome.json', 'w') as fp:
            json.dump(self.dict, fp, indent=4, ensure_ascii=False)



base_file = getData("https://www.csfd.cz/zebricky/nejlepsi-filmy/?show=complete")
base_file.getMovies()
base_file.getActors()
base_file.saveData()

    

