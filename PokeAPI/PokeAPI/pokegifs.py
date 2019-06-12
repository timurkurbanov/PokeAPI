import jason
import requests
KEY = os.environ.get("GIPHY_KEY")

def get_json(url):
    res = requests.get(url)
    return json.loads(res.content)


pokemon = get_json("http://pokeapi.co/api/v2/pokemon/pikachu/")


print(pokemon["name"])
print(pokemon["id"])
print(pokemon["types"])


search_results = get_json(f"https://api.giphy.com/v1/gifs/search?api_key={KEY}&q=pikachu&rating=g")

giphy_url = search_results['data'][0]['url']
print(giphy_url)
