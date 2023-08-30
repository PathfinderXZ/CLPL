import requests
import webbrowser as wb
from dotenv import load_dotenv
import os

load_dotenv(__file__[:-18] + "config/.env")
n_pages = 2

def safety():
    queries = []
    compound_count = int(input("No. of compounds: "))

    for i in range(1, compound_count + 1):
        compound = input(f"Compound {i}: ")
        queries.append(f"{compound} safety data sheet")

    url = "https://www.googleapis.com/customsearch/v1"

    for i in range(compound_count):
        params = {
            "q": queries[i],
            "key": os.getenv("GOOGLE_SEARCH_API_KEY"),
            "cx": os.getenv("GOOGLE_SEARCH_ENGINE_KEY")
        }

        response = requests.get(url=url, params=params)
        results = response.json()

        if "items" in results:
            for page_num in range(0, n_pages):
                wb.open_new_tab(results["items"][page_num]["link"])

if __name__ == "__main__":
    safety()
