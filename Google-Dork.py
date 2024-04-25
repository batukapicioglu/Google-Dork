import requests
from bs4 import BeautifulSoup
import time
import sys

def print_help():
    print("Welcome to Google Dork Search!")
    print("Usage: python google_dork_search.py [options]")
    print("Options:")
    print("-h, --help                Show this help message and exit")
    print("Available Dork Options:")
    print("1. intext                  Search for a keyword in text")
    print("2. intitle                 Search for a keyword in title")
    print("3. inurl                   Search for a keyword in URL")
    print("4. maps                    Search for a location in maps")
    print("5. ext                     Search for a file extension")
    print("6. book                    Search for a book")
    print("7. allintext               Search for all keywords in text")
    print("8. allintitle              Search for all keywords in title")
    print("9. related                 Search for related results")
    print("10. info                   Search for information about a keyword")
    print("11. link                   Search for linked results")
    print("12. cache                  Search for cached results")
    print("13. site                   Search for a keyword in a specific site")
    print("14. filetype               Search for a specific file type")
    print("Type 'done' when finished.")
    sys.exit()

def google_search_with_dork(dork_query):
    url = f"https://www.google.com/search?q={dork_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    print("Performing Google search...")
    for _ in range(10):  # Simulating loading with a loop
        time.sleep(0.1)
        print(".", end="", flush=True)
    print("\n")  # Print a newline after loading is finished

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all("div", class_="tF2Cxc")
        if not search_results:
            print("No results found.")
        else:
            for result in search_results:
                title = result.find("h3").text
                link = result.a["href"]
                print(f"Title: {title}")
                print(f"Link: {link}")
                print("-" * 50)
    else:
        print("Failed to retrieve search results.")

if __name__ == "__main__":
    print("Welcome to Google Dork Search!")

    while True:
        print("Please select the options you want to search with:")
        print("Type 'done' when finished.")
        print("Available Dork Options:")
        print("1. intext")
        print("2. intitle")
        print("3. inurl")
        print("4. maps")
        print("5. ext")
        print("6. book")
        print("7. allintext")
        print("8. allintitle")
        print("9. related")
        print("10. info")
        print("11. link")
        print("12. cache")
        print("13. site")
        print("14. filetype")
        
        dork_options = input("Enter your choice(s) separated by comma (e.g., 2, 9, 10): ").split(",")

        if "done" in dork_options:
            break
        else:
            keywords = []
            for option in dork_options:
                if option.strip() in [str(i) for i in range(1, 15)]:
                    keyword = input(f"Enter the keyword of {option}: ")
                    keywords.append(keyword)
                else:
                    print("Invalid option! Please choose a valid option.")

            dork_query = ""
            for option, keyword in zip(dork_options, keywords):
                if option == "5":
                    keyword = f".{keyword}"
                if option == "1":
                    keyword = f"\"{keyword}\""
                if option == "2":
                    keyword = f"intitle:\"{keyword}\""
                if option == "3":
                    keyword = f"inurl:\"{keyword}\""
                dork_query += f"{['intext', 'intitle', 'inurl', 'maps', 'ext', 'book', 'allintext', 'allintitle', 'related', 'info', 'link', 'cache', 'site', 'filetype'][int(option)-1]}:{keyword} "
            
            google_search_with_dork(dork_query)

    print("Thank you for using Google Dork Search!")
