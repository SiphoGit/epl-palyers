# Create a new file named 'utils.py' inside 'epl_players_scraper' lambda
# Copy and paste this code in 'utils.py'

url = "https://footballapi.pulselive.com/football/players?pageSize=2&compSeasons=719&altIds=true&page=0&type=player&id=-1&compSeasonId=719"

payload = {}
headers = {
'accept': '*/*',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'no-cache',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'origin': 'https://www.premierleague.com',
'pragma': 'no-cache',
'priority': 'u=1, i',
'referer': 'https://www.premierleague.com/',
'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

