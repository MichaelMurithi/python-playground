import requests


def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    params = {"q": "stars:>50000"}
    responce = requests.get(gh_api_repo_search_url, params=params)
    responce_json = responce.json()['items']
    return responce_json


if __name__ == "__main__":
    # main methods run here
    results = repos_with_most_stars()
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} starts.")
