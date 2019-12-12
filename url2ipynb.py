import sys

from bs4 import BeautifulSoup
import json
import urllib.request
import html2md


def url2ipynb(url,outfile):

    if url.startswith('http://') or url.startswith('https://'):
            response = urllib.request.urlopen(url)
            data = response.read()
    else:
        data = open(url, 'rb').read()


    soup = BeautifulSoup(data, 'html.parser')

    ipynb = {'nbformat': 4, 'nbformat_minor': 1, 'cells': [], 'metadata': {}}
    divlist = soup.find_all('div', class_=['text_cell_render' , 'input_area'])
    if divlist:
        for d in divlist:
            if "input_area" in d['class']:
                cell = {}
                cell['metadata'] = {}
                cell['outputs'] = []
                cell['source'] = [d.get_text()]
                cell['execution_count'] = None
                cell['cell_type'] = 'code'
            else:
                cell = {}
                cell['metadata'] = {}

                cell['source'] = [html2md.html2md(str(d))]
                cell['cell_type'] = 'markdown'
            ipynb['cells'].append(cell)
        open(outfile, 'w').write(json.dumps(ipynb))

if __name__ == '__main__':
   
    if len(sys.argv) < 2:
        print('Usage: url2ipynb url|filename outputfile')
    else:
        url2ipynb(sys.argv[0], sys.argv[1])
    
