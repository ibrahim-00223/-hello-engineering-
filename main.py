import requests


def rechercher_la_poste():
    url = "https://recherche-entreprises.api.gouv.fr/search?q=la%20poste&page=1&per_page=1"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = rechercher_la_poste()
    print(data)
