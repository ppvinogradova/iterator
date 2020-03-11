import json
from pprint import pprint

# class CountriesWiki:

#   def __init__(self, path):
#     self.path = path
#     self.file = open(self.path, encoding = 'utf8')
  


with open('countries.json') as f:
  info = json.load(f)
  for c in info:
    country = c['name']['common']


  #f'https://ru.wikipedia.org/wiki/{country}'