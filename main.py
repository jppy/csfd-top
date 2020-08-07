# download list of movies > store them > create webapp > seach in the data

from getData import getData

# Are we going to dowload the data?
q = input("Do you want to download the data? (Y/N)").lower()
while q != "y" or q != "n":
    if q == "y":
        base_file = getData("https://www.csfd.cz/zebricky/nejlepsi-filmy/?show=complete")
        base_file.getMovies()
        base_file.getActors()
        base_file.saveData()
        break
    elif q == "n":
        print ("Continuing..")
        break
    else:
        print ("Incorrect input, please answer 'Y'/'N'")
        q = input("Do you want to download the data? (Y/N)").lower()

# Run the DB

# Pop the app

# Search 