import requests

url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

querystring = {"game":"8133"}

headers = {
	"x-rapidapi-key": "89e8d18db2msh750cb1be8006c38p19c402jsne47214e05847",
	"x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())