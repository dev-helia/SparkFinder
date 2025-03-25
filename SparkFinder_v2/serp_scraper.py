from serpapi import GoogleSearch
import csv

# move into other file in the future
API_KEY = "c1eb68fc3323afd8fc17c6c2784380fbb1b7e26d62278bc57fa5c55ce5f7e21b"

def search_google(query, num_results=10):
    params = {
        "engine": "google",
        "q": query,
        "api_key": API_KEY,
        "num": num_results
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results.get("organic_results", [])
    
    return [(r.get("title"), r.get("link")) for r in organic_results]

def main():
    with open("keywords.txt", "r") as f:
        keywords = [line.strip() for line in f.readlines() if line.strip()]

    with open("results.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Keyword", "Title", "Link"])

        for kw in keywords:
            print(f"Searching: {kw}")
            results = search_google(kw)
            for title, link in results:
                writer.writerow([kw, title, link])

if __name__ == "__main__":
    main()