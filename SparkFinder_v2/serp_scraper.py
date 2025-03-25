from serpapi import GoogleSearch
import csv

# move into other file in the future
API_KEY = "c1eb68fc3323afd8fc17c6c2784380fbb1b7e26d62278bc57fa5c55ce5f7e21b"

def search_google(query, num_results=10):
    params = {
        "engine": "google", # search engine
        "q": query, # search query
        "api_key": API_KEY, # API key
        "num": num_results # number of results to return
    }
    
    search = GoogleSearch(params) # create a GoogleSearch object with the params dictionary
    results = search.get_dict() # get the results as a dictionary
    organic_results = results.get("organic_results", []) # get the organic results
    
    # return a list of tuples containing the title and link of each result
    # [("Title1", "https://link1.com"), ("Title2", "https://link2.com"), ...]
    return [(r.get("title"), r.get("link")) for r in organic_results] 

def main():
    # read keywords from file
    # Open the keyword file, one keyword oneline, save as a list 'keywords'
    with open("keywords.txt", "r") as f:
        keywords = [line.strip() for line in f.readlines() if line.strip()]

    # create a CSV file to store the results
    with open("results.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Keyword", "Title", "Link"])

        # search for each keyword and write the results to the CSV file
        for kw in keywords:
            print(f"Searching: {kw}")
            results = search_google(kw)
            for title, link in results:
                writer.writerow([kw, title, link])

if __name__ == "__main__":
    main()