import json
import wikipedia

def make_list(file):
  with open(file,'r') as f:
    info = json.load(f)
    with open('countries_list.txt', 'w') as f:
      for c in info:
        country = c['name']['common']
        c = country + '\n'
        f.write(c)

class CountriesWiki:

  def __init__(self, path):
    self.file = open(path, encoding = 'utf-8')

  def __iter__(self):
    return self

  def __next__(self):
    line = self.file.readline().strip()
    page_id = line + '(country)'
    try:
      page = wikipedia.page(page_id)
      wiki_url = page.url
    except wikipedia.exceptions.PageError:
      wiki_url = 'no page found'
    finally:
      string = line + ': ' + wiki_url + '\n'
      if not line:
        raise StopIteration
      return string

if __name__ == '__main__':
  make_list('countries.json')
  with open('results.txt', 'w') as f:
    for result in CountriesWiki('countries_list.txt'): 
      f.write(result)
      print('.')
  