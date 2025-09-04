import requests

def fetch_leetcode_solved(username):
    url = f'https://leetcode-stats-api.herokuapp.com/{username}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("totalsolved",0)
    return 0