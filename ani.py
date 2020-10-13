import requests

query = '''
    query ($id: Int) { # Define which variable will be used in the query (id)
    Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    id
    title {
        romaji
        english
        native
        }
    }
}
'''

variables = {
    'id': 15125
}

api_url = 'https://graphql.anilist.co'

response = requests.post(api_url, json={'query': query, 'variables': variables}).json()
print(response)