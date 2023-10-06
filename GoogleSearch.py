# pip install google
# pip install googlesearch-python

from googlesearch import search

def fetch_google_results(query, num_results=10):
    try:
        search_results = search(query, num=num_results, stop=num_results)
        return list(search_results)
    except Exception as e:
        print("An error occurred:", e)
        return []

def main():
    query = input("Enter your search query: ")
    num_results = 10  # change this if you want different number of results

    results = fetch_google_results(query, num_results)

    if results:
        print("\nTop", num_results, "results for:", query)
        for idx, result in enumerate(results, start=1):
            print(idx, "-", result)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
